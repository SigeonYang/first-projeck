# 하나의 디렉토리에 여러 모듈 파일을 모아둠

# import travel.thailand # 맨 뒤는 모듈이나 패키지만 가능
#                        # 함수나 클래스는 직접 임폴트 불가능
# trip_to=travel.thailand.ThailandPackage()
# trip_to.detail()

from travel.thailand import ThailandPackage
trip_to=ThailandPackage()
trip_to.detail()

# from random import * => 랜덤 모듈에서 모든 것들을 사용하겠다

# from travel import *
# 트래블 패키지에서 전체를 임폴트 해오려면, 패키지에서 공개 여부를 설정해야 한다.
# __init__ 파일을 통해
# __init__ 안에 __all__ = ["vietnam"] 가 있음