# git이란?



git과 github의 차이





# git/github 소스 관리 흐름

크게 소스 관리는 2가지 경우로 나뉜다.

- 지역 저장소 -> github(원격 저장소)
- github(원격 저장소) -> 지역 저장소



## 지역 저장소에서 깃허브

- 새 프로젝트 생성(디렉토리)
- `git init`으로 해당 프로젝트를 `git local repository`로 지정
- 이때 `.git`이라는 지역 저장소 관리 디렉토리가 생성됨
- 파일을 수정하고 `git add` 명령어로 수정한 파일을 `staging area`로 옮기고
- `git commit`으로 `local repository`에 저장하게 된다.
- `git push`로 원격 저장소에 지역 저장소 변경사항을 반영한다.



## 깃허브에서 지역 저장소

- 원격 저장소의 프로젝트 전체를 `git clone`으로 지역 저장소에 내려받기
- 일부 변경 사항만 `git pull`로 내려받기



