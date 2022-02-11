from random import *
#내 답
# time_list=[]
# for i in range(0,50):
#     time_list.append(randint(5,51))
#     if 5 <= time_list[i] <= 15:
#      print("[o] {0}번째 손님 (소요시간 : {1}분".format(i+1,time_list[i]))
#     else:
#      print("[ ] {0}번째 손님 (소요시간 : {1}분".format(i+1,time_list[i]))
# last=[]
# for i in time_list:
#     if 5<=i<=15:
#         last.append(i)

# print("총 탑승 승객:{}분".format(len(last)))

#정답
cnt=0
for i in range(1,51):
    time=randint(5,50)
    if 5<=time<=15:
        print("[o] {0}번째 손님 (소요시간: {1}분". format(i,time))
        cnt+=1
    else:
        print("[ ] {0}번째 손님 (소요시간: {1}분". format(i,time))
print(cnt)