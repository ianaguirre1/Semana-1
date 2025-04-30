lista = [1,2,3,4,5]
while True:
    try:
        numero = int(input("ingresa un numero"))
        for i in lista:
            if i == numero:
                print("encontre el numero")
                break
        else:
                print("no encontré el numero")
                continue
        break
    except:ValueError
    print("ingresa el numero de nuevo")
            
            

