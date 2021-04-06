# 알게 된 것

### 다른 곳에 있는 모듈을 추가할 때 sys.path.append를 사용한다
```
import sys
import os
sys.path.append(f"{os.environ['HOME']}/python-study/300/")
print(sys.path)
```

### windows : sys.path.append 대신 PYTHONPATH로 python 실행할 때 path를 추가할 수 있다
```
PYTHONPATH="${HOME}/python-study/jump2python/week4/game" python
```

### ubuntu : 모르겠당....

### \_\_init__.py의 용도
```
※ python3.3 버전부터는 __init__.py 파일이 없어도 패키지로 인식한다(PEP 420)
https://wikidocs.net/1418

~/python-study$ python
>>> import jump2python.week4.game

이렇게 하면 jump2python, week4에 __init__.py이 없어도 game을 가져올 수 있었음
```
- \_\_init__.py에 \_\_all__ 변수를 사용하면 *로 import 할 때 아래 단계를 바로 사용가능
```
__all__ = ['echo']

>>> from jump2python.week4.game.sound import *
>>> echo.echo_test()
echo
```
- 같은 패키지 안에 있는 모듈을 사용하고 싶을 때 상대 경로로 사용 가능
```
# 상대 경로
from ..sound.echo import echo_test

# 절대 경로
from game.sound.echo import echo_test
```