# 튜플선언 (변하면 안되는 값을 쓸 때 튜플을 사용하게 된다.)
a1 = (1, 2, 3, 4, 5)

# 튜플 요소값 삭제 시 오류
# del a1[0]   # TypeError: 'tuple' object doesn't support item deletion

# 튜플 요소값 변경 시 오류
# a1[0] = 'a' # TypeError: 'tuple' object does not support item assignment

# 인덱싱
a2 = a1[0]
print('튜플 인덱싱 : ', a2)  # 1
print('type : ', type(a2))  # <class 'int'>

# 슬라이싱
a3 = a1[1:]
print('튜플 슬라이싱 : ', a3)   # (2, 3, 4, 5)
print('원본 튜블 : ', a1)   # (1, 2, 3, 4, 5)
print('type : ', type(a3))  # <class 'tuple'>

# 튜플 더하기
a4 = (6, 7)
# (1, 2, 3, 4, 5, 6, 7)   // 튜플원본은 변화없고 새로운 튜플을 만듬.
print('튜플 더하기 : ', a1 + a4)

# 튜플 곱하기
print('튜플 곱하기 : ', a1 * 2)  # (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
