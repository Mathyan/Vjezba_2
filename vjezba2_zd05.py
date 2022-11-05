time= int(input("Upisite vrijeme u sekundama: "))
dani= time//86400
sati= time%86400//3600
minute= time%86400%3600//60
sekunde= time%86400%3600%60
print("{} sekunda = {} dana, {} sata, {} minuta, {} sekunde".format(time,dani,sati,minute,sekunde))