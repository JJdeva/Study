# 연습

## 문제 - 커뮤니티 게시판 데이터베이스 만들기

### 1. 데이터베이스 만들기

- db명 : community_board



### 2. 유저. 테이블 만들기

- 유저 정보를 저장할 테이블 생성 (익명X)
- 테이블명 : users
- 컬럼
    1. user_pk : INTEGER
    2. user_id : VARCHAR(80)
    3. user_pw : VARCHAR(12)
    4. register_date : DATE
- 설명
    - user_pk : 유저 정보 수정 및 삭제할 때 쓸 pk
    - user_id : 사용자 계정 아이디
    - user_pw : 사용자 계정 비밀번호
    - register_date : 회원가입 날짜



### 3. 게시판 테이블 만들기

- 테이블명 : board
- 컬럼
    1. board_pk : INTEGER
    2. board_user : INTEGER
    3. register_date : DATE
    4. title : VARCHAR(30)
    5. description : VARCHAR(3000)
    6. likes : INTEGER
    7. image_name : VARCHAR(50)
- 설명
    - board_pk : 게시판 pk
    - board_user : 게시판 작성자. user_pk가 들어감
    - register_date : 게시판이 등록된 날짜
    - title : 게시판의 제목
    - description : 게시판의 내용
    - likes : 게시판 추천 수
    - image_name : 첨부 이미지 불러올 파일명



### 4. 데이터 추가

1. user테이블

    | user_pk | user_id   | user_pw | register_date |
    | ------- | --------- | ------- | ------------- |
    | 1       | Carveinus | car1234 | 2020-04-23    |
    | 2       | Jenna     | kk3375  | 2020-07-12    |
    | 3       | Wlfur     | fur0022 | 2020-08-31    |

    - (1, 'Carveinus', 'car1234', '2020-04-23')
    - (2, 'Jenna', 'kk3375', '2020-07-12')
    - (3, 'Wlfur', 'fur0022', '2020-08-31')

2. board테이블

    | board_pk | board_user | register_date | title                  | description                                                  | likes | image_name  |
    | -------- | ---------- | ------------- | ---------------------- | ------------------------------------------------------------ | ----- | ----------- |
    | 1        | 1          | 2020-05-02    | Developer's essay      | Perhaps the reason we develop is because of the sense of accomplishment when we create something useful |       |             |
    | 2        | 3          | 2020-09-28    | Why the earth is round | I took a picture myself from space and saw that the earth is round |       | er.png      |
    | 3        | 2          | 2020-07-13    | Coffee time            | I had a vanilla latte this afternoon at the blue signboard cafe on the boulevard. |       | coffee.jpeg |
    | 4        | 2          | 2020-08-14    | Chicken is inefficient | This is because fried chicken is more expensive than other chicken dishes. |       |             |
    | 5        | 1          | 2020-06-22    | When bothering         | Let's get someone else to work.                              |       |             |

    

### 5. 한 페이지에 등록날짜를 내림차순으로 정렬해 최근 3개 게시글 조회

- 게시글 제목과 내용만 출력

    

### 6. 유저의 비밀번호 변경하기

- Carveinus 유저의 비밀번호를 car4321로 변경하자



### 7. 신고당한 게시판 삭제

- When bothering 게시글이 신고당했다고 가정하고 삭제해보자.





---

## 풀이

### 1번

- 코드

```postgresql
CREATE DATABASE community_board;
```

- 결과

```
CREATE DATABASE
```



### 2번

- 코드

```postgresql
CREATE TABLE users (
    user_pk INTEGER PRIMARY KEY NOT NULL,
    user_id VARCHAR(80),
    user_pw VARCHAR(12),
    register_date DATE
);
```





### 3번

- 코드

```postgresql
CREATE TABLE board (
	board_pk INTEGER,
    board_user INTEGER,
    register_date DATE,
    title VARCHAR(30),
    description VARCHAR(3000),
    likes INTEGER,
    image_name VARCHAR(50)
);
```





### 4번

- users에 데이터 추가

```postgresql
INSERT INTO users VALUES
(1, 'Carveinus', 'car1234', '2020-04-23'),
(2, 'Jenna', 'kk3375', '2020-07-12'),
(3, 'Wlfur', 'fur0022', '2020-08-31');
```

- board에 데이터 추가

```postgresql
INSERT INTO board VALUES
(1, 1, '2020-05-02', 'Developer''s essay', 'Perhaps the reason we develop is because of the sense of accomplishment when we create something useful', , ''),
(2, 3, '2020-09-28', 'Why the earth is round', 'I took a picture myself from space and saw that the earth is round', , 'er.png'),
(3, 2, '2020-07-13','Coffee time', 'I had a vanilla latte this afternoon at the blue signboard cafe on the boulevard.', , 'coffee.jpeg'),
(4, 2, '2020-08-14', 'Chicken is inefficient', 'This is because fried chicken is more expensive than other chicken dishes.', , ''),
(5, 1, '2020-06-22', 'When bothering', 'Let''s get someone else to work.', ,'');
```



### 5번

```postgresql
SELECT title, descrition FROM board
ORDER BY register_date DESC
LIMIT 3;
```

```

```



### 6번

```postgresql
UPDATE 	users
	SET user_pw = 'car4321'
	WHERE user_id = 'Carveinus'
RETURNING *;
```

```

```



### 7번

```postgresql
DELETE FROM board
WHERE title = 'When bothering';
SELECT * FROM board;
```

```
```

















