# 리스트 (리스트명 = [요소1, 요소2, 요소3,...])

a1 = []  # 빈값 가능
a2 = [1, 2, 3]  # 숫자 가능
a3 = ['Life', 'is', 'too', 'short']  # 문자 가능
a4 = [1, 2, 'Life', 'is']   # 숫자 + 문자 가능
a5 = [1, 2, ['Life', 'is']]  # 리스트 + 리스트 가능

print('리스트 값 더하기 : ', a2[0] + a2[2])  # 4
print('리스트 합하기 : ', a2 + a3)  # [1, 2, 3, 'Life', 'is', 'too', 'short']
print('리스트 곱하기 : ', a2 * 2)   # [1, 2, 3, 1, 2, 3]
print('리스트의 슬라이싱 : ', a3[0:3])  # ['Life', 'is', 'too']
print('리스트안의 리스트 가져오기 : ', a5[2])   # ['Life', 'is']
print('리스트안의 리스트 중 값 가져오기 : ', a5[2][0])  # Life
a5[2][0] = 'Love'
print('리스트 값 수정 : ', a5)  # [1, 2, ['Love', 'is']]
a2[1:] = [3, 5]
print('리스트 연속된 값 수정 : ', a2)   # [1, 3, 5]
a4[0:2] = []
print('리스트 값 지우기 : ', a4)    # ['Life', 'is']
del a4[0]
print('del로 리스트 값 지우기 : ', a4)  # ['is']

# ----------- List의 function은 print안에서 실행되지 않았다. --------------
# append 함수
a6 = [1, 2, 3]
a6.append(4)
print('append 함수 : ', a6)  # [1, 2, 3, 4]

# sort 함수
a7 = [1, 3, 2]
a8 = ['가', '다', '나']
a9 = ['A', 'C', 'B']
a7.sort()
a8.sort()
a9.sort()
print('숫자 sort 함수 : ', a7)  # [1, 2, 3]
print('한글 sort 함수 : ', a8)  # ['가', '나', '다']
print('영어 sort 함수 : ', a9)  # ['A', 'B', 'C']

# reverse 함수
a10 = ['a', 'b', 'c']
a10.reverse()
print('reverse 함수 : ', a10)   # ['c', 'b', 'a']

# index 함수 (위치반환)
a11 = [1, 2, 3]
print(a11.index(3))  # 2

# insert 함수 (원하는 index에 값을 추가 할 수 있다.)
a12 = [1, 2, 3]
a12.insert(0, 4)
print('insert 함수 : ', a12)  # [4, 1, 2, 3]

# remove 함수 (제일 처음에 나오는 같은 값만 지운다)
a13 = [1, 2, 3, 1, 2, 3]
a13.remove(3)
print('remove 함수 : ', a13)

# pop 함수 (후입선출)
a14 = [1, 2, 3]
res1 = a14.pop()
print('pop 함수 (res1) : ', res1)
print('pop 함수 (원래리스트) : ', a14)

# count 함수
a15 = [1, 1, 2, 3]
res2 = a15.count(1)
print('count 함수 : ', res2)

# extend 함수 (리스트 확장)
a16 = [1, 2, 3]
a16.extend([4, 5])
print('extend 1 : ', a16)
a17 = [6, 7]
a16.extend(a17)
print('extend 2 : ', a16)
