# vscode 설정

확장에서

- `Auto Rename Tag` 
- `Auto Close Tag`
- `CSS Peek`
- `Color Highlight`
- `Highlight Matching Tag`





# HTML

HTML : HyperText Markup Language

웹 프로그래밍에서 골격을 담당

태그는 꺽쇠 기호를 이용하여 정의 할수 있다. `<Tag></Tag>`

현재 html 버전은 5버전을 사용

html 코드는 브라우저에 따라 다르게 표시될 수 있음

마크업은 어디서 어디까지가 텍스트인지 혹은 이미지인지를 구분



태그를 사용할 때 들여쓰기를 사용함

들여쓰기는 몇칸을 써도 상관없음 (닫는 기호로 구분하기때문에)



# HTML 기본 구조

```html
<!DOCTYPE html>
<html lang="ko">
    <head>
        <meta charset="UTF-8">
    </head>
    <body>
        
    </body>
</html>
```

- `<!DOCTYPE html>` : HTML5를 사용한다는 것을 정의
- `<html></html>` 
    - 웹의 범위를 명시해주는 태그 (웹 문서의 시작과 끝)
    - 보통 `<html lang="ko"></html>`로 사용 언어를 표기해준다.
- `<head></head>`
    - 브라우저가 웹 문서를 해석하는데 필요한 정보를 입력
    - 설정과 디자인 부분을 불러오는 태그
- `<body></body>`
    - 실제 브라우저 화면에 나타내는 내용을 입력
    - 실제 화면에 뜨는 것은 body안에 작성





# 기본 Tag
## head

### meta

단일 태그 / 정보를 담는 태그

- `<meta charset="UTF-8">`
    - 문자 인코딩에 대한 정보를 담는 태그

- `<meta name="keywords" content="html의 구조">`
    - 웹 문서의 키워드
- `<meta name="description" content="html의 구조설명">`
    - 웹 문서의 설명
- `<meta name="author" content="jay">`
    - 웹 문서의 소유자나 제작자



### title

문서의 제목을 나타내는 태그

- `<title>내 문서</title>`



## body

### h

- 제목을 나타내는 태그
- h1, h2, h3, h4, h5 ,h6 까지 있으며 숫자가 커질수록 크기가 작아짐

### br

- 줄 바꿈 태그
- 단일 태그

### hr

- 줄을 만들어서 구분을 해주는 태그
- 단일 태그



### p

- 일반 문단을 나타내는 태그

### span

- 영역을 묶어주는 태그
- 스타일을 적용할 때 사용한다.
- 영역을 묶어 부분적으로 스타일을 입힐 때 주로 사용





# 시맨틱 태그

웹 사이트의 영역을 나눌 때 사용

왜 쓰는 걸까? 안써도 웹 문서를 만들 수 도 있다.

- 브라우저가 HTML 소스만 봐도 어느 부분이 제목이고, 메뉴이고, 본문인지를 쉽게 알 수 있음
- 영역을 명확하게 나누기 때문에 플랫폼별로 웹 문서를 표현하기 쉽다.
    (pc, 모바일 등등)
- 인터넷에서 웹 사이트를 검색할 때 필요한 내용을 정확히 찾을 수 있음

## header

- 페이지의 헤더 영역을 나타내는 태그

## nav

- 네이게이션 영역을 나타내는 태그
- 보통 다른 곳으로 연결하는 링크를 연결해둠
- 헤더, 푸터, 사이드 바 등 영향을 받지 않아 어디에 위치해도 상관없다.

## main

- 본문 영역을 나타내는 태그
- 웹 문서의 핵심이 되는 내용을 넣는다.

## article

독립된 컨텐츠를 담는 태그

## section

- 컨텐츠의 영역을 나타내는 태그

## aside

- 사이드 바 영역을 나타내는 태그

## footer

- 푸터 영역을 나타내는 태그
- 웹 문서 맨 아래에 영역을 만들어 사이트 제작 정보, 저작권 정보, 연락처 등의 정보를 담는다.
- 헤더, 섹션, 아티클 등 다양한 시맨틱 태그를 모두 사용할 수 있어 다양한 정보를 다양한 형식으로 넣을 수 있다.

## div

- div는 division의 약자로 소스들을 묶어 구분해주는 태그
- 시맥틱 태그가 나오기 전에 헤더, 네비게이션, 푸터 등을 구별할 때 많이 썼다.
- 지금도 많이 쓴다.
- 보통 css의 속성 class, id를 적용할 많이 사용한다.



# 텍스트 태그

## hn

- 제목을 나타내는 태그
- h1, h2, h3, h4, h5, h6까지 있으며 숫자가 커질수록 글자 크기가 점점 작아진다.

## p

- 텍스트 단락을 만들 때 사용하는 태그

## br

- 텍스트 단락에서 줄바꿈을 하기 위해 사용하는 태그다.
- 단일 태그

## blockquote

- 이용할 때 쓰는 태그
- 기본적으로 들여쓰기가 적용되며 다른 텍스트와 구분하여 적용된다.



## strong

- 텍스트를 굵게 표시할 때 사용
- b와 동일하게 보이나 텍스트를 강조(경고나 주의같이)할 때 사용

## b

- 텍스트를 굵게 표시할 때 사용
- strong과는 다르게 정말 글자 자체만 굵게 표시



## em

- 텍스트를 이테릭체로 표시할 때 사용
- strong과 같이 강조할 때 사용

## i

- 텍스트를 이테릭체로 표시할 때 사용
- b처럼 텍스트 자체만 이테릭으로 표현할 때 사용



# 목록 태그

## ol

- 순서가 있는 목록을 만드는 태그
- ordered list의 약자
- ol 하위에 li를 써서 목록을 만들어 준다.

```html
<ol>
    <li>항목1</li>
    <li>항목2</li>
</ol>
```

- 자동으로 목록 앞에 숫자나 문자를 써서 순서를 나타내준다
- 속성
    - type : 숫자나, 알파벳, 로마 숫자 중 선택이 가능
        - type = "1" : 숫자(default)
        - type = "a" : 영소문자
        - type = "A" : 영대문자
        - type = "i" : 로마 숫자 소문자
        - type = "I" : 로마 숫자 대문자
    - start
        - 선택된 타입중에 몇번째부터 시작해 순서를 메길지 결정
        - start = "3"이면 3번부터 리스트 시작
    - 예제
        - `<ol type="a" start="4"></ol>`
        - d부터 리스트가 만들어진다.





## ul

- 순서가 없는 목록을 만드는 태그
- unordered list의 약자
- ul 하위에 li를 써서 목록을 만들어 준다.

```html
<ul>
    <li>목록1</li>
    <li>목록2</li>
</ul>
```

- 결과 목록 앞에 나오는 원이나 사각형같은 그림을 불릿(builet)이라고 함





# 표 태그

## table

- 테이블을 만들기 위해 사용함
- tr과 td와 함께 쓴다.

## caption

표의 제목을 붙이고 싶을 때 사용

## tr

- 행을 만들어 주는 태그

## td

- 열을 만들어 주는 태그



2 by 3의 테이블을 만든다고 하면 다음과 같이 작성한다.

```html
<table>
    <tr>
    	<td>1행 1열</td>
        <td>1행 2열</td>
        <td>1행 3열</td>
    </tr>
    <tr>
    	<td>2행 1열</td>
        <td>2행 2열</td>
        <td>2행 3열</td>
    </tr>
</table>
```

## th

- 표의 제목 행에 셀을 만들 때 사용하는 태그
- td대신에 th를 넣으면 두껍게 표시되며 제목 셀이 된다.



## rowspan

- 행을 병합할 때 쓰는 속성
- 행끼리 합치는거라 세로모양으로 합쳐짐

## colspan

- 열을 병합할 때 쓰는 속성
- 열끼리 합치는거라 가로모양으로 합쳐짐

## colgroup

- 열 순서대로 그루핑해서 스타일을 먹일 수 있음
- col 태그와 함께 쓰임
- 3열짜리 테이블이면

```html
<table>
    <colgroup>
    	<col style="color:red;">
        <col>
        <col style="width:10px;"
    </colgroup>
</table>
```

- col이 3번나오는데 순서대로 1열, 2열, 3열로 스타일이 적용된다.
- 스타일적용을 안해줘도 `<col>`로 패스시켜줘야한다.



## table 구조 나누기

### thead

- 표의 제목

### tbody

- 표의 본문

### tfoot

- 표의 요약



# 이미지 태그

## img

- 이미지를 넣을 수 있게 해주는 태그
- `<img src="이미지경로" alt="이미지 대신 표시해줄 텍스트">`



## 이미지 속성

### width, height

- 이미지의 가로, 세로 크기를 지정할 수 있음
- `%` : 이미지 크기의 상대크기
- `px` : 픽셀의 절대크기



# 미디어 태그

웹 브라우저에서 지원하는 멀티미디어

- 비디오
    - mp4
    - webm
- 오디오
    - mp3
    - mp4, m4a



## object

- 오디오, 비디오, 자바 애플릿, pdf 등 다양한 멀티미디어 파일을 삽입할 때 사용
- `<object width="" height="" data=""></object>`



## embed

- 대부분 브라우저에서 사용할 수 있는 미디어 태그
- src속성을 이용해 데이터를 삽입
- 단일 태그
- `<embed src="파일경로" width="" height="">`



## audio, video

- `<audio src="오디오파일경로"></audio>`
- `<video src="비디오파일경로"></video>`
- width, height, controls 속성 사용 가능
    - controls를 써주면 사용자가 재생, 정지 등 컨트롤이 가능해짐



# 하이퍼링크

## a

- `<a href="링크">링크설명</a>`
- target 속성
    - 누르면 새탭에서 열게 해주는 옵션
    - `target="_blank"`로 지정하면 새탭에서 열림



## 앵커(anchor)

`<a href=""></a>`를 쓰는 건 같으나 id를 사용해서 같은 페이지에서 누를 시 해당 id로 이동하게 해주는 기능이다.

예를 보자.

```html
<div>
    <p id="mylist">
        mylist
    </p>
    <ul>
        <li><a href="#mylist1">목록1</a></li>
        <li><a href="#mylist2">목록2</a></li>
        <li><a href="#mylist3">목록3</a></li>
    </ul>
</div>

<div id="mylist1">
	<h1>목록1입니다.</h1>
    <p>1</p><p>1</p><p>1</p><p>1</p><p>1</p><p>1</p><p>1</p><p>1</p><p>1</p><p>1</p>
    <p>1</p><p>1</p><p>1</p><p>1</p><p>1</p><p>1</p><p>1</p><p>1</p><p>1</p><p>1</p>
    <p>1</p><p>1</p><p>1</p><p>1</p><p>1</p><p>1</p><p>1</p><p>1</p><p>1</p><p>1</p>
</div>
<div id="mylist2">
	<h1>목록2입니다.</h1>
    <p>2</p><p>2</p><p>2</p><p>2</p><p>2</p><p>2</p><p>2</p><p>2</p><p>2</p><p>2</p>
    <p>2</p><p>2</p><p>2</p><p>2</p><p>2</p><p>2</p><p>2</p><p>2</p><p>2</p><p>2</p>
    <p>2</p><p>2</p><p>2</p><p>2</p><p>2</p><p>2</p><p>2</p><p>2</p><p>2</p><p>2</p>    
</div>
<div id="mylist3">
	<h1>목록3입니다.</h1>
    <p>3</p><p>3</p><p>3</p><p>3</p><p>3</p><p>3</p><p>3</p><p>3</p><p>3</p><p>3</p>
    <p>3</p><p>3</p><p>3</p><p>3</p><p>3</p><p>3</p><p>3</p><p>3</p><p>3</p><p>3</p>
    <p>3</p><p>3</p><p>3</p><p>3</p><p>3</p><p>3</p><p>3</p><p>3</p><p>3</p><p>3</p>
</div>
<div>
	<a href="#mylist">목록으로 돌아가기</a>
</div>
```







# 폼 태그

## form

- 폼을 만드는 기본적인 태그
- 폼을 열고 안에 다양한 폼 요소를 넣어서 사용한다.
- 속성을 지정해서 사용한다

<table>
    <tr>
    	<th>종류</th>
        <th>설명</th>
    </tr>
    <tr>
		<td rowspan="3">method</td>
        <td>http mothod를 지정해준다.</td>
    </tr>
    <tr>
        <td>get<br>- 256~4096바이트까지 서버로 넘김<br>- 주소 표시줄에 사용자가 입력한 내용이 그대로 드러나는 단점 존재</td>
    </tr>
    <tr>
        <td>post<br>- 입력한 내용의 길이에 제한받지 않고 사용자가 입력한 내뇽도 드러나지 않음</td>
    </tr>
    <tr>
        <td>name</td>
        <td>js로 폼을 제어할 때 사용할 폼의 이름 지정</td>
    </tr>
    <tr>
        <td>action</td>
        <td>폼 내용을 처리해 줄 서버 프로그램 지정</td>
    </tr>
    <tr>
        <td>target</td>
        <td>action속성에서 지정한 js 파일을 현재 창이 아닌 다른 위치에서 열도록 해줌</td>
    </tr>
</table>

plus)

- autocomplete="on"
    - 자동완성 지원
- autocomplete="off"
    - 자동완성 X



예시)

```html
<form action="search.php" method="post">
    <input type="text" title="검색">
    <input type="submit" value="검색">
</form>
```





## fieldset, legend

폼태그 안에 쓰는 태그로 한개의 폼에 여러개의 정보를 입력받을 때 쓴다.

```html
<form action="">
    <fieldset>
        <legend>
            상품 선택
        </legend>
    </fieldset>
    <fieldset>
        <legend>
            배송 정보
        </legend>
    </fieldset>
</form>
```



## label

폼 요소에 라벨을 붙이는 레이블태그

보통 input태그와 함께 쓰임

1. 태그 안에 폼 요소를 넣는 것

```html
<label>아이디(6자 이상)<input type="text"></label>
```



2. for 속성과 폼 요소의 id 속성을 이용해 서로 연결해 사용
    - 단점. css스타일이 적용이 안된다.

```html
<label for="id명">레이블명<input id="id명"></label>
```



css를 적용하기 위해 이렇게 따로 분리해서 쓴다. 서로 분리하고 id를 사용해 연결해주는 방식

```html
<label for="user_id">아이디(6자 이상)</label>
<input type="test" id="user_id">
```



## input

다양한 입력값을 받을 수 있는 태그

입력 형태를 지정할 때 다양한 type속성을 함께 사용한다.

| 종류           | 설명                                                         |
| -------------- | ------------------------------------------------------------ |
| text           | 한 줄짜리 텍스트를 입력할 수 있는 텍스트 박스를 넣음         |
| password       | 비밀번호 입력할 수 있는 필드 넣음                            |
| search         | 검색할 때 입력하는 필드 넣음                                 |
| url            | URL 주소를 입력할 수 있는 필드 넣음                          |
| email          | 이메일 주소를 입력할 수 있는 필드 넣음                       |
| tel            | 전화 번호를 입력할 수 있는 필드 넣음                         |
| checkbox       | 주어진 여러 항목에서 2개 이상 선택할 수 있는 체크 박스 넣음  |
| radio          | 주어진 여러 항목에서 1개만 선택할 수 있는 라디오 버튼 넣음   |
| number         | 숫자를 조절할 수 있는 스핀 박스 넣음                         |
| range          | 숫자를 조절할 수 있는 슬라이드 막대 넣음                     |
| date           | 사용자 지역을 기준으로 날짜(연,월,일)을 넣음                 |
| month          | 사용자 지역을 기준으로 날짜(연,월)을 넣음                    |
| week           | 사용자 지역을 기준으로 날짜(연,주)를 넣음                    |
| time           | 사용자 지역을 기준으로 (시,분,초,분할 초)을 넣음             |
| datetime       | 국제 표준시(UTC)로 설정된 날짜와 시간(연,월,일,시,분,초,분할초)을 넣음 |
| datetime-local | 사용자가 있는 지역을 기준으로 날짜와 시간(연,월,일,시,분,초,분할초)를 넣음 |
| submit         | 전송 버튼을 넣음                                             |
| reset          | 리셋 버튼을 넣음                                             |
| image          | submit 버튼 대신 사용할 이미지를 넣음                        |
| button         | 일반 버튼 넣음                                               |
| file           | 파일을 첨부할 수 있는 버튼 넣음                              |
| hidden         | 사용자에게는 보이지 않지만 서버로 넘겨주는 값이 있는 필드를 만듦 |



### text, password

- text
    - 한줄 입력
- password
    - 비밀번호 입력하는데 `*`나 다른 걸로 표시해 비밀번호를 가려줌



- 속성
    - size
        - 화면에 몇 글자가 보이도록 지정
    - value
        - 텍스트 필드 요소가 화면에 보일 때 텍스트 필드 부분에 보여주는 내용
        - 비밀번호 필드에선 안씀
    - maxlength
        - 텍스트 필드와 비밀번호 필드에 입력할 수 있는 최대 문자 수

- 로그인 폼 예시

```html
<form>
    <fieldset>
        <label>아이디: <input type="text" id="user_id" size="10"></label>
        <label>비밀번호: <input type="password" id="user_pw" size="10"></label>
        <input type="submit" value="로그인">
    </fieldset>
</form>
```





# Dropdown

박스를 클릭하면 하위에 항목이 나오고 항목을 고를 수 있음



select 태그를 써준다.

```html
<form action="subject.php" method="post">
    <label for="subject">학과</label>
    <select id="subject">
        <option>컴퓨터공학과</option>
        <option>신소재공학과</option>
        <option>기계공학과</option>
        <option>화학공학과</option>
        <option>전자공학과</option>
    </select>
</form>
```



드랍다운 항목끼리도 그루핑이 가능

- optgroup 태그
- label 속성

```html
<form action="subject.php" method="post">
        <label for="subject">학과</label>
        <select id="subject">
            <optgroup label="공학계열">
                <option>컴퓨터공학과</option>
                <option>신소재공학과</option>
                <option>기계공학과</option>
                <option>화학공학과</option>
                <option>전자공학과</option>
            </optgroup>
            <optgroup label="입문계열">
                <option>영문학과</option>
                <option>문학과</option>
                <option>역사학과</option>
            </optgroup>
        </select>
    </form>
```



# 데이터 목록의 시작과 끝 표시

드랍다운과 비슷한 기능

일반적인 드랍다운은 내용만 표기

일반적인 드랍다운이 아닌 시작과 끝에 내용을 표기할 수 있음

- datalist 태그를 쓴다.
- option엔 value, label이 온다.



```html
<form action="subject.php" method="post">
        <label for="interest">관심항목</label>
        <input type="text" id="interest" list="english">
        <datalist id="english">
            <option value="grammar" label="문법"></option>
            <option value="voca" label="어휘"></option>
            <option value="speaking" label="회화"></option>
            <option value="listening" label="청취"></option>
            <option value="reading" label="독해"></option>
        </datalist>
        <button type="submit">선택완료</button>
    </form>
```



# textarea

- textarea 태그 사용
    - 태그 사이에 값을 넣으면 기본으로 출력되게 할 수 있음
- 속성
    - cols : 가로의 길이 / 길이를 벗어나면 다음 줄로 줄바꿈
    - rows : 세로의 길이 / 길이를 벗어날 경우 스크롤이 생김

```html
<textarea cols="10" rows="3"></textarea>
```

- 속성
    - readonly : 수정이 불가능한 textarea를 만든다.
