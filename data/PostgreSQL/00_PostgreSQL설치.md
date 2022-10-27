# PostgreSQL 설치 및 설정

- PostgreSQL 엔진 설치
- pgAdmin 설치



## PostgreSQL 설치

데이터 저장, DB 구축, 쿼리 등에 사용하는 SQL 엔진

https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

비밀번호만 설정하고 나머지는 default로 모두 다운로드 받자. (14.5버전)



## pgAdmin

PostgreSQL에 연결해 사용하는 GUI 툴

https://www.pgadmin.org/download/

https://www.postgresql.org/ftp/pgadmin/pgadmin4/v6.13/macos/

dmg파일을 받고 기본으로 설치





## 환경변수 설정

```bash
> vim ~/.zshrc
```

환경변수 추가 해주기

```bash
export PATH="/Library/PostgreSQL/14/bin/:$PATH"
```





## 확인

- 버전확인

```bash
> psql --version
psql (PostgreSQL) 14.5
```



- 접속
    - 처음 설정한 계정(관리자) : postgres

```bash
> psql -U postgres
Password for user postgres:
psql (14.5)
Type "help" for help.

postgres=#
```



