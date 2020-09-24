# Git 써보기

### repository와 commit

1. 레포지토리(repository)

   프로젝트 디렉토리의 초창기 모습부터 변화 모델까지 버전별 변경 사항에 대해 기록해 놓는 저장소

   커밋이 저장되는 곳

2. 커밋(commit)

   프로젝트 디렉토리의 특정 모습을 하나의 버전으로 남기는 행위 & 결과물

   커밋할때 레포지토리에 사진찍듯이 저장된다.

   

### repository 만들기

```shell
$ git init # 비어있는 레포지토리를 생성 / .git 디렉토리가 생김(이것이 레포지토리)
```



### 첫 commit 해보기

commit 하기전에 git에게 commit한 사람의 정보 알려주기

```shell
$ git config user.name "Jaejin An"
$ git config user.email "ec9303@naver.com"
```

commit 을 하면 유저 이름과 메일 주소도 함께 저장된다.

```shell
$ git commit -m "커밋 정보"
```

그전에 add를 해줘야함

```shell
$ git add [파일이름]
```



### Git의 3가지 작업 영역

1. working directory

   작업을 하는 프로젝트 디렉토리

2. staging area

   git add를 한 파일들이 존재하는 영역, 커밋시 staging area에 있는 파일들만 커밋에 반영

3. repository

   working directory의 변경 이력들이 저장되어 있는 영억, 커밋들이 저장되는 영역

- 요약

  working directory에서 뭔가 작업을 하고, 작업한 파일들을 **git add** 해주고, 커밋을 하면 staging area에 있던

  파일들의 모습이 마치 영화의 한 장면, 스냅샷(snapshot)처럼 이 repository에 저장되는 것



​	**모든 파일 한번에 add 해주기**

```shell
$ git add .
```



### Git이 보는 파일의 4가지 상태

Git 파일들은 2가지 상태를 가짐.

- Untracked 

  ​	: 한번도 git add 를 안해준 상태(변동사항이 추적 안됨)

- Tracked : git add를 해주고 변동사항이 추적되는 상태

  - staged 상태 : git add 상태
  - Unmodified 상태 : 변경사항 없는 상태
  - Modified 상태 : 변경되어 반영이 필요한 상태

![깃](C:\Users\ajj\Desktop\깃.PNG)

- Add the file : Untracked 상태의 파일을 처음으로 git add 해주면 staged가 됨
- Edit the file : 최신 커밋과 비교했을 때 차이가 없는 Unmodified 상태의 파일의 내용을 수정하면 Modified가 됨
- Stage the file : Modified 상태의 파일을 git add 해주면 staged가 됨
- Remove the file : 파일을 삭제하면 git에선 인식이 안됨
- Commit : staging area에 있는 파일들이 커밋에 반영되고, 최신 커밋과 차이가 사라지니 Unmodified 상태가 됨



### git add 취소하기

git add (staging area에 파일 추가)  < - >  git reset(staging area에서 파일 제거)

```shell
$ git reset [파일명]
```

다시 add 전으로 돌아감. git status했을 때 modified로 남아있음. 다시 clean으로 가려면 파일 변경사항을 없애주면 됨



### git의 커맨드를 알아보자

$ git help [커맨드 이름]

$ man git-[커맨드 이름]

알고 싶은 커맨드의 설명이 나옴. 

처음 화면으로 돌아가고 싶으면 q를 입력하자





### git 기초 커맨드 정리

```shell
$ git init
$ git config user.name "이름"
$ git config user.email "이메일주소"
$ git add [파일이름]
$ git add [디렉토리명/]
$ git add .
$ git reset [파일이름]
$ git status
$ git commit -m "커밋 메시지"
$ git help [커맨드 이름]
```

