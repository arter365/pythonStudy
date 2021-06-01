# 문자형 ('', "" 모두 동일하게 사용 가능 : ''를 표준으로 사용한다.)
b1 = "Python's favorite food is perl"
b2 = '"Python is very eash." he says.'
print(b1)
print(b2)
b3 = 'Python\'s favorite food is perl'
b4 = "\"Python is very easy.\" he says."
print(b3)
print(b4)

# 문자열 연산
b3 = 'Python'
b4 = ' is fun!'
b5 = b3 + b4
print('문자열 더하기 : ', b5)       # Python is fun!
print('문자열 곱하기 : ', b5 * 3)   # Python is fun!Python is fun!Python is fun!

b6 = 'Life is too short, You need Python'

# 문자열 인덱싱(Indexing)
print('문자열 인덱싱 : ', b6[2])    # f
print('문자열 -인덱싱 : ', b6[-1])  # n (-하면 뒤로 가서 계산한다.)

# 문자열 슬라이싱(Slicing)
print('문자열 슬라이싱 : ', b6[0:4])    # Life

b7 = '20201229Rainy'
print('date : ', b7[:8])
print('weather : ', b7[8:])

b8 = '12345678'
print('문자열 슬라이싱 간격 : ', b8[::2])  # 1357 (2칸간격으로 가져온다. [이상:미만:간격])
print('문자열 슬라이싱 간격 : ', b8[::-2])  # 8642 (-이기 때문에 뒤에서 가져온다.)

# 문자열 포메팅
b9 = 'I eat %d apples.' % 3
b10 = 'I eat ' + str(3) + ' apples.'
b11 = 'I eat %d %s.' % (3, 'apples')
b12 = 'I eat %s %s.' % (3, 'apples')   # %s로 숫자도 표현 가능하다.
b13 = 'I eat {} apples.'.format('3')
b14 = 'I eat {number} {food}.'.format(number='3', food='apples')
food = 'apples'
b15 = f'I eat 3 {food}.'    # python 3.6이상 가능
print(b9)   # I eat 3 apples. (이하 동일한 출력)
print(b10)
print(b11)
print(b12)
print(b13)
print(b14)
print(b15)
b16 = '%0.4f' % 0.1234567
print(b16)  # 0.1235  소수점 자릿수 (반올림 된다.)

b17 = 'hobby'

# 문자열 개수 세기(count)
print('count : ', b17.count('b'))   # (없으면 0)

# 문자열 위치 알려주기(find)
print('find : ', b17.find('o'))  # index는 0,1,2,3,4,5 이렇게 진행된다. (없으면 -1)

# 문자열 삽입(join)
b18 = ','
b19 = 'abcd'
b20 = b18.join(b19)
print('join : ', b20)   # a,b,c,d

b21 = ' hi HELLO'
# 소문자를 대문자로(upper)
print('upper : ', b21.upper())  # HI HELLO

# 대문자를 소문자로(lower)
print('lower : ', b21.lower())  # hi hello

# 양쪽 공백지우기(strip)
print('strip : ', b21.strip())  # hi HELLO

b22 = 'Life is too short'
# 문자열 바꾸기(replace)
print('replace : ', b22.replace('Life', 'Your leg'))    # Your leg is too short
# 문자열 나누기(split) // List를 리턴한다.
print('split : ', b22.split())  # ['Life', 'is', 'too', 'short']
b23 = 'a:b:c:d'
print('split : ', b23.split(':'))  # ['a', 'b', 'c', 'd']
