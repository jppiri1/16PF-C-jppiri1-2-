

def add(a, b):
    print("ADDING %d + %d" %(a, b))
    return a + b
def subtract(a, b):
    print("SUBTRACTING %d - %d" % (a, b))
    return a - b

def multiplay(a, b):
    print("MULTIPLAYING %d * %d" % (a, b))
    return a * b

def divide(a, b):
    print("DIVIDING %d / %d" % (a, b))
    return a / b

print("Let`s do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiplay(90, 2)
iq = divide(100, 2)

print("Age: %d, Height: %d, Weight: %d IQ: %d" % (age, height, weight, iq))



print("Here is a puzzle.")

what = add(age, subtract(height, multiplay(weight, divide(iq, 2))))

print("That becomes: ",what, "Canyou do it by hand?")