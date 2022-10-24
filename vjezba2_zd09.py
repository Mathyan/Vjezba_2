broj = int(input("Cetveroznamenkasti broj:"))
print("{}{}{}{}".format(broj%1000%100%10,broj%1000%100//10,broj%1000//100,broj//1000))