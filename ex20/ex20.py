#-*-coding:cp949
from sys import argv

script,input_file = argv

def print_all(f) :
    print(f.read())

def rewind(f) :
    f.seek(0)

def print_a_line (line_count, f):
    print ("%d %s" % (line_count, f.readline()))

current_file = open(input_file)

print("First let`s print the whole file:굈")

print_all(current_file)

print("Now let`s rewind, kind of like tape.")

rewind(current_file)

print("Let`s print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

#만약 실행이안된다면 edit configuration에서 스크립트파라멘터에 test.txt추가