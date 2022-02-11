# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름: {0}\t나이: {1}\t".format(name,age),end='')
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *lang): # *: 가변인자고 맘대로 넣을 수 있다.
    print("이름: {0}\t나이: {1}\t".format(name,age),end='')
    for i in lang:
        print(i, end="")
    print()

profile("유재석",20,"Python", "Java", "c", "c++", "c#","JavaScript")
profile("김태호", 25, "Kotlin", "Swift ")