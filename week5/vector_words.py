import os
import operator
import json

import _collections
from random_word import RandomWords

path_source = 'D:\\TrashPy\\Python-Hus'
dictionary = 'text_docs'
base_filename = 'filetext'
filename_suffix = '.txt'


def random_text_generator(path, filename):
    path_filename = os.path.join(path, filename)
    if not os.path.exists(path_filename):
        file = open(path_filename, 'w')


def random_files_in_text_docs():
    path_text_docs = os.path.join(path_source, dictionary)
    # mkdir folder text_docs if not exist
    if not os.path.exists(path_text_docs):
        os.makedirs(path_text_docs)
    # generate 10 file txt
    for i in range(0, 4):
        filename = base_filename + str(i) + filename_suffix
        random_text_generator(path_text_docs, filename)
        # print(filename)


def convert_data(sorted_data):
    result = {}
    for turkey in sorted_data:
        result[turkey[0]] = turkey[1]
    return result


def add_file(data, filename):
    path = os.path.join(os.getcwd(), filename)
    with open(path, 'w') as outfile:
        json.dump(data, outfile)


def get_vector(data, size):
    vector = ['' for i in range(0, size)]
    temp = 0
    for key, value in data.items():
        if temp == size:
            break
        vector[temp] = key
        temp += 1

    return vector


def process():
    random_files_in_text_docs()
    path_text_docs = os.path.join(path_source, dictionary)
    print(path_text_docs)
    data_temp = {}
    for i in range(0, 4):
        path_file_text = path_text_docs + '\\' + base_filename + str(i) + filename_suffix
        f = open(path_file_text, 'r')
        word_list = f.read().split()
        for word in word_list:
            word = word.replace(".", "")
            if word not in data_temp:
                data_temp[word] = 0
            data_temp[word] += 1

    sorted_data = sorted(data_temp.items(), key=operator.itemgetter(1), reverse=True)
    data = convert_data(sorted_data)
    add_file(data, 'data.json')
    vector = get_vector(data, 10)
    print(vector)

    for i in range(0, 4):
        path_file_text = path_text_docs + '\\' + base_filename + str(i) + filename_suffix
        f = open(path_file_text, 'r')
        word_list = f.read().split()
        print(path_file_text + ": ", end="")
        cw = [0 for i in range(0, 10)]

        for word in word_list:
            word = word.replace(".", "")
            for i in range(0, len(vector)):
                word_key = vector[i]
                if word == word_key:
                    cw[i] += 1

        print(cw, end="\n")


    # load file json
    # with open('data.json') as json_file:
    #     re_data = json.load(json_file)
    #
    # print(json.dumps(data, indent=4))

process()
