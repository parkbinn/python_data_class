# number = int(input())

# if number < 5:
#     print("숫자가 5보다 작습니다.")
# elif 5< number < 10:
#     print ("5보다 크고 10보다 작다")
# else:
#     print("10보다 큽니다.")

"""
서울에서 부산을 간다고 가정하에 나의 주머니에 있는
돈(money)에 따른 조건문
if => 7만원 있으면 비행기를 타고
elif => 5만원 있으면 기차를 타고
elif => 3만원 있으면 버스를 타고
else => 걸어간다.
"""

from re import I


a = 0
while a < 5:
    a = a + 1
    print(a)


# Q. 1부터 5까지 더하는 프로그램을 만들어보시오.
# (1) for 
# (2) while

# a = 1+2+3+4+5
# result = 0
# for i in range(1,6):
#     result += i #result += i
#     print (result)

for i in range(10): #0~9
    if 3<=i<=5:
        continue #반복문의 코드 처음으로 돌아간다.
    print (i) # 0,1,2,6,7,...
