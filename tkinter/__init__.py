
''' 
1. __init__.py
해당 디렉토리가 패키지의 일부임을 알려주는 역할을 한다
빈 내용이더라도 폴더를 만들고 그 안에 py 파일이 있다면
__init__.py 를 써줘야 패키지로 인식한다.
파이썬 3.3부터는 없어도 잘 동작하지만 호환성을 위해서 둔다.
2. __init__.py 에서 __all__
from 패키지 imprt * 로 import 할 때,
해당 패키지의 모든 모듈이 import 되는 것이 아니라
__init__.py 에서 __all__ 로 설정해 준 모듈만 import 된다
'''