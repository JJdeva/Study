# Git - git은 터뜨리며 배우는 것

### SCM & VCS

- Source Code Management(SCM) : 코드 관리 도구
- Version Control System(VCS) : 버전 관리 시스템
- 코드 관리 도구
-  how? **버전** 관리( **commit**, 해당 폴더의 특정 시점의 사진/스냅샷)



## `git`의 역할

1. 코드 관리 도구
2. 코드 저장 도구
3. 협업 도구
4. 배포 도구





### 명령어들

> git은 `폴더 단위`로 코드를 관리 한다. 

> git 저장소(repository) == git으로 관리되는 폴더

> git 저장소 상위 폴더에서 git을 시작하지 않는다.

### (1) git init

- git 저장소를 시작한다 == 현재 폴더를 git 저장소로 만든다. == git으로 관리되는 프로젝트 생성

```shell
$ git init
Initialized empty Git repository in C:/Users/JAY/git/.git/
```

- (master)라는 표시가 프롬프트에 뜬다.
- `.git`폴더가 생성된다.
  - `.git`폴더를 삭제하면 git 관리가 끝난다.



### (2) `git status`

- git의 현재상태를 알려준다.
- 최초 상태

```shell
$ touch a.txt
on branch master
   -> master라는 branch에 있다.
No commits yet
   -> commit(버전, 스냅샷) 아직 없다.
nothing to commit (create/copy files and use "git add" to track)
   -> commit 할게 없다. (파일 만들어서, git add해줘)
```

- 파일 생성 후 상태

```shell
$ git status
On branch master

No commits yet

Untracked files: (추적되지 않은 파일들)
  (use "git add <file>..." to include in what will be committed)
        a.txt <- "git add 파일명"을 사용하세요. 포함하기 위해서.

nothing added to commit but untracked files present (use "git add" to track)
```



### (3) `git add [파일명/폴더명]`

- 스냅샷을 찍기(commit 하기, 버전생성을) 위해 파일을 추가

- git add 후, status

```shell
$ git add a.txt
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   a.txt
```



### (4) `git commit -m '커밋 메시지'`

- git 설치 후 최초로 commit을 하면,

```shell
*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"
-->> 이메일하고 이름을 넣어줘
to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'JAY@DESKTOP-VCQ555G.(none)')
```

- git 초기 설정 명령어 물어본다.
  - git config --global user.email "내 이메일주소"
  - git config --global user.name "내 이름"

- 이메일, 이름이 설정 되면 git commit 뭔가 새로운 창이 뜨는데, esc 연타하고 :q!누르면 나옴. 이거 쓸일은 당분간 없다. (들어가지 말자)

- git commit -m '메시지' 로 쓰자



### (5) `git log`

현재까지의 버전(commit,스냅샷)을 모두 출력

- `git log` : 전체를 다 보여줌 

- `git log --oneline` : 한줄로 표시
- `git log --oneline -숫자` : 특정 개수만 출력 (최근거에서 숫자개만큼)



### (6) `git checkout [커밋해시]`

- 특정 시점의 커밋을 체크
- 돌아가 보고 싶은 시기의 해시를 넣어서 git checkout 커밋해서 로 쓴다.

```sh
$ git checkout 720eec96b
Note: switching to '720eec96b'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 720eec9 First commit
```

- 돌아갈 땐 git checkout master



## 코드 저장 도구

집, 캠퍼스 동시 작업시, 

### (1) github 원격 저장소 생성

`'https://github.com/[유저네임]/[원격저장소이름].git'`



### (2) `git remote`

현재 등록된 원격저장소들의 목록



### (3) `git remote add[저장소이름][저장소주소url]`

- 새로운 원격저장소를 추가

- 첫번째(원본) 원격저장소의 이름은 `origin`으로 하는게 관례(convention)
- git remote -v (저장소 위치표시)



### (4) `git push [저장소이름][브랜치이름]`

- origin
- git push origin master














