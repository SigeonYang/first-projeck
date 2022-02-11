#피클 = 프로그램 상에서 사용하고있는 코드를 파일로 주는 것
import pickle
# profile_file = open("profile.pickle",'wb')
# #w는 쓰기모드 b는 바이너리/피클을 위해서 항상 바이너리 정의/ 피클에서는 인코딩 설정 필요없음
# profile = {"이름": "박명수", "나이":30, "취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile,profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)
print(profile_file)
profile_file.close()