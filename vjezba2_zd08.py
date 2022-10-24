broj = int(input("Upisite broj :"))
broj = broj % 1000
sto=broj//100
des=broj%100//10
jed=broj%100%10
print("{}\n{}\n{}".format(sto,des,jed))