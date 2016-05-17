#-coding:utf8
# http://learnpythonthehardway.org/book/

the_count=[1, 2, 3, 4, 5]
fruits = ['apples','oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']


for number in the_count:
    print("This is count %d" % number) #for를 이용하면 위의 함수 만큼여러번 출력


    for fruit in fruits:
        print("A fruit oftype:%s" % fruit)



for i in change:
    print("I got %r" % i)


elements = []


for i in range(0,6):
    print("Adding %d to the list." % i)

    elements.append(i)



elements2 = [i for i in range(0,6)] #range는 등차수열을만든다


for i in elements:
    print("Element was:%d" % i)

#ex27 ~ ex33 중요