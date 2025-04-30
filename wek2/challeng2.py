lista = list(range(51,101))
lista1 = list(range(0,51))

calificación = int(input("ingresa una calificacion numerica"))
# entrada = input("ingresa las calificaciones separadas por comas: ejmeplo: 80,65,35: ")
# calificaciónes = [int(valor.strip())for valor in entrada.split(",")]

if calificación in lista:
    print("aprovaste")
    
elif calificación in lista1:
    print("no aprovaste")         
entrada = input("ingresa las calificaciones separadas por comas: ejmeplo: 80,65,35: ")
calificaciónes = [int(valor.strip())for valor in entrada.split(",")]
print(calificaciónes)



 