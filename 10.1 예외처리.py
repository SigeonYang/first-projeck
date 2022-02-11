try:
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫번쨰 숫자를 입력하세요:"))
    num2 = int(input("두번쨰 숫자를 입력하세요:"))
    print("{0} / {1} = {2}".format(num1,num2,int(num1/num2)))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err: # err에 뜨는 에러를 프린트하는 것
    print(err)