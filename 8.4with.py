# with open("study.txt", "w", encoding="utf8") as study_file:
# #with로 쉽게 불러오기
# #study.txt에 쓰기모드, 인코딩해서 study_file 변수에 저장
#     study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt","r",encoding="utf8") as study_file:
    print(study_file.read())

#위드는 매번 close 필요가 없음