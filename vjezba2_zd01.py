# Napišite program vjezba2_zd01.py koji od korisnika traži unos dva cijela broja i potom
# ispisuje njihovu sumu (koristite naredbe input i print). Napravite tri verzije programa:
# a) sa korištenjem tri varijable (prvi_pribrojnik, drugi_pribrojnik i zbroj)

prvi_pribrojni= int(input("Upisite prvi pribrojnik :"))
drugi_pribrojni= int(input("Upisite drugi pribrojnik :"))
zbroj = prvi_pribrojni + drugi_pribrojni
print("{} + {} = {}".format(prvi_pribrojni,drugi_pribrojni,zbroj))

# b) sa korištenjem dvije varijable (prvi_pribrojnik, drugi_pribrojnik)

prvi_pribrojni= int(input("Upisite prvi pribrojnik :"))
drugi_pribrojni= int(input("Upisite drugi pribrojnik :"))
print("{} + {} = {}".format(prvi_pribrojni,drugi_pribrojni,prvi_pribrojni + drugi_pribrojni))

# c) bez korištenje varijabli
