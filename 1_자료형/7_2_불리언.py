# 참(True), 거짓(False)

# T와 F를 대문자로 적어야 한다.
a1 = True
a2 = False
print('True type : ', type(a1))  # <class 'bool'>
print('False type : ', type(a2))  # <class 'bool'>

# 리스트, 튜플, set 또한 값이 있으면 참 없으면 거짓
a3 = [1, 2, 3, 4]
while a3:
    a3.pop()
    print(a3)
# [1, 2, 3]
# [1, 2]
# [1]
# []
