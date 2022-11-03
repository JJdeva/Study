# doit django

doit django 책을 클론하면서 내용 정리



## 웹 사이트 구조 구상

- 대문 페이지
- 블로그 페이지
- 자기소개 페이지



- 대문 페이지
    - 랜딩(landing)페이지라고 도 함
    - 웹 사이트에 처음 접속할 때 나타나는 일종의 대문 역할
- 블로그 페이지
    - 평소에 공부한 내용이나 살면서 느낀 점들을 기록하는 공간
    - 포스트 목록 페이지(post list)
    - 포스트 상세 페이지(post detail)
- 자기 소개 페이지
    - 나에 대해 알릴 수 있는 페이지



## 초기 설정

프로젝트 생성

```
> django-admin startporject config .
```



db 생성(migration)

```
> python manage.py migrate
```



관리자 계정 생성

```
> python manage.py createsuperuser
jay/4354
```



gitignore에 sqlite3 제외시키기

```
# .gitignore
db.sqlite3
```



settings.py에서 언어랑 타임존 변경

```python
# settings.py

LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'

USE_TZ = False
```



## 앱 생성

App

- blog : 블로그 페이지를 위한 앱
- single_pages : 대문 페이지와 자기소개 페이지를 위한 앱



앱 생성

```
python manage.py startapp blog
python manage.py startapp single_pages
```



settings.py의 INSTALLED_APPS에 생성한 앱 등록

```python
INSTALLED_APPS = [
    'blog.apps.BlogConfig',
    'single_pages.apps.SinglePagesConfig',
    ...
]
```



## 모델 생성

모델 생성 = db 테이블 스키마 생성



### blog 모델 생성

- Post 모델
    - attributes
        - title(제목)
        - content(내용)
        - created_at(작성일)
        - author(작성자)

```python
# blog/models.py

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField() # 월, 일, 시, 분, 초까지 기록가능한 필드
```

db에 마이그레이션 해주기

```
python manage.py makemigrations
python manage.py migrate
```



gitignore에 migrations 등록해 제외시켜주기

- models 수정할 일이 많을텐데 모델 수정 내역을 일일이 커밋해주면 나중에 데이터베이스 충돌이 일어날 수 있음

```
# .gitignore
migrations/
```



관리자 페이지에 Post모델 추가하기

```python
# blog/admin.py

from django.contrib import admin
from .models import Post

admin.site.register(Post)
```



str메소드 추가해서 보기 좋게 해주기

- 글 번호랑 제목 보이게 해주기

```python
# blog/models.py

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField() # 월, 일, 시, 분, 초까지 기록가능한 필드
    
    def __str__(self):
        return f'[{self.pk}] {self.title}'
```



자동으로 생성시간 등록과 수정시간까지 생기게 만들기

- auto_now_add : 생성시 자동으로 지금 시간 추가
- auto_now : 수정사항 생성시 시간 변경

```python
# blog/models.py

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'[{self.pk}] {self.title}'
```





## url 등록

기본 url 생성 계획

<table>
    <tr>
    	<th colspan="2">페이지</th>
        <th>URL</th>
    </tr>
    <tr>
    	<td colspan="2">대문페이지</td>
        <td>도메인/</td>
    </tr>
    <tr>
        <td rowspan="2">블로그페이지</td>
        <td>포스트목록</td>
        <td>도메인/blog/</td>
    </tr>
    <tr>
        <td>포스트상세</td>
        <td>도메인/blog/포스트_pk</td>
    </tr>
    <tr>
    	<td colspan="2">자기소개페이지</td>
        <td>도메인/about_me/</td>
    </tr>
</table>



config/urls.py에 path include등록

```python
# config/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]
```



### blog url

```python
# blog/urls.py

from django.urls import path
from . import views

urlpattern = [
    path('', views.index),
]
```







## view

### FBV

함수 기반 뷰 (function based view)

```python
# blog/views.py

from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('-pk')

    return render(request, 'blog/index.html', {'posts' : posts,})
```









### CBV

클래스 기반 뷰 (class based view)

`django.views.generic`에서 임포트





#### ListView

리스트(목록)를 나열할 때 쓰는 뷰 클래스

--> `from django.views.generic import ListView`

ListView를 상속받아서 뷰를 만들면 된다.

```python
class PostList(ListView):
    model = Post
    template_name = 'blog/index.html'
    ordering = '-pk'
    
# 또는 그냥 as_view()까지 써서 바로 보내버려도 됨
# 예시
# post_detail = DetailView.as_view(model=Post, pk_url_kwarg='id')
```

- model= : view에서 쓸 모델만 지정하면 끝
- templates 오류가 나는데 default로 html을 불러올 때 `모델명_list.html`을 찾아서 불러옴. 여기선 post_list.html
- 그냥 편하게 template_name을 지정하는게 좋음
- FBV에선 render에 context 해쉬를 넣어줬어야 했는데 여긴 그냥 `모델명_list`라고 템플릿에서 쓰면 자동으로 객체를 불러옴
- ordering도 지원



#### DetailView

얘도 마찬가지로 template찾을 때 post_detail.html로 찾음











## ORM

Object Relational Mapping(객체 관계 매핑)



ORM에서는 객체(장고에선 모델)명을 table명으로 씀

blog에서 Post모델을 만들었음

```python
from blog.models import Post

p = Post.objects.all()
```











get_absolute_url()함수

```python
def get_absolute_url(self):
    return f'/blog/{self.pk}/'
```



이미지필드

- `ImageField(upload_to='업로드할경로/%Y/%m/%d/', blank=True)`
- 이미지를 업로드하면 경로로 년,월,일 디렉토리에 저장됨
- blank는 이미지를 넣어야하나 안넣어야하냐
    - True면 이미지 삽입이 필수가 아니란거

파일필드

- `FileField(upload_to='파일경로/%Y/%m/%d/', blank=True)`
- 파일을 업로드할 수 있는 필드 (이미지 외의 파일말하는거)







<!-- <script src="{% static 'blog/bootstrap/bootstrap.min.js %}"></script> -->









about_me

```html
<!DOCTYPE html>
<html>
    <head>
        <title>About me</title>
        <style>
            nav {
                background-color: darkgree;
                font-size: 150%;
                text-align: center;
            }
            nav a {
                color: gold;
            }
        </style>
    </head>
    <body>
        <nav>
        	<a href="./index.html">Home</a>
            <a href="./blog_list.html">Blog</a>
            <a href="./about_me.html">About me</a>
        </nav>
        
        <h1>About Me</h1>
        <h2>서울사람 이성용입니다. </h2>
        <p>HTML, CSS JS, DJANGO로 재미있는 웹 사이트 만드는 것을 좋아합니다. </p>
        <a href="index.html">첫 화면으로 가기</a>
    </body>
</html>
```

blog_list.html

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Blog</title>
        <style>
        	            nav {
                background-color: darkgree;
                font-size: 150%;
                text-align: center;
            }
            nav a {
                color: gold;
            }
        </style>
    </head>
    <body>
		<nav>
        	<a href="./index.html">Home</a>
            <a href="./blog_list.html">Blog</a>
            <a href="./about_me.html">About me</a>
        </nav>
        
        
        <h1>Blog</h1>
		<p>아직 작성하지 않았습니다.</p>
    </body>
</html>
```



detail

```
{% extends 'blog/base.html' %}

{% block main_area %}
{% load static %}
    <!-- Page content-->
    <div class="container">
        <div class="row">
            <div class="col-lg-8">
                <!-- Post content-->
                <h1 class="mt-4">{{ post.title }}</h1>
                <h5 class="text-muted">{{ post.hook_text }}</h5>
                <p class="lead">
                    by
                    <a href="#">작성자명 쓸 위치(개발예정)</a>
                </p>
                <hr>
                <p>{{ post.created_at }}</p>
                {% if post.head_image %}
                    <hr>
                    <img class="img-fluid rounded" src="{{ post.head_image.url }}" alt="">
                {% endif %}
                <hr>
                <p>{{ post.content }}</p>
                <hr>
                {% if post.file_upload %}
                    <a href="{{ post.file_upload.url }}" class="btn btn-outline-dark mb-3" role="button" download>Download</a>
                {% endif %}
                <!-- Comments section-->
                <section class="mb-5">
                    <div class="card bg-light">
                        <div class="card-body">
                            <!-- Comment form-->
                            <form class="mb-4"><textarea class="form-control" rows="3" placeholder="Join the discussion and leave a comment!"></textarea></form>
                            <!-- Comment with nested comments-->
                            <div class="d-flex mb-4">
                                <!-- Parent comment-->
                                <div class="flex-shrink-0"><img class="rounded-circle" src="https://dummyimage.com/50x50/ced4da/6c757d.jpg" alt="..." /></div>
                                <div class="ms-3">
                                    <div class="fw-bold">Commenter Name</div>
                                    If you're going to lead a space frontier, it has to be government; it'll never be private enterprise. Because the space frontier is dangerous, and it's expensive, and it has unquantified risks.
                                    <!-- Child comment 1-->
                                    <div class="d-flex mt-4">
                                        <div class="flex-shrink-0"><img class="rounded-circle" src="https://dummyimage.com/50x50/ced4da/6c757d.jpg" alt="..." /></div>
                                        <div class="ms-3">
                                            <div class="fw-bold">Commenter Name</div>
                                            And under those conditions, you cannot establish a capital-market evaluation of that enterprise. You can't get investors.
                                        </div>
                                    </div>
                                    <!-- Child comment 2-->
                                    <div class="d-flex mt-4">
                                        <div class="flex-shrink-0"><img class="rounded-circle" src="https://dummyimage.com/50x50/ced4da/6c757d.jpg" alt="..." /></div>
                                        <div class="ms-3">
                                            <div class="fw-bold">Commenter Name</div>
                                            When you put money directly to a problem, it makes a good headline.
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- Single comment-->
                            <div class="d-flex">
                                <div class="flex-shrink-0"><img class="rounded-circle" src="https://dummyimage.com/50x50/ced4da/6c757d.jpg" alt="..." /></div>
                                <div class="ms-3">
                                    <div class="fw-bold">Commenter Name</div>
                                    When I look at the universe and all the ways the universe wants to kill us, I find it hard to reconcile that with statements of beneficence.
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>
            <!-- Side widgets-->
            <div class="col-lg-4">
                <!-- Search widget-->
                <div class="card mb-4">
                    <div class="card-header">Search</div>
                    <div class="card-body">
                        <div class="input-group">
                            <input class="form-control" type="text" placeholder="Enter search term..." aria-label="Enter search term..." aria-describedby="button-search" />
                            <button class="btn btn-primary" id="button-search" type="button">Go!</button>
                        </div>
                    </div>
                </div>
                <!-- Categories widget-->
                <div class="card mb-4">
                    <div class="card-header">Categories</div>
                    <div class="card-body">
                        <div class="row">
                            <div class="col-sm-6">
                                <ul class="list-unstyled mb-0">
                                    <li><a href="#!">Web Design</a></li>
                                    <li><a href="#!">HTML</a></li>
                                    <li><a href="#!">Freebies</a></li>
                                </ul>
                            </div>
                            <div class="col-sm-6">
                                <ul class="list-unstyled mb-0">
                                    <li><a href="#!">JavaScript</a></li>
                                    <li><a href="#!">CSS</a></li>
                                    <li><a href="#!">Tutorials</a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- Side widget-->
                <div class="card mb-4">
                    <div class="card-header">Side Widget</div>
                    <div class="card-body">You can put anything you want inside of these side widgets. They are easy to use, and feature the Bootstrap 5 card component!</div>
                </div>
            </div>
        </div>
    </div>
    <!-- Footer-->
    <footer class="py-5 bg-dark">
        <div class="container"><p class="m-0 text-center text-white">Copyright &copy; Your Website 2022</p></div>
    </footer>
    <!-- Bootstrap core JS-->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    <!-- Core theme JS-->
    <script src="js/scripts.js"></script>
</body>
</html>
```

style="height: 500px;" 







```
curl -o /Users/jay/code/test.json -L "https://openapi.naver.com/v1/search/local.json?query=구로맛집&display=5&start=1&sort=random" \
    -H "X-Naver-Client-Id: " \
    -H "X-Naver-Client-Secret: " -v
```

```
curl -o /Users/jay/code/test.json -L "https://openapi.naver.com/v1/search/local.json?query=%EA%B5%AC%EB%A1%9C%EB%A7%9B%EC%A7%91&display=5&start=1&sort=random" \
    -H "X-Naver-Client-Id: " \
    -H "X-Naver-Client-Secret: " -v
```





%EA%B5%AC%EB%A1%9C%EB%A7%9B%EC%A7%91





```
{'lastBuildDate': 'Thu, 03 Nov 2022 16:05:44 +0900', 'total': 5, 'start': 1, 'display': 5, 
'items': [
{'title': '샤오카오', 'link': '', 'category': '중식>양꼬치', 'description': '', 'telephone': '', 'address': '서울특별시 구로구 구로동 1124-56', 'roadAddress': '서울특별시 구로구 디지털로32나길 17-6', 'mapx': '302946', 'mapy': '543027'}, {'title': '교대이층집 <b>구로</b>디지털단지점', 'link': 'http://sgfco.kr', 'category': '음식점>육류,고기요리', 'description': '', 'telephone': '', 'address': '서울특별시 구로구 구로동 1124-56', 'roadAddress': '서울특별시 구로구 디지털로32나길 17-6', 'mapx': '302943', 'mapy': '543024'}, {'title': '새벽집 양곱창', 'link': '', 'category': '한식>곱창,막창,양', 'description': '', 'telephone': '', 'address': '서울특별시 구로구 신도림동 694', 'roadAddress': '서울특별시 구로구 경인로61길 21', 'mapx': '301536', 'mapy': '545658'}, {'title': '새벽집소곱창', 'link': '', 'category': '한식>곱창,막창,양', 'description': '', 'telephone': '', 'address': '서울특별시 구로구 신도림동 419-4 상가B동 1층 101, 102호', 'roadAddress': '서울특별시 구로구 경인로63길 11 상가B동 1층 101, 102호', 'mapx': '301604', 'mapy': '545672'}, {'title': '최우영스시', 'link': 'https://www.instagram.com/cwyseafood', 'category': '일식>초밥,롤', 'description': '', 'telephone': '', 'address': '서울특별시 구로구 구로3동 212-8 B118호', 'roadAddress': '서울특별시 구로구 디지털로 288 B118호', 'mapx': '302511', 'mapy': '542972'}]}
```

https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20211028_108%2F1635420017030PjXR7_JPEG%2FJvmKu66r1x9YcZRMTOMW0ml6.jpg&type=f&size=680x360

https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20221014_169%2F1665706293463WPrI3_JPEG%2FDSC_0546.JPG&type=f&size=680x360
