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



































