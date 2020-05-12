"""
# Exemplos

num =[2,5,9,1]
num[2] =3
num.append(7)
num.sort()
num.sort(reverse=True)
num.append(2)
print(num)
num.remove(2)# remove apenas o primeiro elemento com o valor selecionado
if 5 in num:
    num.remove(5)
else:
    print('Não achei o valor 5 na lista')
#num.pop()
print(num)
print(f'Essa lista possui:{len(num)} elementos')
--------------------------------------------------------------------------------------
valores =list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Fim')
---------------------------------------------------------------------------------------
#Listas encadeadas
teste = list()
teste.append('Italo')
teste.append(20)
galera = list()
galera.append(teste[:])
teste[0] = 'Julia'
teste[1] = 20
galera.append(teste[:])
print(galera)
-----------------------------------------------------------------------------------------
galera =[['João',19],['Ana',33],['Joaquim',13],['Maria',45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')
"""

galera = list()
dado = list()
totmai =totmen= 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)

for p in galera:
    if p[1] >=21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores e tantos {totmen} menores de idade')