from copy import copy

a1 = [1, 2, 3]

# 주소 복사
a2 = a1
# 주소값 확인
print('주소값 a1 : ', id(a1))   # 1796620243520 (주소는 바뀜)
print('주소값 a2 : ', id(a2))   # 1796620243520
# is (주소가 같은지 확인)
print('주소비교 a1,a2 : ', a1 is a2)  # True

# 값 복사
a3 = a1[:]
# 주소값 확인
print('주소값 a1 : ', id(a1))   # 1796620243520
print('주소값 a3 : ', id(a3))   # 1971504962752 (주소가 다름)
# is (주소가 같은지 확인)
print('주소비교 a1,a3 : ', a1 is a3)  # False

# 함수를 이용한 값 복사 (from copy import copy 추가)
a4 = copy(a1)
# 주소값 확인
print('주소값 a1 : ', id(a1))   # 1796620243520
print('주소값 a4 : ', id(a4))   # 1842626013440 (주소가 다름)
# is (주소가 같은지 확인)
print('주소비교 a1,a3 : ', a1 is a4)  # False

# 변수를 할당하는 다양한 방법 ===========================

# 튜플을 이용한 각각의 변수에 값 할당
a5, a6 = ('python', 'life')
print(a5)   # python
print(a6)   # life

# 위와 동일 (튜플에 튜플을 각각 할당)
(a7, a8) = ('python', 'life')
print(a7)   # python
print(a8)   # life

# 리스트도 동일하게 사용가능
[a9, a10] = ['python', 'life']
print(a9)   # python
print(a10)  # life

# 각각의 변수에 같은 값 넣기
a11 = a12 = 'hello'
print(a11)  # hello
print(a12)  # hello

# 변수의 값 바꾸기 (temp 없이)
a13 = 3
a14 = 5
a13, a14 = a14, a13  # 튜플()를 생략한 형태
print(a13)  # 5
print(a14)  # 3
