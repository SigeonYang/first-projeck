class House:
    #매물 초기화
    def __init__(self,location,deal_type,house_type,price,completion_year):
        self.location=location
        self.house_type=house_type
        self.deal_type=deal_type
        self.price=price
        self.completion_year=completion_year

    #매물 정보 표시
    def show_detail(self):
        print("{0} {1} {2} {3} {4}".format(self.location,self.house_type,self.deal_type,self.price,self.completion_year))

house = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house1.show_detail()