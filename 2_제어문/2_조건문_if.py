# 만약 돈이 있으면 택시를 타고, 돈이 없으면 걸어 간다. (들여쓰기가 중요하다)
money = True
if money:
    print('신나게~')
    print('택시를 타고 가라')
else:
    print('열심히~')
    print('걸어 가라')

# 비교연산자 사용
score = 70
if score >= 90:
    print('수')
elif score >= 60:
    print('우')
else:
    print('미')

kor = 85
eng = 75
# not pass1이 출력된다.
if kor >= 80 & eng >= 70:
    print('pass1')
else:
    print('not pass1')
# ()를 해야 pass2가 출력된다.
if (kor >= 80) & (eng >= 70):
    print('pass2')
else:
    print('not pass2')
# and를 사용하면 ()를 안해도 된다.
if kor >= 80 and eng >= 70:
    print('pass3')
else:
    print('not pass3')
