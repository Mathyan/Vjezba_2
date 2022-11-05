d5b = int(input("Upisite peteroznamenkasti broj: "))
zbroj = d5b//10000
zbroj +=d5b%10000//1000
zbroj +=d5b%10000%1000//100
zbroj +=d5b%10000%1000%100//10
zbroj +=d5b%10000%1000%100%10
print("Zbroj znamenka je ",zbroj)