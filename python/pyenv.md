# pyenv



## pyenv 설치

Homebrew를 설치하고 pyenv로 가상환경을 만들어서 사용해보자.



우선 파이썬 버전 관리해주는 `pyenv`를 설치하자.

```bash
brew install pyenv
```



그리고 파이썬 가상 환경을 만들어주는 `pyenv-virtualenv`를 설치하자.

```bash
brew install pyenv-virtualenv
```



이제 터미널에서 설정을 해주자.

```bash
> echo $SHELL
/bin/zsh
> echo 'eval "$(pyenv init --path)"' >> ~/.zprofile
> echo 'eval "$(pyenv init -)"' >> ~/.zshrc
> echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc
```



설정 후 터미널을 종료시키고 다시 실행시킨다.



```bash
pyenv --version
```

여기서 우리가 설치한 pyenv 버전이 정상 출력하면 설치와 설정이 잘 된 것이다.





## pyenv 사용

### 파이썬 설치

```bash
pyenv install --list
```

설치가능한 파이썬 버전 리스트가 출력된다.



출력된 버전 중 설치하고자 하는 것을 골라 설치해준다.

```bash
pyenv install 3.8.13
```



설치한 파이썬 목록을 보려면

```bash
pyenv versions
```



### 가상환경 생성

위에서 우리가 쓸 파이썬을 설치를 했다. 이제 설치한 파이썬을 이용해 가상환경을 만들어보자.



사용하고자 하는 버전의 파이썬과 사용할 가상환경 이름을 써주자.

```bash
pyenv virtualenv 3.8.13 myenvs
```



만든 것을 삭제하려면

```bash
pyenv uninstall myenvs
```



다시 versions로 확인해보자.

```
  system
  3.7.13
* 3.8.13 (set by /Users/jay/.pyenv/version)
  3.8.13/envs/airflowEnv
  3.8.13/envs/djangoEnvs
  3.10.1
  airflowEnv
  djangoEnvs
```

`*`는 현재 적용되어있는 파이썬을 뜻한다.



### 전역/지역 설정

우선 글로벌부터 보자. 글로벌로 설정해두면 어디서 실행하든 글로벌 설정된 파이썬으로 실행된다.



글로벌 설정은

```bash
pyenv global 3.8.13
```



로컬은 지정한 디렉토리에서만 로컬지정 파이썬 환경을 사용하는 것

로컬 설정은 원하는 디렉토리로 이동 후

```bash
pyenv local djangoEnvs
```







