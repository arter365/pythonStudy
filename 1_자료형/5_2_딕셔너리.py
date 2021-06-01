# --- 딕셔너리는 순서가 없다 (value는 같아도 되지만 key는 같을 수 없다) ---

# 딕셔너리 읽기 [키로 읽기]
a1 = {'name': 'Eric', 'age': '15'}
print('딕셔너리 읽기1 : ', a1['name'])    # Eric   (없는 키를 찾으면 KeyError: 'xxx'라고 발생)

# 딕셔너리 읽기 [get함수로 읽기]
print('딕셔너리 읽기2 : ', a1.get('name'))  # Eric (없는 키를 찾으면 None 메시지가 나옴)
print('딕셔너리 읽기2 : ', a1.get('name1', '없음'))  # Eric (없는 키를 찾을 때 출력 할 메시지 지정가능)

# 딕셔너리에 키가 있는지 확인
print('딕셔너리에 있는지 : ', 'age' in a1)

# 딕셔너리 추가
a2 = {1: 'a'}
a2['name'] = 'b'    # Key와 Value 추가
print('딕셔너리 추가 : ', a2)   # {1: 'a', 'name': 'b'}

# 딕셔너리 삭제
# del a2[0]      # 딕셔너리는 순서가 없기 때문에 키로 지워야 한다.
del a2[1]       # 여기서 1은 순서가 아니라 Key값이다.
print('딕셔너리 삭제 : ', a2)   # {'name': 'b'}

a3 = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}

# keys (Key 리스트 만들기)
print('keys : ', a3.keys())  # dict_keys(['name', 'phone', 'birth'])

# values (Value 리스트 만들기)
print('values : ', a3.values())  # dict_values(['pey', '0119993323', '1118'])

# items (키,값을 배열안에 튜플형태로 리턴)
print('items : ', a3.items())
# dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')])

# --- 예제 ---
for k in a3.keys():
    print('key : ', k)
# key :  name
# key :  phone
# key :  birth

for v in a3.values():
    print('value : ', v)
# value :  pey
# value :  0119993323
# value :  1118

for k, v in a3.items():
    print('key : ', k)
    print('value : ', v)
# key :  name
# value :  pey
# key :  phone
# value :  0119993323
# key :  birth
# value :  1118

# clear (key,value 모두 지우기)
a3.clear()
print('clear : ', a3)   # {}
