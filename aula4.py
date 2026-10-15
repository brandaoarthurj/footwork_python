"""
Listas em Python
Tpo list = Mutavel
Suporta varios valores de qualquer tipo
Conhecimento reutilizaveis - indices e fatiamento
Metodos uteis:
    append, imsert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[1] (CRUD)

"""
lista = ['Scoot Henderson', 00, 3, 'Pointer']
lista.append('Luka Doncic')
lista.append('Donovan Clingan')
five = lista.pop()
six = lista.pop()
lista.append('Stephen Curry')

seven = lista.pop(0)
lista.append('Carmelo Anthony')

lista.insert(0, 'Lebron James')
lista.insert(1, 'Anthony Davis')
lista.insert(2, 'Lamello Ball')
lista[3] = 'Anthony Edwards'
lista[4] = 'Cooper Flagg'
lista[5] = 'Kyrie Irving'
lista[7] = 'Klay Thompson'

print(lista[0], lista[1], lista[2])
print(lista, five, six, seven)
