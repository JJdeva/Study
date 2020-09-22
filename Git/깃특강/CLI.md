# CLI - Command Line Interface



### `CLI` vs. `GUI`

- CLI : Command Line Interface (명령어)
- GUI : Graphic User Interface (그래픽)

- **(중요)** : CLI에서는 유저가 컴퓨터에게 끊임없이 명령을 해야함



#### 명령어

- $ git --version : 버전확인
- `pwd` : print working directory 현재 위치를 절대 경로로 표시
- `ls` : list 현재 폴더(디렉토리)의 내용물을 표시
  - `ls -a` : 숨김 파일도 표시

- `cd[폴더명/경로]` : change directory 폴더를 이동
  - `cd ..` : 상위폴더로 이동
  - `..` : 상위폴더
  - `.` : 현재 폴더
- `mkdir [폴더명]` : make directory 폴더를 생성
- `rm -r [폴더명]` : remove : 폴더를 제거
- `touch [파일명]` : 파일을 생성 예) touch a.txt
- `rm [파일명]` : 파일을 삭제
- `cat [파일명]`: 파일 내용을 출력

- `cp [파일명][경로명]` : 파일 복사붙여넣기 예) cp. a.txt git/
  - `cp` : copy 파일 또는 폴더(recursively, -r)를 이동

- `mv [파일명][경로명]` : 파일 또는 폴더를 이동

  - 예) mv b.txt .. : 상위폴더로 이동

  - 예) mv a.txt /c/Users/JAY/anaconda3/ 상위의 아나콘다 폴더로 이동(절대 경로)

    

