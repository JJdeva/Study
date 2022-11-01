# SQL이란

사용자가 데이터베이스에 접근하여 데이터를 다루기 위한 전용 언어

이를 구조화된 질의 언어(SQL, Structured Query Language)라 한다.

RDBMS에서 데이터베이스와 소통하기 위해 SQL을 사용한다.



## 특징

- 데이터 베이스와 소통
    - 데이터에 대한 쿼리
    - 데이터베이스의 데이터를 정의, 조작, 제어
- 비절차적 언어
    - 절차를 신경쓸 필요 없이 쿼리만 날리면 RDBMS가 알아서 처리해 값을 리턴함
- 테이블 기준으로 데이터를 처리 (레코드 기준이 아님)





## 표준 SQL

많은 종류의 RDBMS가 있다. Oracle, MySQL, MS server, Postgresql 등등

이 모든 RDBMS가 모두 서로 다른 언어를 쓰면 문제가 생길 것, 이러한 문제를 방지하기 위해 표준 SQL이란게 있다. (처음 ANSI에서 SQL-86, 최근엔 ISO에서 표준(SQL:2019)을 지정하고 있다고 함)

제품마다 조금씩은 다른 SQL 문법을 가지고 있지만 표준 SQL을 기본으로하기에 어느정도 호환된다.
(oracle, mysql은 표준을 잘 따르지 않는다고함...)



## SQL의 분류

RDBMS의 기능은 크게 데이터 정의, 조작, 제어 기능이다. 이러한 기능은 SQL을 통해 구현된다.



- 데이터 정의어 (DDL, Data Definition Language)
    - 데이터베이스 객체(테이블, 뷰, 인덱스, 함수 등)를 정의, 변경, 제거
    - 객체 관리에 사용하는 SQL을 DDL이라 함
    - CREATE, ALTER, DROP, RENAME, TRUNCATE 등
- 데이터 조작어 (DML, Data Manipulation Language)
    - 테이블 내의 데이터를 갱신, 삭제, 추가, 저장 등 데이터를 조작하는 SQL
    - SELECT, INSERT, DELETE, UPDATE 등
    - 트랜잭션이 발생하는 SQL도 DML이다.
- 데이터 제어어 (DCL, Data Control Language)
    - 데이터베이스 접근, 권한 부여하는 SQL
    - 데이터베이스의 데이터를 안전하게 보호하기 위해서다.
    - GRANT, REVOKE, DENY 등