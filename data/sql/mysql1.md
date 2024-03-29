# 내용

MySQL 서버의 시스템 설정

- 설정에 따라 쿼리에 어떤 영향을 주는지?
- 설정에 따라 대소문자 구분, 문자열 표기 방법 등과 같은 SQL 작성 규칙 달라진다.

MySQL의 예약어와 예약어를 사용할 때 주의해야 할 사항



## sql_mode

sql_mode : MySQL 서버의 시스템 설정 (여러 개의 설정 값들이 동시 설정될 수 있음)

SQL 작성 결과에 영향을 미치는 설정값은 뭐가 있을까?



sql_mode를 설정할 때는 구분자(`,` 콤마)를 이용해 여러개의 키워드를 동시 설정할 수 있음

설정값(시스템 변수)의 종류

- SQL 쿼리 작성 규칙
- 서버 내부적으로 데이터 타입 변환
- 기본값 제어 등

일단 데이터베이스를 만들고 테이블을 만들어 데이터를 저장하기 시작했다면 가능한 한 sql_mode 시스템 변수 내용을 변경하지 않는게 좋다.

또한 같은 복제 그룹에 속한 모든 MySQL 서버들은 동일한 sql_mode 시스템 변수를 유지하는게 좋다.

sql_mode 시스템 변수를 변경할 땐 변경 후 어떤 변화가 생기고 어떤 문제가 터질까 생각하고 바꿔야 한다.



MySQL 서버에 대해 잘 모를 땐 그냥 기본 설정값을 쓰자. (sql_mode 시스템 변수 변경 X)

MySQL 8.0의 sql_mode 기본 값들

- `ONLY_FULL_GROUP_BY`
- `STRICT_TRANS_TABLES`
- `NO_ZERO_IN_DATE`
- `NO_ZERO_DATE`
- `ERROR_FOR_DIVISION_BY_ZERO`
- `NO_ENGINE_SUBSTITUTION`



몇가지 시스템변수 (page 4)

| 시스템 변수                                | 내용                                                         |
| ------------------------------------------ | ------------------------------------------------------------ |
| STRICT_ALL_TABLES<br />STRICT_TRANS_TABLES | MySQL 서버에서 INSERT나 UPDATE 문장으로 데이터를 변경하는 경우 컬럼의 타입과 저장되는 값의 타입이 다를 때 자동으로 타입 변경을 수행한다.<br />이때 타입이 적절히 변환되기 어렵거나 컬럼에 저장될 값이 없거나 값의 길이가 컬럼의 최대 길이보다 큰 경우 MySQL 서버가 INSERT나 UPDATE 문을 계속 실행할지, 아니면 에러를 낼지 결정한다.<br />- TRANS : transaction의 약어로 InnoDB같은 트랜잭션을 지원하는 스토리지 엔진에만 엄격한 모드를 적용<br />- ALL : 트랜잭션 지원 여부와 무관하게 모든 스토리지 엔진에 대해 엄격한 모드를 적용<br />두 옵션은 원하지 않는 값으로 자동 변환을 유발 시킬 수 있으므로 MySQL 서버를 서비스에 적용하기 전에 반드시 활성화할 것을 권장 |
| ANSI_QUOTES                                | MySQL에서는 문자열을 표현할 때 `' '`, `" "`를 동시에 사용할 수 있다.<br />다른 DBMS에서는 문자열은 `' '`를, 컬럼명/테이블명과 같은 식별자를 구분할 때 `" "`를 사용함<br />ANSI_QUOTES를 설정하면 문자열에는 싱글쿼터만 쓸 수 있음 |
| ONLY_FULL_GROUP_BY                         |                                                              |
| PIPE_AS_CONCAT                             |                                                              |
| PAD_CHAR_TO_FULL_LENGTH                    |                                                              |
| NO_BACKSLASH_ESCAPES                       |                                                              |
| IGNORE_SPACE                               |                                                              |
| REAL_AS_FLOAT                              |                                                              |
| NO_ZERO_IN_DATE<br />NO_ZERO_DATE          |                                                              |
| ANSI                                       |                                                              |
| TRADITIONAL                                |                                                              |





## 영문 대소문자 구분

mysql 서버는 설치 운영체제에 따라 대소문자를 구분한다.
이는 db나 테이블이 디스크의 디렉토리나 파일로 매핑되기 때문이다.

윈도우는 대소문자를 구분하지 않지만 유닉스/리눅스 시스템은 대소문자를 구분한다. 그렇기에 호환성 문제가 날 수도 있다.

`lower_case_table_names`시스템 변수

설정값

- 0 : 기본값 / 대소문자 구분 저장 / 대소문자 구분
- 1 : 모두 소문자로 저장되게 하고 MySQL 서버가 대소문자를 구분하지 않게 해줌
- 2 : 윈도우, macOS에서 설정가능 / 저장은 대소문자 구분 / 쿼리에서 대소문자를 구분하지 않음

--> 그냥 모두 소문자로 통일해서 쓰는게 좋을 것 같다.





## MySQL 예약어

생성하는 db, table, 컬럼 이름을 예약어와 같은 키워드로 생성하면 SQL문에 작성할 때 그 이름을 `백틱`으로 감싸줘야 함.

구분하기 헷갈리고 가독성에도 안좋고하니 대도록 예약어는 쓰지말도록 하자.

근데 뭐가 예약어인지를 모를 때는 그냥 일단 테이블을 만들어 보고 예약어라는 에러 경고를 받아보면 알 수 있다.

테이블 생성이 실패하면 예약어는 `백틱`으로 감싸지 않고는 쓸 수 없다는 것을 의미한다.







## 리터럴 표기법

### 문자열

표준 SQL은 싱글 쿼터로 문자열을 표현한다.

- `SELECT * FROM emp_no WHERE dept_no='d001';`

MySQL은 싱글, 더블 모두 사용 가능하다. (혼란스러울 수도 있다)

- `SELECT * FROM emp_no WHERE dept_no='d001';`
- ``SELECT * FROM emp_no WHERE dept_no="d001";`

쿼테이션마크를 문자열 안에 포함하고자 할 때 표준 SQL은 `'`, `"`를 연속으로 사용(`''`, `""`)해서 표현할 수 있음

- `SELECT * FROM emp_no WHERE dept_no='d''001';` --> d'001
- `SELECT * FROM emp_no WHERE dept_no='d""001';`

MySQL에서는 위의 방법과 다음 2가지 방법을 더 쓸 수 있음

- `SELECT * FROM emp_no WHERE dept_no="d'001";`
- `SELECT * FROM emp_no WHERE dept_no='d"001';`



sql_mode에서 ANSI_QUOTES를 설정하면 더블쿼터를 문자열에 쓸 수 없음.
또한 식별자 키워드랑 겹쳐서 충돌나는 건 `백틱`이 아니라 `더블쿼터`를 써야함



### 숫자

숫자 값을 입력할 때는 쿼테이션마크 없이 숫자만 입력하면 된다.

<u>문자열 형태로 숫자로 입력해도 비교 대상이 숫자값이나 숫자 타입이면 자동으로 형변환(문자->숫자)을 해서 비교한다.</u>
비교할 때 문자보다 숫자가 우선시 되기때문에 문자를 숫자로 형변환한다.



성능 비교 예시

1. `SELECT * FROM test WHERE num_col='10001';`

2. `SELECT * FROM test WHERE str_col=10001;`

1번의 경우 비교 대상이 숫자면 '10001'을 숫자 10001로 변환해서 비교한다. (1번만 변환)
또한 비교대상이 문자열이면 그냥 비교한다.(0번만 변환)

2번의 경우 비교 대상이 숫자인 경우 그냥 비교한다.(0번만 변환)
비교 대상이 문자일 경우 비교 대상인 컬럼 전체를 문자열로 변환하면서 비교를 한다. 컬럼의 레코드가 10만개면 10만번 변환-비교가 일어나는 것이므로 성능에 큰 영향을 끼친다. (인덱스를 만들어놔도 소용없다.)
또, 비교 컬럼에서 숫자로 형변환이 불가능할 경우 에러로 정지될 수도 있다.



이러한 문제를 피하려면 숫자값은 숫자 필드 컬럼에만 저장해야 함. 주의하자.



### 날짜

날짜에 대한 데이터를 DBMS에 INSERT하려면 문자열을 DATE 타입으로 변환하는 코드가 필요함

MySQL에서는 형식에 맞는 날짜포맷으로 입력하면 자동으로 DATE나 DATETIME 값으로 변환

(STR_TO_DATE()같은 함수 필요 없음)

- `SELECT * FROM dept_emp WHERE from_date='2011-04-29';`
- `SELECT * FROM dept_emp WHERE from_date=STR_TO_DATE('2011-04-29', '%Y-%m-%d');`

<u>날짜 타입과 문자열을 비교할 때 MySQL은 문자열을 DATE타입으로 변환해서 비교함</u>



### 불리언

`BOOL` or `BOOLEAN` 타입이 존재

BOOL, BOOLEAN으로 타입지정을 해도 실제로는 TINYINT 타입으로 지정된다.

값으로는 TRUE, FALSE, 1, 0 사용

TRUE, FALSE로 값을 넣어도 MySQL은 TRUE=1, FALSE=0으로 저장한다.

프로그래밍에선 0은 false, 나머진 true인데 mysql에선 false는 무조건 0, true는 무조건 1로 매핑된다. (다른 숫자는 조회가 되지 않는다.)

```mysql
CREATE TABLE tb_boolean (
	bool_value BOOLEAN );
	
INSERT INTO tb_boolean VALUES (FALSE);
SELECT * FROM tb_boolean WHERE bool_value=FALSE;
SELECT * FROM tb_boolean WHERE bool_value=TRUE;
```



```mysql
CREATE TABLE bool_test (bool_value BOOLEAN);
INSERT INTO bool_test VALUES (FALSE), (TRUE), (true), (false), (0), (1), (3), (100);

SELECT * FROM tb_boolean WHERE bool_value IN (FALSE, TRUE);

-----
0
1
1
0
0
1
```

3, 100은 조회가 안된다.

불리언 타입을 꼭 사용하고 싶다면 ENUM 타입으로 관리하는 것이 명확하고 실수할 가능성을 줄여줄 수 있음





## 연산자

### 동등 비교 연산자

- `=`
- `<=>`

두 개의 연산자는 동등 비교 연산자다. 좌변과 우변이 같으면 true, 다르면 false다.

기본적으로 NULL은 연산하지 않는다.

차이점은 `<=>`은 NULL값도 비교 연산을 한다는 것. (<u>NULL-safe 비교 연산자</u>라고 부름)

```mysql
> SELECT 1=1, NULL=NULL, 1 = NULL;

+-----+-----------+----------+
| 1=1 | NULL=NULL | 1 = NULL |
+-----+-----------+----------+
|   1 |      NULL |     NULL |
+-----+-----------+----------+

> SELECT 1 <=> 1, NULL <=> NULL, 1 <=> NULL;

+---------+---------------+------------+
| 1 <=> 1 | NULL <=> NULL | 1 <=> NULL |
+---------+---------------+------------+
|       1 |             1 |          0 |
+---------+---------------+------------+
```

`NULL <=> NULL` : NULL은 NULL하고 같다라는 걸 의미





### 부정 비교 연산자

- `<>`
- `!=`

`같지 않다`라는 의미로 둘다 같은 연산 결과를 보여준다. 둘 중 어느것을 써도 상관없지만 가독성을 위해 한가지로 통일해서 쓰자.



### NOT 연산자

- `!`
- `NOT`

TRUE or FALSE를 반대로(부정) 만드는 연산자.

둘 중 어느것을 써도 상관없지만 부정을 할 때 결과를 명확히 모를 땐 쓰는것에 신중하자.





### AND(&&)와 OR(||) 연산자

- `AND` = `&&`
- `OR` = `||`

oracle에선 `||`을 문자열을 결합하는 연산자로 씀. MySQL에서 oracle처럼 쓰고자 하면 sql_mode에서 `PIPE_AS_CONCAT`을 설정해주면 된다. 이때 ||은 문자열 더하기로 쓰이지만 &&은 똑같이 쓸 수 있음

```mysql
> SET sql_mode='PIPES_AS_CONCAT';
```



AND와 OR 중 AND가 더 우선순위가 높다.
AND와 OR을 같이 쓰면 AND가 먼저 계산된다. 우선순위를 지정하고 싶다면 ()로 따로따로 묶어서 쓰자.



































172.25.250.0/24 - 120/65/30/30/10 (65때문에 할당 불가능)

172.25.250.0/25. 172.25.250.0 - 127.25.250.119

172.25.250.0/25. 172.25.250.120 - 172.25.250.184

172.25.250.0/27. 172.25.250.185 - 172.25.250.216

172.25.250.0/27. 172.25.250.217 - 172.25.250.248

172.25.250.0/28. 172.25.250.249 - 172.25.250.258



192.168.0.0/16 - 32700/8100/8100/8100/4000

192.168.0.0/16 192.168.0.0 - 192.168.128.59

192.168.0.0/19 192.168.128.60 - 192.168.158.254

192.168.0.0/19 192.168.158.255 - 192.168.199.194 

192.168.0.0/19 192.168.199.195 - 192.168.230.139

129.168.0.0/20 192.168.230.140 - 192.168.245.19





























