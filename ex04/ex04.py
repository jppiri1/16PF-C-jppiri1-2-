#-*-coding:cp949
cars = 100 #자동차 100대
space_in_a_car = 4.0 #공간안의 자동차 4대
drivers = 30 #운전자 30명
passengers = 90 #승객 90명
cars_not_driven = cars - drivers #사용불가 자동차 = "자동차-운전자"
cars_driven = drivers #사용가능 자동차 = 운전자
carpool_capacity = cars_driven * space_in_a_car #카풀 수용력 = 사용가능 자동차 * 공간안의 자동차
average_passengers_per_car = passengers / cars_driven # 차 한대당 평균 승객


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."