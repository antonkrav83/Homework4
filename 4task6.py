import re
my_string = input("Введите текст: ")
my_list = re.sub(r'[^\w\s]',' ', my_string).split()
print("Количество различных слов в тексте: ", len(set(my_list)))