#-*-coding:cp949
cars = 100 #�ڵ��� 100��
space_in_a_car = 4.0 #�������� �ڵ��� 4��
drivers = 30 #������ 30��
passengers = 90 #�°� 90��
cars_not_driven = cars - drivers #���Ұ� �ڵ��� = "�ڵ���-������"
cars_driven = drivers #��밡�� �ڵ��� = ������
carpool_capacity = cars_driven * space_in_a_car #īǮ ����� = ��밡�� �ڵ��� * �������� �ڵ���
average_passengers_per_car = passengers / cars_driven # �� �Ѵ�� ��� �°�


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."