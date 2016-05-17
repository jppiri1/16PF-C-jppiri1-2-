#-coding:utf8
# http://learnpythonthehardway.org/book/

i = 0
numbers = []

while i <6: # while roop는 조건문에따라 실행
    print("At the top i is %d" % i)
    numbers.append(i)

    i = i + 1

    print("Numbers now: " + str(numbers))
    print("At the bottom i is %d" % i)

print("The numbers: ")

for num in numbers:
    print(num)