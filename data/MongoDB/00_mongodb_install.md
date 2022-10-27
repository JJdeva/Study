# MongoDB 설치

MacOS m1 silicon 기준입니다.



homebrew필요

<a href="https://www.mongodb.com/docs/v5.0/tutorial/install-mongodb-on-os-x/">설치 공식 가이드 - MongoDB 5.0 Manual</a>

설치가이드가 자세하네.. 따라만하면 될듯

## 설치

1. homebrew MongoDB tap 추가

```bash
> brew tap mongodb/brew
```



2. homebrew 및 brew formulae 업데이트

```bash
> brew update
```



3. MongoDB 5.0 커뮤니티 에디션 다운로드

```bash
> brew install mongodb-community@5.0
```



### 정보

mongodb-community@5.0에 포함된 바이너리들

- `mongod` : server
- `mongos` : sharded cluster query router
- `mongosh` : mongodb shell



주요 파일 및 디렉토리

| file or directory | path                          |
| ----------------- | ----------------------------- |
| config file       | /opt/homebrew/etc/mongod.conf |
| log directory     | /opt/homebrew/var/log/mongodb |
| data directory    | /opt/homebrew/var/mongodb     |



## 서비스 시작

MongoDB를 실행하기 위해선 mongod 서버 서비스를 시작해 프로세스로 올려줘야 함



homebrew를 이용한 MacOS 자동 서비스 시작/종료

- 서비스 시작

```bash
> brew services start mongodb-community@5.0
```

- 서비스 종료

```bash
> brew services stop mongodb-community@5.0
```





conf 파일을 이용해 수동으로 서비스 시작/종료

- 백그라운드 프로세스로 시작

```bash
mongod --config /opt/homebrew/etc/mongod.conf --fork
```

- 종료
    - mongosh에서 mongod로 접속해 shutdown 입력





## 확인

- 서비스 확인

```bash
❯ brew services list

Name                  Status  User File
mongodb-community@5.0 started jay  ~/Library/LaunchAgents/homebrew.mxcl.mongodb-community@5.0.plist
```

- 수동 시작 시 확인 방법

```bash
> ps aux | grep -v grep | grep mongod
```



- 로그 확인

```bash
> sudo cat /opt/homebrew/var/log/mongodb/mongo.log
> sudo cat /opt/homebrew/var/log/mongodb/output.log
```
```bash
```



