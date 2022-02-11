# for wating_no in range(1,6):
#     print("대기번호: {0}".format(wating_no))
    
# starbucks=['아이언맨','토르','아이엠 그루트']
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

# #while
# customer='토르'
# index=5
# while index >=1:
#     print("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(customer,index))
#     index-=1
#     if index==0:
#         print('커피는 폐기처분되었습니다.')

# customer = '아이언맨'
# index=1
# while True:
#     print("{0}, 커피가 준비되었습니다. 호출{1}회.".format(customer,index))
#     index+=1

# customer = '토르'
# person='unknown'
# while person != customer:
#     print ("{0}, 커피가 준비되었습니다.".format(customer))
#     person=input("이름이 어떻게 되세요?")
# print("{0}, 커피가 나왔습니다.".format(customer))

# absent=[2,5] #결석
# no_book = [7]
# for student in range(1,11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 끝, {0}는 교무실로 따라와".format(student))
#         break
#     print("{0}야, 책 읽어봐".format(student))

#출석번호 1 2 3 4, 앞에 100을 붙이기로 함.
# student=list(range(1,6))
# print(student)
# student=[i+100 for i in student]
# print(student)

# #학생 이름을 길이로 변환
# students=["Iron man", "Thor", "I am groot"]
# students=list(len(i) for i in students)
# print(students)