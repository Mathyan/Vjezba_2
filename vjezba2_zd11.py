# Napišite program vjezba2_zd11.py koji od korisnika traži unos koeficijenata kvadratne
# jednadžbe a, b i c (kvadratna jednadžba ax2+bx+c=0) i potom ispisuje rješenja ove kvadratne
# jednadžbe x1 i x2, pri čemu pretpostavljamo da je vodeći koeficijent a različit od 0 i da
# kvadratna jednadžba ima realna rješenja (koristimo biblioteku math).
import math
print("Za rijesenje ax^2+bx+c=0")
a = float(input("Upisi a: "))
b = float(input("Upisi b: "))
c = float(input("Upisi c: "))
x_pos = (-b+math.sqrt(b**2-4*a*c))/(2*a)
x_neg = (-b-math.sqrt(b**2-4*a*c))/(2*a)
print("x1 = {}, x2 = {}".format(x_pos,x_neg))