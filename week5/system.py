import os

print(os.getcwd())

# try:
#     filename = "test.txt"
#     f = open(filename, 'rt')
#     text = f.read()
#     print(text)
#     f.close()
# except IOError:
#     print("problem reading: " + filename)

# command = input("Enter command: ")
# filename = input("Enter filename: ")

command = "cd"
filename = "abc.txt"
dir_name = "abc"
parent_dir = os.getcwd()

if command == "mkdir":
    path = os.path.join(parent_dir, dir_name)
    try:
        os.mkdir(path)
        print("created: " + path)
    except FileExistsError:
        print("path already exists: " + path)

if command == 'mkfile':
    path = os.path.join(parent_dir, filename)
    try:
        file = open(path, 'r')
        print('file already exists: ' + path)
    except IOError:
        print('created: ' + path)
        file = open(path, 'w')

if command == 'ls':
    list_file = os.listdir(parent_dir)
    list_file = [parent_dir + "\\" + i for i in list_file]
    print(list_file)

if command == 'cd':
    print(os.getcwd())
    os.chdir('D:\\TrashPy\\Python-Hus\\week4')
    print(os.getcwd())


def list_tree_dir(startPath):
    for root, dirs, files in os.walk(startPath):
        level = root.replace(startPath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))


list_tree_dir("D:\\TrashPy")
