import theater_module
theater_module.price(3)
theater_module.price(4)
theater_module.price_morning(3)
theater_module.price_soldier(3)

import theater_module as mv # mv로 호출
mv.price(3)
mv.price(4)
mv.price_soldier(3)

from theater_module import *
# from random import *
price(3)
price_morning(3)
price_soldier(3)

from theater_module import price, price_morning
# 내가 쓸 함수만 임폴트


from theater_module import price_soldier as sol
sol(5)