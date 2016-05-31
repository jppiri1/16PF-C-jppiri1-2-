#-coding:utf8
a = 0
b = 0
for i in range(1, 101):
    a += i*i # i의 제곱을 a에더함
    b += i   # i의 제곱을 b에더함
print(a) # 
print(b+b)
print((b*b)-a)