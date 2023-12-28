# 객체 비교 연산자 살펴보기
'''
==> 객체는 메모리 힙 영역에 있는 데이터 >> 객체(Object)
==> 데이터의 설명서 / 명세서 에 해당하는 class 를 기반으로 생성됨
==> 파이썬은 모~든 데이터는 객체(Object) 
'''

# print(10 is 10)
# 해당 명령으로 진행시 SyntaxWarning 이 발생



num1 = 10
num2 = 10

num3 = 20

print(num1 is num2)
print(id(num1) == id(num2))
print(id(num1) == id(num3))
print(num1 is int())

name = ""