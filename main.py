dia = int(input())
mes = int(input())
if((dia >= 1 and dia <= 19) and (mes == 1)):
    print("capricornio")
elif((dia >= 20 and dia <= 30) and (mes == 1)):
    print("acuario")
elif((dia >= 1 and dia <= 18) and (mes == 2)):
    print("acuario")
elif((dia >= 19 and dia <= 30) and (mes == 2)):
    print("piscis")
elif((dia >= 1 and dia <= 20) and (mes == 3)):
    print("piscis")
elif((dia >= 21 and dia <= 30) and (mes == 3)):
    print("aries")
elif((dia >= 1 and dia <= 19) and (mes == 4)):
    print("aries")
elif((dia >= 20 and dia <= 30) and (mes == 4)):
    print("tauro")
elif((dia >= 1 and dia <= 20) and (mes == 5)):
    print("tauro")
elif((dia >= 21 and dia <= 30) and (mes == 5)):
    print("geminis")
elif((dia >= 1 and dia <= 20) and (mes == 6)):
    print("geminis")
elif((dia >= 21 and dia <= 30) and (mes == 6)):
    print("cancer")
elif((dia >= 1 and dia <= 22) and (mes == 7)):
    print("cancer")
elif((dia >= 23 and dia <= 30) and (mes == 7)):
    print("leo")
elif((dia >= 1 and dia <= 22) and (mes == 8)):
    print("leo")
elif((dia >= 23 and dia <= 30) and (mes == 8)):
    print("virgo")
elif((dia >= 1 and dia <= 22) and (mes == 9)):
    print("virgo")
elif((dia >= 23 and dia <= 30) and (mes  == 9)):
    print("libra")
elif((dia >= 1 and dia <= 22) and (mes == 10)):
    print("libra")
elif((dia >= 23 and dia <= 30) and ( mes == 10)):
    print("escorpio")
elif((dia >= 1 and dia <= 21) and (mes == 11)):
    print("escorpio")
elif((dia >= 22 and dia <= 30) and (mes  == 11)):
    print("sagitario")
elif((dia >= 1 and dia <= 21) and (mes == 12)):
    print("sagitario")
elif((dia >= 22 and dia <= 30) and (mes == 12)):
    print("capricornio")
else:
    print("ERROR -> Algo Salio mal...")