year = 2024
print(id(2024))
print(id(year))
# 위 예시는 같은 주소를 가지는 것을 확인할 수 있음

year = 2023
print(id(year))
# year 변수의 값이 바뀔 경우 주소가 변경된다.


year = '2023'
print(id(year))



# 위 경우 문자열 2023으로 새로 저장된다.