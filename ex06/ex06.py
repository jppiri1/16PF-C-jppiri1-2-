#-*-coding:cp949
x = "There are %d types of people" %10 # %d 자리에 10삽입
binary = "binary" # binary = "binary"
do_not = "don`t" # do_not = "don`t"
y = "those who know %s and those who %s." % (binary, do_not) # %s에 차례대로 binary(binary)와 do_not(don`t)을 삽입

print x # x출력
print y # y 출력

print "I said: %r." % x # %r 자리에 x출력
print "I also said: '%s'."% y # %s 자리에 y출력

hilarious = False # hilarious = False
joke_evaluation = "Isn`t that joke so funny?! %r" # joke_evaluation = "Isn`t that joke so funny?! %r"

print joke_evaluation % hilarious # Isn`t that joke so funny?! False를 출력

w = "this is the left side of..." # w = "this is the left side of..."
e = "a string with a right side." # e = "a string with a right side."

print w + e # w와 e를 이어서 출력
