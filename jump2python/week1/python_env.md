# ๐ธ Python ์ค์น & ํ๊ฒฝ

- ์ฐธ๊ณ 
```
$ : command ํน์ terminal์์ ์คํ
>>> : python์์ ์คํ
```
- code editor : [VScode](https://demun.github.io/vscode-tutorial/)
- ๋ชจ๋, ํจํค์ง : ๋ค๋ฅธ ๊ณณ์์ ์ฌ์ฉํ  ์ ์๊ฒ ์ฝ๋๋ฅผ ๋ชจ์๋ ํ์ผ
```
๋ชจ๋์ ์ฌ์ฉํ๊ณ  ์ถ์ผ๋ฉด 
1. ๋ชจ๋์ ์ค์นํ๋ค/๋ชจ๋์ ์์น๋ฅผ ์๋ค
2. ํ์ด์ฌ์์๋ from, import๋ผ๋ ํค์๋๋ก ๋ชจ๋/ํจ์๋ฅผ ๋ถ๋ฌ์ฌ ์ ์๋ค

ex) sys ๋ชจ๋์ ์ ์ฒด ํจ์๋ฅผ ํ์ฌ ํ๊ฒฝ์ ๊ฐ์ ธ์จ๋ค
>>> import sys
>>> sys.ps1()
>>> sys.ps2()

ex) sys ๋ชจ๋์์ ps1, ps2 ํจ์๋ง ํ์ฌ ํ๊ฒฝ์ ๊ฐ์ ธ์จ๋ค
>>> from sys import ps1, ps2
>>> ps1()
>>> ps2()
```

## ๐ธ Python Interpreter [์ค์น](https://www.python.org/downloads/)
- python์ ์ค์นํ๋ค = python interpreter๋ฅผ ์ค์นํ๋ค
- ๋ฒ์  ํ์ธ
```
$ python --version
Python 3.9.1 
```
```
linux๊ณ์ด ํ๊ฒฝ์์๋ python3์ผ๋ก ์ค์น๋์์ ์ ์๋ค.
$ python3 --version
Python 3.9.1 

.bashrc์์ alias๋ก python ๋ฒ์ ์ ๋ฐ๊ฟ ์๋ ์๋ค
$ vi ~/.bashrc 
alias python="python3"


ํ์ฌ shell์ ๋ฐ๋ก ์ ์ฉํ๊ธฐ
$ source .bashrc
```

- python์ด ์ค์น๋ ์์น ํ์ธ
```
$ python

Python 3.9.1 (default, Jan 14 2021, 06:05:11) 
[GCC 5.5.0] on linux
Type "help", "copyright", "credits" or "license" for more information.

>>> import sys
>>> print(sys.executable)
/usr/bin/python3
```

## ๐ฒ [Python Interpreter](https://github.com/python/cpython)

0. Interpreter([์ธํฐํ๋ฆฌํฐ](https://ko.wikipedia.org/wiki/%EC%9D%B8%ED%84%B0%ED%94%84%EB%A6%AC%ED%84%B0))
```
ํ๋ก๊ทธ๋๋ฐ ์ธ์ด๋ก ์์ฑํ ์์ค ์ฝ๋๋ฅผ ๋ฐ๋ก ์คํํ๋ ์ปดํจํฐ ํ๋ก๊ทธ๋จ/ํ๊ฒฝ
```
- ์ปดํจํฐ๋ ์ฌ๋์ ์ธ์ด๋ฅผ ์ดํดํ  ์ ์๋ ๊ธฐ๊ณ
- ์ฌ๋์ ์ธ์ด(๋ช๋ น)๋ฅผ ์ปดํจํฐ๊ฐ ์ดํดํ  ์ ์๊ฒ ๋ฒ์ญํด์ฃผ๋ ํ๋ก๊ทธ๋จ.
- ์ธํฐํ๋ฆฌํฐ์ ๋น๊ตํ  ์ ์๋ ๋จ์ด๋ ์ปดํ์ผ๋ฌ

1. python interpreter
```
Cpython(=default python interpreter), pypy
```

๊ด๋ จ๊ธ
- ์ํ๋ง๐ธ : ํ์ด์ฌ ์ธํฐํ๋ฆฌํฐ
    - https://wikidocs.net/54
    - https://cjh5414.github.io/about-python-and-how-python-works/

- ์ค๊ฐ๋ง๐ฒ : ์ธํฐํ๋ฆฌํฐ vs ์ปดํ์ผ๋ฌ
    - https://medium.com/@yeon22/term-compiler-vs-interpreter-2199abe0f01d
    - https://www.guru99.com/difference-compiler-vs-interpreter.html

- ๋งค์ด๋ง๐ฅต : ์ธํฐํ๋ฆฌํฐ ๋์ ๋ฐฉ์๊ณผ ์ฝ๋ ์ดํด๋ณด๊ธฐ
    - https://tech.ssut.me/peephole-how-python-optimizes-bytecode/
    - https://realpython.com/cpython-source-code-guide/

## ๐ฒ Python ๊ฐ์ ํ๊ฒฝ
0. ๊ฐ์ ํ๊ฒฝ์ด ํ์ํ ์ด์ 

```
python ๋ชจ๋ ์ค์น ํจํค์ง์ธ pip๋ก ์ค์นํ๋ฉด ์ ์ญ์ ์ค์น๋๋ค
= ๋ชจ๋  ์์น์์ ์ค์นํ ๋ชจ๋์ ์ฌ์ฉํ  ์ ์๋ค
```
- ํ๋ก์ ํธ๊ฐ ํ๋, ํผ์ ๊ฐ๋ฐํ๋ค๋ฉด ๋ฌธ์ ๊ฐ ๋ฐ์ํ์ง ์๋๋ค
- ๊ทธ๋ ์ง๋ง ํ๋ก์ ํธ๊ฐ ๋ง์์ง๊ณ  ํ๋ก์ ํธ๋ง๋ค ๋ค๋ฅธ ํ๊ฒฝ์์ ๊ฐ๋ฐํ๊ณ  ์ถ์ ๋ ๋ฌธ์ ๊ฐ ์๊ธธ ์ ์๋ค

```
์์)
A ํ๋ก์ ํธ์ B ํ๋ก์ ํธ๋ฅผ ์งํํ  ๋ ๋ค์๊ณผ ๊ฐ์ python, module ๋ฒ์ ์ด ํ์ํ๋ค
```
| | A | B|
|---|---|---|
| python | 3.9 | 3.6 |
| django | 3.6 | 2,7 |

```
A ํ๋ก์ ํธ๋ฅผ ๋จผ์  ์งํํ๋ค๊ฐ B ํ๋ก์ ํธ๋ฅผ ์์ํ๊ฒ ๋๋ฉด 
- pip๋ก ์ค์นํ์ ๋ : python, django ํน์  ๋ฒ์ ์ ์ฝ ์ง์ด์ ์ฌ์ฉํด์ผ ํจ()

-> A์ B๋ฅผ ์๋ค๊ฐ๋ค ํ  ๋๋ง๋ค ๋ฒ์  ๋ณ๊ฒฝํด์ผํจ
-> ์งฑ ๋ถํธํจ!!!! ๋ค๋ฅธ ๋ฐฉ๋ฒ์ ์์๊น?
-> ๊ฐ์ ํ๊ฒฝ์ ์ฌ์ฉํด๋ณด์!
```

1. ๊ฐ์ ํ๊ฒฝ
```
๊ฐ์ ์ปดํจํฐ์์ ์คํ๋๋ ๋ค๋ฅธ ํ์ด์ฌ ํ๋ก๊ทธ๋จ์ ๋์์ ์ํฅ์ ์ฃผ์ง ์์ผ๋ฉด์, 
ํ์ด์ฌ ํจํค์ง๋ฅผ ์ค์นํ๊ฑฐ๋ ์๊ทธ๋ ์ด๋๋ฅผ ํ  ์ ์๋ ๊ฒฉ๋ฆฌ๋ ์คํ ํ๊ฒฝ
```

2. ๊ฐ์ ํ๊ฒฝ ํด ์ข๋ฅ
```
venv, virtualenv, conda, pipenv
```

๊ด๋ จ๊ธ
- ๐ธ : ๊ฐ์ ํ๊ฒฝ ํด ์ค์น/์ฌ์ฉ๋ฒ
    - https://windybay.net/post/13/


## ๐ฒ [pipenv](https://github.com/pypa/pipenv) - [manage app dependency](https://packaging.python.org/tutorials/managing-dependencies/#managing-dependencies!)

0. pipenv๋ฅผ ์ฌ์ฉํ๊ฒ ๋  ์์ 
```
๊ฐ์ ํ๊ฒฝ A์ ์ค์นํ ๋ชจ๋๋ค์ ๋ค๋ฅธ ์ปดํจํฐ์๋ ๋๊ฐ์ ํ๊ฒฝ์ ์ค์นํ๊ณ  ์ถ์ ๋
```

1. pipenv ์ค์น
```
$ python -m pip install --user pipenv

python -m pip: python์ผ๋ก pip ๋ชจ๋์ ์คํํ๋ค

pip install --user pipenv: ํ์ฌ ์ฌ์ฉ์ ๊ณ์ ์๋ง pipenv๋ฅผ ์ค์นํ๋ค
```

2. pipenv ๋ค๋ฃจ๊ธฐ
> 1) pipenv --three : ๊ฐ์ ํ๊ฒฝ์ ๋ง๋ค ๋ python3 ํ๊ฒฝ์ผ๋ก ์ค์  
>   - ๋ด ์ปดํจํฐ์ ์ค์น๋ python3 ๋ฒ์ ์ ๊ธฐ์ค์ผ๋ก ์ค์ ๋จ
```
$ pipenv --three
Creating a virtualenv for this project...
Pipfile: /home/ubuntu/python-study/Pipfile
Using /home/ubuntu/.linuxbrew/bin/python3.9 (3.9.1) to create virtualenv...
โ ธ Creating virtual environment...created virtual environment CPython3.9.1.final.0-64 in 768ms
  creator CPython3Posix(dest=/home/ubuntu/.local/share/virtualenvs/python-study-wFTYkrzK, clear=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/home/ubuntu/.local/share/virtualenv)
    added seed packages: pip==20.3.3, setuptools==51.1.2, wheel==0.36.2
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator

โ Successfully created virtual environment! 
Virtualenv location: /home/ubuntu/.local/share/virtualenvs/python-study-wFTYkrzK
Creating a Pipfile for this project...
```
์ค์ ์ด ์๋ฃ๋๋ฉด ํ์ฌ ํด๋์ Pipfile์ด ์์ฑ๋๋ค
> Pipfile ๋ด์ฉ
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
> 2) pipenv --python 3.8 : python ํน์  ๋ฒ์ ์ผ๋ก ๊ฐ์ ํ๊ฒฝ ์ค์ 
   
๋ง์ฝ python3.8์ด ์ค์น๋์ง ์์์ผ๋ฉด ์๋์ ๊ฐ์ ์๋ฌ๊ฐ ๋ฐ์ํ๋ค.
```
Warning: Python 3.8 was not found on your system...
Neither 'pyenv' nor 'asdf' could be found to install Python.
You can specify specific versions of Python with:
$ pipenv --python path/to/python
```
์ ์์ ์ผ๋ก ์ค์น๋๋ฉด Pipfile์ python version์ด 3.8๋ก ๋์ด์๋ค.
```
python_version = "3.8"
```

> 3) pipenv shell : ํ์ฌ ์์นํ ํ๋ก์ ํธ์ ๊ฐ์ ํ๊ฒฝ์ผ๋ก ์ ์
> - ๊ดํธ ์์ ํ๋ก์ ํธ ์ด๋ฆ์ด ๋ค์ด์์ผ๋ฉด ๊ฐ์ ํ๊ฒฝ์ ์๋ค๋ ๋ป!
> - ex: (python-study)
> - ๊ฐ์ ํ๊ฒฝ ์ข๋ฃ๋ exit์ด๋ผ๊ณ  ์ ๊ฑฐ๋ ctrl+d๋ฅผ ๋๋ฅธ๋ค
```
$ pipenv shell

Launching subshell in virtual environment...
~/python-study$  . /home/ubuntu/.local/share/virtualenvs/python-study-wFTYkrzK/bin/activate
(python-study) ~/python-study$
```

> 4) pipenv install Django==2.2.17 : ๊ฐ์ ํ๊ฒฝ์ Django 2.2.17 ๋ฒ์ ์ ์ค์น, ์์กด์ฑ ๊ธฐ๋ก
> - ์์กด์ฑ ๊ธฐ๋ก = Pipfile์ Django ๋ฒ์  ๊ธฐ๋ก
```
$ pipenv install Django==2.2.17

Installing Django==2.2.17...
Adding Django to Pipfile's [packages]...
โ Installation Succeeded 
Pipfile.lock not found, creating...
Locking [dev-packages] dependencies...
Locking [packages] dependencies...
Building requirements...
Resolving dependencies...
โ Success! 
Updated Pipfile.lock (accb5a)!
Installing dependencies from Pipfile.lock (accb5a)...
  ๐   โโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโ 0/0 โ 00:00:00
To activate this project's virtualenv, run "pipenv shell".
Alternatively, run a command inside the virtualenv with "pipenv run".
```
Pipfile์ ๋ค์๊ณผ ๊ฐ์ด ์์ ๋จ
```
[packages]
django = "==2.2.17"
```
   
Pipfile.lock : Django๋ฅผ ์ค์นํ๊ธฐ ์ ์ Django์์ ํ์๋ก ํ๋ ๋ชจ๋ ๋ฆฌ์คํธ์ ๋ฒ์ ์ ์ ์ด ๋ ํ์ผ

> 5) pipenv --rm : ํ์ฌ ํด๋์์ ์์ฑ๋ ๊ฐ์ ํ๊ฒฝ ์ญ์ 
> - ์ญ์ ๊ฐ ํ์ํ  ๋ : ํ๋ก์ ํธ ํด๋ ์ด๋ฆ์ ๋ฐ๊พธ๊ฑฐ๋ ์์น๋ฅผ ๋ณ๊ฒฝํ  ๋
> - ๋ด ๊ฒฝ์ฐ, python-study ์์น์ ๊ฐ์ํ๊ฒฝ์ ๋ง๋๋ ๊ฒ์ด ์๋๋ผ
>   
>   python-study ๋ด๋ถ week_one ํด๋์ ๊ฐ์ํ๊ฒฝ์ ๋ง๋ค๊ณ  ์ถ์ด์ ๊ฐ์ ํ๊ฒฝ ์ญ์ ๊ฐ ํ์ํ๋ค
> - Pipfile์ ์ด๋ฏธ ์์ผ๋ week_one์ผ๋ก ์ด๋์์ผ์ pipenv install๋ง ํด์ฃผ๋ฉด 
>   
>   ๊ฐ์ ํ๊ฒฝ์ด ๋ค์ ์์ฑ๋๋ค
```
$ pipenv --rm
Removing virtualenv (/home/ubuntu/.local/share/virtualenvs/python-study-wFTYkrzK)...

$ mv Pipfile ./jump2python/week_one
$ pipenv install
```

