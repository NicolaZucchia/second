dim = int(input("Inserire la dimensione della lista: \n"))
print("Inserire i valori della lista: \n")
lista = []
for i in (0, dim):
    value = int(input("Valore: \n"))
    lista.append(value)
sum = 0;
for i in (0, dim):
    sum = sum + lista[i]
print("La somma degli elementi nella lista è" + sum + "\n")
