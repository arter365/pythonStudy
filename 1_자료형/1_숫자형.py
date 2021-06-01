# 자료형을 알고 있다면 그 언어의 절반을 터득한 것

# 숫자형 (정수형 : 1,2,-2  실수형 : 1.24, -34.56)
a1 = 1                          # python은 변수 앞에 type을 선언하지 않는다.
print('정수값', a1)             # 1
print('정수타입', type(a1))     # <class 'int>

a2 = 1.24
print('실수값', a2)             # 1.24
print('실수타입', type(a2))     # <class 'float'>

# 사칙연산
a3 = 3
a4 = 4
print('더하기 : ', a3 + a4)         # 7
print('빼  기 : ', a3 - a4)         # -1
print('곱하기 : ', a3 * a4)         # 12
print('제  곱 : ', a3 ** a4)        # 81
print('나누기 : ', a3 / a4)         # 0.75
print('나누기 몫 : ', a3 // a4)     # 0
print('나누기 나머지 : ', a3 % a4)  # 3
