# CSS

Cascading Style Sheet

HTML로 짜여진 웹 프로그램 내에서 같은 구조로 다른 스타일을 적용할 때 사용

http://www.csszengarden.com/



## 스타일 형식

선택자 -> 스타일 속성 -> 속성값



선택자란 태그, 클래스, 아이디 등을 뜻함

예시) `p {text-align: center;}`



스타일 속성을 두 개 이상 지정할 경우

`p {text-align: center; color : blue;}`



스타일을 표기하는 방법

- 깔끔하고 가독성을 위해서 

```css
p {
    text-align : center;
    color : blue;
}
```



내부 스타일 시트

- html 내부에 style태그로 직접 css 내용을 넣는 방식

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>CSS</title>
    <style>
        ul {
            color: blue;
            list-style-type: square;
        }
    </style>
</head>
<body>
    <h1>세계 3대 미항</h1>
    <ul>
        <li>시드니</li>
        <li>라우데자네이루</li>
        <li>나폴리</li>
    </ul>
</body>
</html>
```



외부 스타일 시트

- 외부에 따로 css파일을 만들고 link태그로 html에서 불러서 사용하는 방식
- 속성
    - href : css의 경로를 지정
    - rel : "stylesheet"라고 지정
    - type : "text/css"라고 지정

```css
ul {
    color: blue;
    list-style-type: square;
}
```

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>CSS</title>
    <!-- stylesheet 분리 -->
    <link rel="stylesheet" href="./css3.css" type="text/css">
</head>
<body>
    <h1>세계 3대 미항</h1>
    <ul>
        <li>시드니</li>
        <li>라우데자네이루</li>
        <li>나폴리</li>
    </ul>
</body>
</html>
```





## 인라인 스타일

태그 별로 스타일을 지정하면 범위가 넓어짐

간단하게 스타일 지정하고 싶은 경우 인라인 스타일 지정

태그 안에 style을 각각 지정

예시)

```html
<p style="color:red; text-align:center;">
    안녕하세요. 가운데 정렬입니다.
</p>
```









## 선택자 종류

- 전체 선택자

    - html 문서 내에서 전체에 스타일을 적용하고 싶은 경우 사용한다.
    - `* {속성: 속성값;}`

- 클래스 선택자

    - html내에서 특정 부분(태그)에 스타일을 적용시키고 싶을 때 사용
    - `class="className"` <-> `.className`으로 연결
    - `.`을 붙여준다.

- id 선택자

  - label - input, anchor 등
  - html 내에서 특정 부분(고유하게)에 스타일을 적용시키고 싶을 때 사용. 단, id는 유일한 값과 유일한 대상을 지정하자
  - 클래스에 비해 범위가 작게 만들기
  - `id="myid"` <-> `#myid`로 연결
  - `#`을 붙여준다.
  
- 그룹 선택자

    - html 내에서 같은 스타일을 적용하고 싶은 부분을 묶어서 사용하고 싶을 때
    - 태그, 클래스, 아이디들을 연속적으로 사용, `,`로 연결해준다.

    ```css
    h1, p, textarea {
        color: blue;
    }
    ```






## 캐스캐이딩

캐스캐이딩 : 위에서 아래로 흐른다라는 의미를 가짐

---> 위에서 아래로 우선 순위를 정하여 스타일을 적용스킨다는 의미





| 우선순위 | 선택자 종류 |
| ::: | :---------: |
| 1        |       인라인 스타일      |
| 2        |      id 선택자       |
| 3        |       클래스 선택자      |
| 4        |       태그 선택자      |
| 5        |       전체 선택자      |

예시)

```css
p {
    color: blue;
}
p {
    color: orange;
}
```

같은 p태그에서 어느 색이 선택될까? 더 뒤에 만들어진 orange가 적용된다.

근데 내가 blue컬러의 p태그를 지정하고 싶다면 important를 지정하면 된다.

```css
p {
    color: blue !important;
}
p {
    color: orange;
}
```

같은 선택자 우선순위에서 최우선 순위를 적용하려면 important를 지정하자





## 스타일 상속

- 상위 태그를 부모 요소
- 하위 태그를 자식 요소
- 부모 요소에 스타일을 지정하면 자식 요소에도 스타일이 지정된다.
- 글자색, 글꼴 등등은 상속이 가능하지만 <u>배경색은 상속이 불가</u>





## CSS 모듈

표준화 속성 : 모든 브라우저와 호환되는 스타일 속성

하지만, 모든 속성들이 표준화가 되어 있는 것은 아님

표준화되지 않은 속성들은 브라우저마다 동작할 수도 있고, 안 할 수도 있음 -> 브라우저를 직접 명시해서 동작을 수동으로 시킬 수 있음

(참고 : https://www.w3.org/style/CSS - STAN­DARDS & DRAFTS)

수동으로 동작시키려면 접두사가 필요함

- `-webkit-` : 웹 키트 기반 브라우저(e.g. chrome, safari)
- `-moz-` : 모질라 기반 브라우저(e.g. mozila, firefox)
- `-o-` : 오페라 기반 브라우저(e.g. opera)
- `-ms-` : 마이크로소프트 인터넷 익스플로러 (e.g. IE)

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>CSS</title>
    <style>
        .box {
            position: absolute;
            left: 50px;
            top: 70px;
            width: 100px;
            height: 60px;
            background: #ff0000;
            border: 2px solid green;
            text-align: center;
        }
        .box:hover {
            -webkit-transform: rotate(15deg);
            -moz-transform: rotate(15deg);
            -o-transform: rotate(15deg);
            -ms-transform: rotate(15deg);
            transform: rotate(15deg);
        }
    </style>
</head>
<body>
    <div class="box">
        Mouse Over
    </div>
</body>
</html>
```

javascript를 이용해 접두사를 한번에 적용 가능함 https://projects.verou.me/prefixfree/

`<script src="prefixfree.min.js"></script>` 적용





## font

`.ttf` 확장자는 무거움(웹사이트용으로는 부적절) -> `.eot` or `.woff` 확장자의 글꼴 파일을 사용하는 것을 권장

글꼴 파일 변환 시 라이센스 꼭 따져보고 작업해야한다.









## ;;





## 박스모델

박스 모델 2가지

- 블록 레벨 요소
    - 내용이 세로로 추가되는 요소
    - p, hn, ul, ol, div
- 인라인 레벨 요소
    - 내용이 가로로 추가되는 요소
    - img, span, input, textarea, label
