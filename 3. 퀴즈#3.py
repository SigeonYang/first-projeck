site=input('사이트 주소를 입력하세요:')
my_str = site.replace("https://","")#규칙1
my_str = my_str[:my_str.index(".")] #처음 . 나오는 곳까지 슬라이싱
print(my_str)
password=my_str[:3] + str(len(my_str)) +str(my_str.count('e'))+"!"
print("{}의 비밀번호는 {}입니다.".format(site,password))