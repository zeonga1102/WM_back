![image](https://user-images.githubusercontent.com/71905164/182584327-171cf850-0bd8-4d62-bdec-1ba090eb9b71.png)
# 🚀MakeMigrations
딥페이크를 이용하여 움직이는 사진을 생성, 지구 밖 행성으로 이주한 사람들의 시민권을 만들어주는 웹사이트

커뮤니티 기능 및 마이 페이지에서 방 꾸미는 기능 등
# ⭐Intro
* 다른 행성들로 이주해서 생활한다는 컨셉의 커뮤니티
* 딥페이크를 이용해서 사진을 움직이게 만들어줌
* **개발 기간**: 2022.07.07 ~ 2022.08.16 (사용자 피드백 반영 기간 2022.08.08 ~ 2022.08.11)
* **개발 인원(4명)**: 김동근, 노을, 이정아, 이현경
* **Team** <a href="https://github.com/cmjcum/WM_back"><img src="https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white"/></a>
* **S.A** <a href="https://cold-charcoal.tistory.com/118">블로그로 이동(☞ﾟヮﾟ)☞</a>
# 🪐Project
### Frontend Repository
<a href="https://github.com/zeonga1102/WM_front"><img src="https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white"/></a>
### 사용 기술
* Python 3.7
* Django REST Framework 3.13
* Docker, Docker-compose
### 핵심 기능
게시판과 마이홈을 통한 회원들 간의 소통과 상점에서 구입한 가구를 통해 방을 꾸미는 기능
* JWT를 이용한 로그인
* 딥페이크를 통한 움직이는 사진 생성
* 게시판 별 게시글과 댓글 CRUD
* 가구 상점과 상점에서 구매한 가구로 방 꾸미기
### 맡은 부분
<details>
<summary>유저 상세 정보 저장 및 프로필 사진에 딥페이크 적용 <a href="https://github.com/cmjcum/WM_back/blob/master/user/views.py#L45">📑코드</a></summary>

유저들의 시민증을 만들어주기 위해 상세 정보를 저장합니다.<br>
이때 사용자가 입력한 사진은 딥페이크를 적용해서 사진이 움직이게 했습니다. 딥페이크는 적용되는데 시간이 오래 걸리므로 멀티 프로세싱을 이용하였습니다.<br>
[📑딥페이크 적용 코드](https://github.com/cmjcum/WM_back/blob/master/deeplearning/deeplearning_make_portrait.py#L88)
</details>
<details>
<summary>방 꾸민 내용 저장 <a href="https://github.com/cmjcum/WM_back/blob/master/myroom/views.py#L124">📑코드</a></summary>

Seralizer를 이용해 현재 유저가 방을 꾸민 내용을 저장합니다.<br>
기존의 배치를 모두 지우고 현재 유저가 어떤 가구를 어떤 위치에 어떤 방향으로 배치했는지 Serializer를 통해 저장합니다.
</details>
<details>
<summary>보유 가구 불러오기 <a href="https://github.com/cmjcum/WM_back/blob/master/myroom/views.py#L119">📑코드</a></summary>

유저는 상점을 통해 구매한 가구만을 이용해 방을 꾸밀 수 있습니다.<br>
방 꾸미기 버튼을 눌렀을 때 유저가 구매한 가구들의 목록을 보여줍니다.
</details>
<details>
<summary>방 불러오기 <a href="https://github.com/cmjcum/WM_back/blob/master/myroom/views.py#L145">📑코드</a></summary>

각 유저가 꾸민 방 정보를 불러옵니다.<br>
현재 방문한 유저의 방 배치를 보여줍니다. 만약 10번 유저의 마이홈에 방문했다면 10번 유저가 꾸며둔 방을 보게됩니다.
</details>
<details>
<summary>상점 페이지에서 가구 조회 <a href="https://github.com/cmjcum/WM_back/blob/master/myroom/views.py#L152">📑코드</a></summary>

상점에서는 현재 유저가 이미 구매한 가구를 제외한 가구들의 목록을 보여줍니다.<br>
그리고 상점 페이지에서도 현재 보유 코인을 확인할 수 있게 했습니다. 백엔드만 작업했습니다.
</details>
<details>
<summary>상점 페이지에서 가구 구매 <a href="https://github.com/cmjcum/WM_back/blob/master/myroom/views.py#L161">📑코드</a></summary>

유저가 선택한 가구를 구매합니다.<br>
선택한 가구를 유저 보유 가구에 추가하고 보유 코인을 차감합니다. 만약 보유 코인이 구매하려는 가구의 가격보다 적다면 구매할 수 없습니다.<br>
구매에 성공하면 프론트로 True를, 보유 코인이 적어 실패하면 False를 전송합니다.
</details>
<details>
<summary>상점 페이지에서 가구 검색 <a href="https://github.com/cmjcum/WM_back/blob/master/myroom/views.py#L185">📑코드</a></summary>

상점 페이지에서 가구를 검색한 결과를 보여줍니다.<br>
유저가 보유하지 않은 가구들을 가구의 이름을 기준으로 검색을 하고 그 결과를 전송합니다.<br>
가구 이름과 검색어가 완전히 일치하지 않고 입력한 검색어를 이름에 포함하기만 해도 결과로 나옵니다.<br>
원래 전체 가구 목록에 존재하는 가구여도 유저가 이미 구매하였으면 검색 결과로 나오지 않습니다.<br>
만약 A라는 가구가 존재하고 유저가 구매했으면 A를 검색했을 때 A는 검색 결과에 나오지 않습니다.
</details>

### ERD
![make migrations (6)](https://user-images.githubusercontent.com/71905164/182602214-7d8cf839-76d6-4d30-af03-99d5f9481137.png)
# 🛠Troubleshooting
### XSS 공격 대응
처음 배포를 한 상태에서는 XSS 공격 가능성을 전혀 고려하지 못해 우리 웹사이트가 XSS 공격을 받았습니다. 보통 우리가 넣지 않은 alert을 띄우는 정도의 공격이었지만 아예 페이지에 접근이 안 되게 하는 경우도 있었습니다.<br>
XSS 공격에 대응하는 방법은 많지만 우리는 백엔드에서 게시글 등 사용자가 조회할 수 있는 텍스트들을 저장할 때 부등호 기호(<, >)를 전부 html 특수문자 코드로(\&lt;, \&gt;) 바꾸어 저장했습니다. Seralizer를 통해 저장할 때 validator를 커스텀 해 replace 함수로 문자열을 바꿔주었습니다.
```python
content_data = data.get('content')
if '<' in data.get('content'):
  content_data = content_data.replace('<', '&lt;')
  if '>' in data.get('content'):
    data['content'] = content_data.replace('>', '&gt;')
```
# 🖋회고
# 🌠Credit
* 프로젝트에 사용된 모든 가구 벡터는 <a href='https://kr.freepik.com/author/macrovector'>macrovector - kr.freepik.com가 제작함</a>
* <a href="https://www.flaticon.com/free-icons/planet" title="planet icons">Planet icons created by Eucalyp - Flaticon</a>
