try:
    print("나누기 전용 계산기입니다.")
    nums=[]
    nums.append(int(input("첫번쨰 숫자를 입력하세요:")))
    nums.append(int(input("두번쨰 숫자를 입력하세요:")))
    # nums.append(int(nums[0]/nums[1]))
    print("{0} / {1} = {2}".format(nums[0],nums[1],nums[2]))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err: # err에 뜨는 에러를 프린트하는 것
    print(err)
except: # 나머지 모든 에러에 대해 처리하는 것
    print("알 수 없는 에러가 발생하였습니다.")
# except Exception as err:  # 나머지 모든 에러에 대해 처리하는 것 + err코드 프린트
#     print("알 수 없는 에러가 발생했습니다.")
#     print(err)