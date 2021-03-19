# Python 설치 & 환경

- 참고
```
$ : command 혹은 terminal에서 실행
>>> : python에서 실행
```
- code editor : [VScode](https://demun.github.io/vscode-tutorial/)
- 모듈, 패키지 : 다른 곳에서 사용할 수 있게 코드를 모아둔 파일
```
모듈을 사용하고 싶으면 
1. 모듈을 설치한다/모듈의 위치를 안다
2. 파이썬에서는 from, import라는 키워드로 모듈/함수를 불러올 수 있다

ex) sys 모듈의 전체 함수를 현재 환경에 가져온다
>>> import sys
>>> sys.ps1()
>>> sys.ps2()

ex) sys 모듈에서 ps1, ps2 함수만 현재 환경에 가져온다
>>> from sys import ps1, ps2
>>> ps1()
>>> ps2()
```

## Python Interpreter [설치](https://www.python.org/downloads/)
- python을 설치한다 = python interpreter를 설치한다
- 버전 확인
```
$ python --version
Python 3.9.1 
```
```
linux계열 환경에서는 python3으로 설치되었을 수 있다.
$ python3 --version
Python 3.9.1 

.bashrc에서 alias로 python 버전을 바꿀 수도 있다
$ vi ~/.bashrc 
alias python="python3"


현재 shell에 바로 적용하기
$ source .bashrc
```

- python이 설치된 위치 확인
```
$ python

Python 3.9.1 (default, Jan 14 2021, 06:05:11) 
[GCC 5.5.0] on linux
Type "help", "copyright", "credits" or "license" for more information.

>>> import sys
>>> print(sys.executable)
/usr/bin/python3
```

## [Python Interpreter](https://github.com/python/cpython)

0. Interpreter([인터프리터](https://ko.wikipedia.org/wiki/%EC%9D%B8%ED%84%B0%ED%94%84%EB%A6%AC%ED%84%B0))
```
프로그래밍 언어로 작성한 소스 코드를 바로 실행하는 컴퓨터 프로그램/환경
```
- 컴퓨터는 사람의 언어를 이해할 수 없는 기계
- 사람의 언어(명령)를 컴퓨터가 이해할 수 있게 번역해주는 프로그램.
- 인터프리터와 비교할 수 있는 단어는 컴파일러

1. python interpreter
```
Cpython(=default python interpreter), pypy
```

관련글
- 순한맛🐸 : 파이썬 인터프리터
    - https://wikidocs.net/54
    - https://cjh5414.github.io/about-python-and-how-python-works/

- 중간맛😲 : 인터프리터 vs 컴파일러
    - https://medium.com/@yeon22/term-compiler-vs-interpreter-2199abe0f01d
    - https://www.guru99.com/difference-compiler-vs-interpreter.html

- 매운맛🥵 : 인터프리터 동작 방식과 코드 살펴보기
    - https://tech.ssut.me/peephole-how-python-optimizes-bytecode/
    - https://realpython.com/cpython-source-code-guide/

## Python 가상 환경
0. 가상 환경이 필요한 이유

```
python 모듈 설치 패키지인 pip로 설치하면 전역에 설치된다
= 모든 위치에서 설치한 모듈을 사용할 수 있다
```
- 프로젝트가 하나, 혼자 개발한다면 문제가 발생하지 않는다
- 그렇지만 프로젝트가 많아지고 프로젝트마다 다른 환경에서 개발하고 싶을 때 문제가 생길 수 있다

```
예시)
A 프로젝트와 B 프로젝트를 진행할 때 다음과 같은 python, module 버전이 필요하다
```
| | A | B|
|---|---|---|
| python | 3.9 | 3.6 |
| django | 3.6 | 2,7 |

```
A 프로젝트를 먼저 진행하다가 B 프로젝트를 시작하게 되면 
- pip로 설치했을 때 : python, django 특정 버전을 콕 집어서 사용해야 함()

-> A와 B를 왔다갔다 할 때마다 버전 변경해야함
-> 짱 불편함!!!! 다른 방법은 없을까?
-> 가상 환경을 사용해보자!
```

1. 가상 환경
```
같은 컴퓨터에서 실행되는 다른 파이썬 프로그램의 동작에 영향을 주지 않으면서, 
파이썬 패키지를 설치하거나 업그레이드를 할 수 있는 격리된 실행 환경
```

2. 가상 환경 종류
```
venv, virtualenv, conda, pipenv
```

관련글
- 🐸 : 가상 환경 설치/사용법
    - https://windybay.net/post/13/


## [pipenv](https://github.com/pypa/pipenv) - [manage app dependency](https://packaging.python.org/tutorials/managing-dependencies/#managing-dependencies!)

0. pipenv를 사용하게 될 시점
```
가상 환경 A에 설치한 모듈들을 다른 컴퓨터에도 똑같은 환경에 설치하고 싶을 때
```

1. pipenv 설치
```
$ python -m pip install --user pipenv

python -m pip: python으로 pip 모듈을 실행한다

pip install --user pipenv: 현재 사용자 계정에만 pipenv를 설치한다
```

2. pipenv 다루기
> 1-a) pipenv --three : 가상 환경을 만들 때 python3 환경으로 설정 
>   - 내 컴퓨터에 설치된 python3 버전을 기준으로 설정됨
```
$ pipenv --three
Creating a virtualenv for this project...
Pipfile: /home/ubuntu/python-study/Pipfile
Using /home/ubuntu/.linuxbrew/bin/python3.9 (3.9.1) to create virtualenv...
⠸ Creating virtual environment...created virtual environment CPython3.9.1.final.0-64 in 768ms
  creator CPython3Posix(dest=/home/ubuntu/.local/share/virtualenvs/python-study-wFTYkrzK, clear=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/home/ubuntu/.local/share/virtualenv)
    added seed packages: pip==20.3.3, setuptools==51.1.2, wheel==0.36.2
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator

✔ Successfully created virtual environment! 
Virtualenv location: /home/ubuntu/.local/share/virtualenvs/python-study-wFTYkrzK
Creating a Pipfile for this project...
```
설정이 완료되면 현재 폴더에 Pipfile이 생성된다
> Pipfile 내용
```
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]

[dev-packages]

[requires]
python_version = "3.9"
```
> 1-b) pipenv --python 3.8 : python 특정 버전으로 가상 환경 설정
   
만약 python3.8이 설치되지 않았으면 아래와 같은 에러가 발생한다.
```
Warning: Python 3.8 was not found on your system...
Neither 'pyenv' nor 'asdf' could be found to install Python.
You can specify specific versions of Python with:
$ pipenv --python path/to/python
```
정상적으로 설치되면 Pipfile의 python version이 3.8로 되어있다.
```
python_version = "3.8"
```

> 2) pipenv shell : 현재 위치한 프로젝트의 가상 환경으로 접속
> - 괄호 안에 프로젝트 이름이 들어있으면 가상 환경에 있다는 뜻!
> - ex: (python-study)
> - 가상 환경 종료는 exit이라고 적거나 ctrl+d를 누른다
```
$ pipenv shell

Launching subshell in virtual environment...
~/python-study$  . /home/ubuntu/.local/share/virtualenvs/python-study-wFTYkrzK/bin/activate
(python-study) ~/python-study$
```

> 3) pipenv install Django==2.2.17 : 가상 환경에 Django 2.2.17 버전을 설치, 의존성 기록
> - 의존성 기록 = Pipfile에 Django 버전 기록
```
$ pipenv install Django==2.2.17

Installing Django==2.2.17...
Adding Django to Pipfile's [packages]...
✔ Installation Succeeded 
Pipfile.lock not found, creating...
Locking [dev-packages] dependencies...
Locking [packages] dependencies...
Building requirements...
Resolving dependencies...
✔ Success! 
Updated Pipfile.lock (accb5a)!
Installing dependencies from Pipfile.lock (accb5a)...
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 0/0 — 00:00:00
To activate this project's virtualenv, run "pipenv shell".
Alternatively, run a command inside the virtualenv with "pipenv run".
```
Pipfile은 다음과 같이 수정됨
```
[packages]
django = "==2.2.17"
```
   
Pipfile.lock : Django를 설치하기 전에 Django에서 필요로 하는 모듈 리스트와 버전을 적어 둔 파일