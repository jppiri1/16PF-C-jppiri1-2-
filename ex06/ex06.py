#-*-coding:cp949
x = "There are %d types of people" %10 # %d �ڸ��� 10����
binary = "binary" # binary = "binary"
do_not = "don`t" # do_not = "don`t"
y = "those who know %s and those who %s." % (binary, do_not) # %s�� ���ʴ�� binary(binary)�� do_not(don`t)�� ����

print x # x���
print y # y ���

print "I said: %r." % x # %r �ڸ��� x���
print "I also said: '%s'."% y # %s �ڸ��� y���

hilarious = False # hilarious = False
joke_evaluation = "Isn`t that joke so funny?! %r" # joke_evaluation = "Isn`t that joke so funny?! %r"

print joke_evaluation % hilarious # Isn`t that joke so funny?! False�� ���

w = "this is the left side of..." # w = "this is the left side of..."
e = "a string with a right side." # e = "a string with a right side."

print w + e # w�� e�� �̾ ���
