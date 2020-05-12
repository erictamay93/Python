"""
# Criando um dicionário dentro de uma lista
brasil = []
estado1 ={'uf':'Rio de janeiro','sigla':'RG'}
estado2 ={'uf':'São Paulo','Sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])
"""
pessoas = {'nome':'Italo','sexo':'m','idade':20}
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
#for k in pessoas.keys():
#    print(k)
#for k in pessoas.values():
#    print(k)

#for k, v in pessoas.items():
#    print(f'{k} = {v}')

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Unidade Federativa: '))
    brasil.append(estado.copy())#serve para fazer uma copia sem ligações como [:] em listas
print(brasil)