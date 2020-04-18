# import pickle
# data = {
#     'a': [1, 2.0, 3, 4+6j],
#     'b': ("character string", b"byte string"),
#     'c': {None, True, False}
# }
# with open('data.pickle', 'wb') as f:
#     pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
# with open('data.pickle', 'rb') as f:
#     data = pickle.load(f)
#     print(data)

# import random
# import string
# import pickle
#
#
# def randomString(stringLength=5):
#     letters = string.ascii_lowercase
#     return ''.join(random.choice(letters) for i in range(stringLength))
#
#
# data = {randomString(): random.randint(0, 100) for i in range(0, 100)}
# print(data)
#
# with open('dict.bat', 'wb') as f:
#     pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
# with open('dict.bat', 'rb') as f:
#     re_data = pickle.load(f)
#     for key, value in re_data.items():
#         print(str(key) + ": " + str(value))

# def is_number(s):
#     try:
#         int(s)
#         return True
#     except ValueError:
#         return False
#
# while 1:
#     n = input("Enter integer: ")
#     if is_number(n):
#         print("ok")
#         break
#     else:
#         print("not ok, re enter!")