from rest_framework import serializers
from django.utils import timezone, dateformat

from .models import Article as ArticleModel
from .models import Comment as CommentModel
from user.models import User as UserModel
from user.models import UserInfo as UserInfoModel
from user.models import ArticleLike as ArticleLikeModel
from user.models import Planet as PlanetModel


class CommentPostSerializer(serializers.ModelSerializer):

    def validate(self, data):
        if len(data.get('content')) < 0:
            raise serializers.ValidationError(
                detail={"error": "내용을 작성해주세요!"},
            )
        return data

    def create(self, validated_data):   
        comment = CommentModel(**validated_data)
        comment.save()
        return validated_data

    def update(self, instance, validated_data):
        formatted_date = dateformat.format(timezone.now(), 'y.m.d H:i')

        for key, value in validated_data.items():
            if key == 'content':
                value = value + f'\r\n({formatted_date}에 마지막으로 수정됨)'
                setattr(instance, key, value)
        instance.save()
        return instance

    class Meta:
        model = CommentModel
        fields = "__all__"


class ArticlePostSerializer(serializers.ModelSerializer):

    def validate(self, data):
        if len(data.get('title')) < 0:
            raise serializers.ValidationError(
                detail={"error": "제목은 비워둘 수 없습니다."},
            )
        if len(data.get('content')) < 0:
            raise serializers.ValidationError(
                detail={"error": "내용은 비워둘 수 없습니다."},
            )
        return data

    def create(self, validated_data):   
        article = ArticleModel(**validated_data)
        article.save()
        return validated_data

    def update(self, instance, validated_data):
        formatted_date = dateformat.format(timezone.now(), 'y.m.d H:i')

        for key, value in validated_data.items():
            if key == 'content':
                value = value + f'\r\n\r\n({formatted_date}에 마지막으로 수정됨)'
                setattr(instance, key, value)
        instance.save()
        return instance

    class Meta:
        model = ArticleModel
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    create_date = serializers.SerializerMethodField()
    reply = serializers.SerializerMethodField()
    reply_cnt = serializers.SerializerMethodField()
    author_name = serializers.SerializerMethodField()

    def get_author_name(self, obj):
        return obj.author.nickname

    def get_create_date(self, obj):
        return dateformat.format(obj.create_date, 'y.m.d H:i:s')

    def get_reply_cnt(self, obj):
        try:
            return obj.comment_set.all().count()
        except:
            return 0

    def get_reply(self, obj):
        try:
            serializer = self.__class__(obj.comment_set, many=True)
            serializer.bind('', self)
            return serializer.data
        except:
            pass


    class Meta:
        model = CommentModel
        fields = [
            "id",
            "article",
            "parent",
            "author",
            "author_name",
            "content",
            "create_date",
            "reply_cnt",
            "reply",
        ]


class ArticleSerializer(serializers.ModelSerializer):
    create_date = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    comments_cnt = serializers.SerializerMethodField()
    author_name = serializers.SerializerMethodField()

    def get_author_name(self, obj):
        return obj.author.nickname

    def get_comments_cnt(self, obj):
        return obj.comment_set.all().count()

    def get_create_date(self, obj):
        return dateformat.format(obj.create_date, 'y.m.d H:i:s')

    def get_comments(self, obj):
        try:
            comments = obj.comment_set.filter(parent=None)
            serializer = CommentSerializer(comments, many=True)
            return serializer.data
        except:
            pass


    class Meta:
        model = ArticleModel
        fields = [
            "id",
            "planet",
            "author",
            "author_name",
            "title",
            "content",
            "picture_url",
            "create_date",
            "comments_cnt",
            "comments",
        ]


class BoardSerialzer(serializers.ModelSerializer):
    create_date = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    detail_url = serializers.SerializerMethodField()
    author_name = serializers.SerializerMethodField()

    def get_author_name(self, obj):
        return obj.author.nickname

    def get_create_date(self, obj):
        return dateformat.format(obj.create_date, 'y.m.d')

    def get_comments(self, obj):
        comments = obj.comment_set.all()
        return comments.count()

    def get_detail_url(self, obj):
        return f'article.html?board={obj.planet.id}&article={obj.id}'


    class Meta:
        model = ArticleModel
        fields = [
            "id",
            "author",
            "author_name",
            "title",
            "detail_url",
            "create_date",
            "comments",
        ]