#-coding:utf8
# http://learnpythonthehardway.org/book/

people = 10
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars.") #맞는지확인
elif cars < people:
    print("We should no take the cars.") #틀리다면 맞는지다시한번확인
else:
    print("We can`t decide.") #결과적으로 틀리면 이것을 출력

if trucks > cars:
    print("That`s too many trucks")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can`t decide")

if people > trucks:
    print("Alright, let`s just take the trucks.")
else:
    print("Fine, let`s stay home then.")