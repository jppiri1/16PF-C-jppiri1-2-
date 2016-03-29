name = 'Jeong Byeong Il'
age = 23 # not a lie
my_height_cm = 178.2 # inches
cm_to_inch = 1.0 / 2.54
my_height_inch = my_height_cm * cm_to_inch
my_weight_kg = 82.2 # lbs
my_eyes = 'Black'
my_teeth = 'Depending on the coffee'
my_hair = 'Black'

print "Let`s talk about %s" % name
print "He`s %g centimeters tall." % my_height_cm
print "He`s %g inches tall." % my_height_inch
print "He`s %d pounds heavy." % my_weight_kg
print "Actually that`s not too heavy"
print "He`s got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually%s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, my_height_cm, my_weight_kg, age + my_height_cm + my_weight_kg)