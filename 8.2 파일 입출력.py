# score_file = open("score.txt", "w",encoding="utf8") #w는 덮어쓰기목적이라는 뜻
# print("수학:0", file=score_file)
# print("영어:50", file=score_file)
# score_file.close()


# score_file = open("score.txt", "a",encoding="utf8") #a는 이미 있는 파일에 어펜드
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8") #읽기 모드
# print(score_file.read()) #전부 읽기
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline()) #한줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

#몇줄인지 모를때 반복문으로 불러오기
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line: #라인이 없을 경우
#         break
#     print(line)
# score_file.close()

#리스트에 값 다 넣기
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line,end="")
score_file.close()
