# psql

터미널에서 postgresql을 다뤄보자.



postgresql 데이터베이스 접속

```bash
> psql -U postgres
Password for user postgres:
psql (14.5)
Type "help" for help.

postgres=#
```

- psql : SQL Shell을 실행하는 명령어
- 옵션
    - -U : 로그인 계정 지정 (대문자로 써야함)



접속 후

```bash
postgres=#
```

여기서 postgres=#가 뜨고 여기서 커맨드를 입력할 수 있다.

postgres=#에서 <u>postgres는 사용자 계정이 아니다.</u> **postgres라는 데이터베이스명**을 의미한다.

처음 설치 후 접속시 postgres라는 데이터베이스로 접속되는 것이다.





help 명령어 : `\?`

```bash
postgres=#\?
General
  \copyright             show PostgreSQL usage and distribution terms
  \crosstabview [COLUMNS] execute query and display results in crosstab
  \errverbose            show most recent error message at maximum verbosity
  \g [(OPTIONS)] [FILE]  execute query (and send results to file or |pipe);
General
  \copyright             show PostgreSQL usage and distribution terms
  \crosstabview [COLUMNS] execute query and display results in crosstab
  \errverbose            show most recent error message at maximum verbosity
  \g [(OPTIONS)] [FILE]  execute query (and send results to file or |pipe);
                         \g with no arguments is equivalent to a semicolon
  \gdesc                 describe result of query, without executing it
  \gexec                 execute query, then execute each value in its result
  \gset [PREFIX]         execute query and store results in psql variables
  \gx [(OPTIONS)] [FILE] as \g, but forces expanded output mode
  \q                     quit psql
  \watch [SEC]           execute query every SEC seconds

Help
  \? [commands]          show help on backslash commands
  \? options             show help on psql command-line options
  \? variables           show help on special variables
  \h [NAME]              help on syntax of SQL commands, * for all commands

Query Buffer
  \e [FILE] [LINE]       edit the query buffer (or file) with external editor
  \ef [FUNCNAME [LINE]]  edit function definition with external editor
  \ev [VIEWNAME [LINE]]  edit view definition with external editor
  \p                     show the contents of the query buffer
  \r                     reset (clear) the query buffer
  \s [FILE]              display history or save it to file
  \w FILE                write query buffer to file

Input/Output
  \copy ...              perform SQL COPY with data stream to the client host
  \echo [-n] [STRING]    write string to standard output (-n for no newline)
  \i FILE                execute commands from file
  \ir FILE               as \i, but relative to location of current script
  \o [FILE]              send all query results to file or |pipe
  \qecho [-n] [STRING]   write string to \o output stream (-n for no newline)
  \warn [-n] [STRING]    write string to standard error (-n for no newline)

Conditional
  \if EXPR               begin conditional block
  \elif EXPR             alternative within current conditional block
  \else                  final alternative within current conditional block
  \endif                 end conditional block

Informational
  (options: S = show system objects, + = additional detail)
  \d[S+]                 list tables, views, and sequences
  \d[S+]  NAME           describe table, view, sequence, or index
  \da[S]  [PATTERN]      list aggregates
  \dA[+]  [PATTERN]      list access methods
  \dAc[+] [AMPTRN [TYPEPTRN]]  list operator classes
  \dAf[+] [AMPTRN [TYPEPTRN]]  list operator families
  \dAo[+] [AMPTRN [OPFPTRN]]   list operators of operator families
  \dAp[+] [AMPTRN [OPFPTRN]]   list support functions of operator families
  \db[+]  [PATTERN]      list tablespaces
  \dc[S+] [PATTERN]      list conversions
  \dC[+]  [PATTERN]      list casts
  \dd[S]  [PATTERN]      show object descriptions not displayed elsewhere
  \dD[S+] [PATTERN]      list domains
  \ddp    [PATTERN]      list default privileges
  \dE[S+] [PATTERN]      list foreign tables
  \des[+] [PATTERN]      list foreign servers
  \det[+] [PATTERN]      list foreign tables
  \deu[+] [PATTERN]      list user mappings
  \dew[+] [PATTERN]      list foreign-data wrappers
  \df[anptw][S+] [FUNCPTRN [TYPEPTRN ...]]
                         list [only agg/normal/procedure/trigger/window] functions
  \dF[+]  [PATTERN]      list text search configurations
  \dFd[+] [PATTERN]      list text search dictionaries
  \dFp[+] [PATTERN]      list text search parsers
  \dFt[+] [PATTERN]      list text search templates
  \dg[S+] [PATTERN]      list roles
  \di[S+] [PATTERN]      list indexes
  \dl                    list large objects, same as \lo_list
  \dL[S+] [PATTERN]      list procedural languages
  \dm[S+] [PATTERN]      list materialized views
  \dn[S+] [PATTERN]      list schemas
  \do[S+] [OPPTRN [TYPEPTRN [TYPEPTRN]]]
                         list operators
  \dO[S+] [PATTERN]      list collations
  \dp     [PATTERN]      list table, view, and sequence access privileges
  \dP[itn+] [PATTERN]    list [only index/table] partitioned relations [n=nested
]
  \drds [ROLEPTRN [DBPTRN]] list per-database role settings
  \dRp[+] [PATTERN]      list replication publications
  \dRs[+] [PATTERN]      list replication subscriptions
  \ds[S+] [PATTERN]      list sequences
  \dt[S+] [PATTERN]      list tables
  \dT[S+] [PATTERN]      list data types
  \du[S+] [PATTERN]      list roles
  \dv[S+] [PATTERN]      list views
  \dx[+]  [PATTERN]      list extensions
  \dX     [PATTERN]      list extended statistics
  \dy[+]  [PATTERN]      list event triggers
  \l[+]   [PATTERN]      list databases
  \sf[+]  FUNCNAME       show a function's definition
  \sv[+]  VIEWNAME       show a view's definition
  \z      [PATTERN]      same as \dp

Formatting
  \a                     toggle between unaligned and aligned output mode
  \C [STRING]            set table title, or unset if none
  \f [STRING]            show or set field separator for unaligned query output
  \H                     toggle HTML output mode (currently off)
  \pset [NAME [VALUE]]   set table output option
                         (border|columns|csv_fieldsep|expanded|fieldsep|
                         fieldsep_zero|footer|format|linestyle|null|
                         numericlocale|pager|pager_min_lines|recordsep|
                         recordsep_zero|tableattr|title|tuples_only|
                         unicode_border_linestyle|unicode_column_linestyle|
                         unicode_header_linestyle)
  \t [on|off]            show only rows (currently off)
  \T [STRING]            set HTML <table> tag attributes, or unset if none
  \x [on|off|auto]       toggle expanded output (currently off)

Connection
  \c[onnect] {[DBNAME|- USER|- HOST|- PORT|-] | conninfo}
                         connect to new database (currently "postgres")
  \conninfo              display information about current connection
  \encoding [ENCODING]   show or set client encoding
  \password [USERNAME]   securely change the password for a user

Operating System
  \cd [DIR]              change the current working directory
  \setenv NAME [VALUE]   set or unset environment variable
  \timing [on|off]       toggle timing of commands (currently off)
  \! [COMMAND]           execute command in shell or start interactive shell

Variables
  \prompt [TEXT] NAME    prompt user to set internal variable
  \set [NAME [VALUE]]    set internal variable, or list all if no parameters
  \unset NAME            unset (delete) internal variable

Large Objects
  \lo_export LOBOID FILE
  \lo_import FILE [COMMENT]
  \lo_list
  \lo_unlink LOBOID      large object operations
```

대부분 서버, 데이터베이스 관리에 쓰임



알아두면 좋은 명령어

| 명령어 | 설명                                   |
| ------ | -------------------------------------- |
| \q     | psql 종료                              |
| \l     | 데이터베이스 조회                      |
| \c     | 입력한 데이터베이스로 이동             |
| \e     | 외부편집기로 SQL 쿼리를 입력할 수 있음 |
| \dt    | 현재 데이터베이스에서 테이블을 확인    |





쿼리문 작성

- 쿼리를 치다 엔터를 누르더라도 계속 입력받음 (세미콜론`;`이 와야 쿼리문이 끝난것으로 인식)
- 보기좋은 쿼리문을 작성하자 (한줄로 쭉 쓰지말고)
    - 엔터로 줄 구분
    - 탭으로 들여쓰기

```bash
postgres=# CREATE TABLE develop_book (
postgres=# 	book_id INTEGER,
postgres=# 	date DATE,
postgres=# 	name VARCHAR(80)
postgres=#);
```



# 실습

온라인 서점 데이터베이스를 구축해보자.

```
└── book_store/       # 서점 데이터베이스
    ├── develop_book  # 자기계발 책 테이블
    ├── novel         # 소설 책 테이블
    └── economy       # 경제관련 책 테이블
```



## 데이터베이스 생성

- 데이터베이스 생성하기

```bash
postgres=# CREATE DATABASE book_store;
CREATE DATABASE
```

- 데이터베이스 조회


```bash
postgres=# \l
                             List of databases
    Name    |  Owner   | Encoding | Collate | Ctype |   Access privileges
------------+----------+----------+---------+-------+-----------------------
 book_store | postgres | UTF8     | C       | C     |
 postgres   | postgres | UTF8     | C       | C     |
 template0  | postgres | UTF8     | C       | C     | =c/postgres          +
            |          |          |         |       | postgres=CTc/postgres
 template1  | postgres | UTF8     | C       | C     | =c/postgres          +
            |          |          |         |       | postgres=CTc/postgres
(4 rows)
```

성공적으로 book_store가 만들어진 걸 볼 수 있다.

현재 postgres 데이터베이스로 접속중이다 ("postgres=#"로 표시됨)

만들어진 데이터베이스로 접속해보자.

- 데이터베이스 접속

```bash
postgres=# \c book_store
You are now connected to database "book_store" as user "postgres".
```

만든 book_store 데이터베이스로 접속이 되었다. 이제 터미널에 "book_store=#"으로 표시가 된다.

- 데이터베이스 삭제
    - 현재 접속중인 데이터베이스는 삭제할 수 없다.

```bash
DROP DATABASE 데이터베이스명;
```





## 테이블 생성

- 테이블 생성하기
    - 테이블명 : develop_book
    - 컬럼 - 데이터타입
        - book_id : 책을 찾기 쉽게 숫자로 만들 값 (자료형 : INTEGER)
        - date : 책이 등록된 날짜 (자료형 : DATE)
        - name : 책 이름 (자료형 : VARCHAR)

```bash
book_store=# CREATE TABLE develop_book (
book_store(# book_id INTEGER,
book_store(# date DATE,
book_store(# name VARCHAR(80));
CREATE TABLE
```

- 테이블 조회 : `\dt`

```bash
book_store=# \dt;
            List of relations
 Schema |     Name     | Type  |  Owner
--------+--------------+-------+----------
 public | develop_book | table | postgres
(1 row)
```

- 테이블 삭제

```bash
DROP TABLE 테이블명;
```





## 데이터 추가

- 테이블에 데이터 추가하기

1. 순서 지정안하고 데이터 추가

    - `INSERT INTO 테이블명 VALUES (값1, 값2, 값3, ...)`

    - 테이블을 만들 때 입력한 컬럼 순으로 테이블이 만들어진다. 그래서 데이터를 추가할 때도 컬럼순에 맞게 순서대로 입력해줘야함 (book_id, date, name 순)

    - 테이블 컬럼과 입력 데이터가 일대일로 대응되야 데이터 추가가 된다.

    - 각 입력 데이터는 컬럼에 지정한 데이터타입에 맞는 형식으로 넣어줘야 한다.


```bash
INSERT INTO develop_book VALUES(1, '2019-12-17', '맛있는 MongoDB');
```

2. 순서 지정하고 데이터 추가

    - `INSERT INTO 테이블명 (컬럼1, 컬럼2, 컬럼3, ...) VALUES (컬럼1에 넣은 값1, ...)`

    - 보통 컬럼이 많아지고 순서를 기억하지 못할 때, 특정 컬럼은 생략하고 싶을 때 이런 방식을 씀
    - 순서 지정안하고 데이터 추가와는 다르게 테이블에서 컬럼의 순서를 지정해서 값을 넣어줌
    - (book_id, date, name) ~ (3, '2022-01-03', 'HTML/CSS')의 순서가 각각 맞아야함

```bash
INSERT INTO develop_book (book_id, date, name) VALUES (3, '2020-01-03', 'HTML/CSS');
```

```bash
INSERT INTO develop_book (book_id, name) VALUES (3, 'HTML/CSS');
```

위의 경우도 가능은 한데 date에 null값 들어감

3. 데이터 한번에 추가하기
    - `INSERT INTO 테이블명 VALUES (컬럼1, 컬럼2, ...), (컬럼1, 컬럼2, ...), ... (컬럼1, 컬럼2, ...);` 

```postgresql
INSERT INTO develop_book VALUES
(1, '2019-12-17', '맛있는 MongoDB'),
(2, '2019-12-25', '''자바'''),
(3, '2020-01-03', 'HTML/CSS'),
(4, '2020-01-24', 'Python'),
(5, '2020-02-04', 'C언어'),
(6, '2020-02-15', 'C++언어'),
(7, '2020-03-10', 'mySQL'),
(8, '2020-04-01', 'Go언어'),
(9, '2020-04-07', 'PHP'),
(10, '2020-04-17', 'Ruby');
```





## 데이터 조회

- 모든 데이터 조회
    - `SELECT * FROM develop_book;`

```bash
book_store=# SELECT * FROM develop_book ;
 book_id |    date    |      name
---------+------------+----------------
       1 | 2019-12-17 | 맛있는 MongoDB
       2 | 2019-12-25 | '자바'
       3 | 2020-01-03 | HTML/CSS
       4 | 2020-01-24 | Python
       5 | 2020-02-04 | C언어
       6 | 2020-02-15 | C++언어
       7 | 2020-03-10 | mySQL
       8 | 2020-04-01 | Go언어
       9 | 2020-04-07 | PHP
      10 | 2020-04-17 | Ruby
(10 rows)
```

- 일부 데이터만 조회

```bash
book_store=# SELECT book_id, name FROM develop_book ;
 book_id |      name
---------+----------------
       1 | 맛있는 MongoDB
       2 | '자바'
       3 | HTML/CSS
       4 | Python
       5 | C언어
       6 | C++언어
       7 | mySQL
       8 | Go언어
       9 | PHP
      10 | Ruby
(10 rows)
```

- 데이터 선택 조회 명령어

| 명령어   | 설명                               |
| -------- | ---------------------------------- |
| LIMIT    | 반환하는 로우의 개수를 지정        |
| OFFSET   | 반환하는 로우의 시작시점을 지정    |
| ORDER BY | 반환하는 로우를 정렬할 때 사용     |
| WHERE    | 지정한 로우만 조회가 되도록 필터링 |

- LIMIT

```bash
book_store=# SELECT * FROM develop_book LIMIT 5;
 book_id |    date    |      name
---------+------------+----------------
       1 | 2019-12-17 | 맛있는 MongoDB
       2 | 2019-12-25 | '자바'
       3 | 2020-01-03 | HTML/CSS
       4 | 2020-01-24 | Python
       5 | 2020-02-04 | C언어
(5 rows)
```

- OFFSET

| offset | book_id | date       | name           |
| :----- | :------ | :--------- | :------------- |
| 0      | 1       | 2019-12-17 | 맛있는 MongoDB |
| 1      | 2       | 2019-12-25 | '자바'         |
| 2      | 3       | 2020-01-03 | HTML/CSS       |
| 3      | 4       | 2020-01-24 | Python         |
| 4      | 5       | 2020-02-04 | C언어          |
| 5      | 6       | 2020-02-15 | C++언어        |
| 6      | 7       | 2020-03-10 | mySQL          |
| 7      | 8       | 2020-04-01 | Go언어         |
| 8      | 9       | 2020-04-07 | PHP            |
| 9      | 10      | 2020-04-17 | Ruby           |

- offset을 지정해보자.
    - LIMIT 6 OFFSET 2; ----> offset이 2부터 6개 조회

```bash
book_store=# SELECT * FROM develop_book
book_store-# LIMIT 6
book_store-# OFFSET 2;
 book_id |    date    |   name
---------+------------+----------
       3 | 2020-01-03 | HTML/CSS
       4 | 2020-01-24 | Python
       5 | 2020-02-04 | C언어
       6 | 2020-02-15 | C++언어
       7 | 2020-03-10 | mySQL
       8 | 2020-04-01 | Go언어
(6 rows)
```

- ORDER BY
    - 조회할 데이터의 순서를 정렬하는 명령어
    - 정렬을 할 기준 컬럼을 지정해준다.
    - 기본이 ASC (오름차순 정렬)
    - DESC를 지정하면 내림차순으로 정렬
    - **문자열 정렬은 유니코드상의 순서로 정렬된다.**

```bash
book_store=# SELECT * FROM develop_book
book_store-# ORDER BY book_id;
 book_id |    date    |      name
---------+------------+----------------
       1 | 2019-12-17 | 맛있는 MongoDB
       2 | 2019-12-25 | '자바'
       3 | 2020-01-03 | HTML/CSS
       4 | 2020-01-24 | Python
       5 | 2020-02-04 | C언어
       6 | 2020-02-15 | C++언어
       7 | 2020-03-10 | mySQL
       8 | 2020-04-01 | Go언어
       9 | 2020-04-07 | PHP
      10 | 2020-04-17 | Ruby
(10 rows)
```
```bash
book_store=# SELECT * FROM develop_book
book_store-# ORDER BY book_id DESC;
 book_id |    date    |      name
---------+------------+----------------
      10 | 2020-04-17 | Ruby
       9 | 2020-04-07 | PHP
       8 | 2020-04-01 | Go언어
       7 | 2020-03-10 | mySQL
       6 | 2020-02-15 | C++언어
       5 | 2020-02-04 | C언어
       4 | 2020-01-24 | Python
       3 | 2020-01-03 | HTML/CSS
       2 | 2019-12-25 | '자바'
       1 | 2019-12-17 | 맛있는 MongoDB
(10 rows)
```

- ORDER BY에 컬럼을 숫자로 써도됨
    - `*`로 하면 테이블 정의한 컬럼 순서대로 1,2,3,...으로 감
    - 컬럼을 따로 지정해 SELECT하면 지정한 순서대로 1,2,3...감
- ORDER BY에 다중 컬럼을 지정해도 됨
    - 순서대로 정렬하는데 처음 컬럼으로 정렬을 하고 그걸 기준으로 다음 컬럼을 정렬함

```bash
book_store=# SELECT book_id, date, name FROM develop_book ORDER BY 3, 2;
 book_id |    date    |      name
---------+------------+----------------
       2 | 2019-12-25 | '자바'
       6 | 2020-02-15 | C++언어
       5 | 2020-02-04 | C언어
       8 | 2020-04-01 | Go언어
       3 | 2020-01-03 | HTML/CSS
       9 | 2020-04-07 | PHP
       4 | 2020-01-24 | Python
      10 | 2020-04-17 | Ruby
       7 | 2020-03-10 | mySQL
       1 | 2019-12-17 | 맛있는 MongoDB
(10 rows)
```
```bash
book_store=# SELECT * FROM develop_book ORDER BY 3;
 book_id |    date    |      name
---------+------------+----------------
       2 | 2019-12-25 | '자바'
       6 | 2020-02-15 | C++언어
       5 | 2020-02-04 | C언어
       8 | 2020-04-01 | Go언어
       3 | 2020-01-03 | HTML/CSS
       9 | 2020-04-07 | PHP
       4 | 2020-01-24 | Python
      10 | 2020-04-17 | Ruby
       7 | 2020-03-10 | mySQL
       1 | 2019-12-17 | 맛있는 MongoDB
(10 rows)
```
- WHERE
    - 특정 내용 필터링 기능
    - 비교연산자
        - = , <> , > , < , >= , <=
        - <> : 서로 다름

book_id가 1이 아닌 데이터 조회

```bash
book_store=# SELECT * FROM develop_book WHERE book_id <> 1;
 book_id |    date    |   name
---------+------------+----------
       2 | 2019-12-25 | '자바'
       3 | 2020-01-03 | HTML/CSS
       4 | 2020-01-24 | Python
       5 | 2020-02-04 | C언어
       6 | 2020-02-15 | C++언어
       7 | 2020-03-10 | mySQL
       8 | 2020-04-01 | Go언어
       9 | 2020-04-07 | PHP
      10 | 2020-04-17 | Ruby
(9 rows)
```
- 서브쿼리

    - 쿼리문안에 존재하는 쿼리문

    ```postgresql
    SELECT * FROM develop_book
    WHERE '2020-01-03' = (
    	SELECT date FROM develop_book
    	WHERE book_id = 3
    );
    ```

    develop_book테이블에서 book_id가 3인 날짜(date)를 가져와 '2020-01-03'이랑 같은 데이터를 조회
    (결과는 모두 참이므로 전체 데이터를 가져옴)



## 데이터 수정

- 선택한 컬럼 데이터 수정

    ```postgresql
    UPDATE 	테이블명
    	SET 컬럼명 = 바꿀 데이터 내용
    	WHERE 수정할 로우의 조건
    RETURNING *; -- 수정한 내용 바로 조회하기
    ```

- RETURNING은 필수는 아님.
    써주면 UPDATE된 레코드를 출력해줌
- 데이터를 수정하면 정렬이 깨질 수 있음
    <u>(append개념으로 뒤에 레코드가 추가되는 형태인가봄?)</u>



## 테이블 복사

- AS를 써서 테이블을 복사해보자.
    - <u>AS다음에 ()안써도 되나봄?</u>

```postgresql
CREATE TABLE develop_book2 AS
SELECT * FROM develop_book
ORDER BY book_id ASC;
```

기존에 만든 테이블은 업데이트를 하면서 정렬이 깨짐
원본은 지우고 복사한 테이블을 원본으로 바꾸자
(보통 이런 방식은 안씀/연습용)

```postgresql
DROP TABLE develop_book;
ALTER TABLE develop_book2 RENAME TO develop_book;
```





## 데이터 삭제

- WHERE를 써서 조건에 맞는 레코드 삭제

```postgresql
DELETE FROM develop_book WHERE book_id = 6;
```

- 모든 데이터 삭제 (where절 안쓰면 됨)
    - 삭제시 확인 꼭 할 것
    - 지우고나면 되돌릴 수 없다.

```postgresql
DELETE FROM develop_book;
```










# 메모

- 식별자
    - 데이터베이스 객체 만들 때는 소문자로 이름짓자.
    - 식별자 만들 때 '_'로 구분짓자. -> book_store

- clear
    - cli창 지우기 = `\! clear``
    - ``\!`은 운영체제에서 쓰는 명령어를 쓸 수 있게 해줌. 그냥 `\!`만 치면 나가짐...



- 쿼테이션 마크
    - 문자열은 싱글쿼테이션마크 `'`로 감싸줘야함
    - 더블쿼터로 둘러싼 문자열은 psql이 컬럼으로 인식함 (문자열로 인식안함)
    - 그럼 싱글쿼터를 문자열 안에서 쓰고 싶을 땐? `''` 싱글 쿼터 2개를 쓰면 한개의 문자 '로 인식한다.



# Reference

모두를 위한 PostgreSQL: 누구나 이해할 수 있는 오픈소스 데이터베이스 개발
