# 패키지는 모듈을 모아둔 집합
# 하나의 디렉토리에 여러 모듈 파일을 모아둠

import travel.thailand # 맨 뒤는 모듈이나 패키지만 가능
                       # 함수나 클래스는 직접 임폴트 불가능
trip_to=travel.thailand.ThailandPackage()
trip_to.detail()