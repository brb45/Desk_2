import json

test_data = [1,2,3]

test_jstr = json.dumps(test_data)
print(type(test_jstr)) # <class 'str'>
print(len(test_jstr)) # 9

test_data_str = "[1,2,3]"
test_data_str = json.dumps(test_data_str)
print(type(test_data_str))
print(len(test_data_str)) # 9


# data_reverse = json.loads(test_jstr)
# print(type(data_reverse)) # <class 'list'>
# print(data_reverse)