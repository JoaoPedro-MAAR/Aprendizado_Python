# Todos essas funçoes tambem podem ser utilizadas com vetor





""" listas podem ser somadas porem elas não somaram os elementos e sim concatenados, assim como em uma multiplicação * """
lista_soma1 = [1 , 2 , 3 , 4]
lista_soma2 = [5 , 6 , 7 , 8]
lista_soma3 = lista_soma1 + lista_soma2
print(lista_soma3)


''' Multiplicaçao '''

lista_multiplicação = lista_soma1 * 2
print(lista_multiplicação)

''' A funçao len serve para descobrirmos o tamanho da lista,vamos ver o tamanho de 2 vezes a tem lista_soma3'''

tamanho = len(lista_soma3 * 2)
print(tamanho)

''' A função append serve para adicionarmos um item ao final do indice da lista aqui adicionaremos elementos em uma lista vazia'''

lista = []
lista.append(10)
lista.append(20)
print(f'Foi mostrado a funçao append nessa lista {lista}')

''' Como uma funçao complementar do append temos o insert que pode-se escolher a posiçao e o elemnto que vai ser escolhido'''

lista.insert(0,45)
lista.insert(2, 13)
print(f'Lista com insert{lista}')

''' A funçao del serve para deletar um intervalo '''

del(lista[0:1])
print(lista)
# O dois ponto determina se o intervalo vai ser aberto ou fechado, na esquerda do numero o exclui da lista

''' Remove assim como o delete deleta a primeira ocorrencia de um numero especifico'''

lista2 = [1 , 1 , 2 , 2]
lista2.remove(2)
print(lista2)

''' Clear deleta todos os itens do lista '''
lista3 = [1 , 2 ,3 ,4 ,5 ,6 ,7 ,8 ,9]
print(f'Lista antes do clear {lista3}')
lista3.clear()
print('Lista depois do clear')
print(lista3)

''' Count retorna a quantidade de vezes que esse item aparece na lista'''
lista4 = [1,1,1,2,2,3]
print(lista4)
print('O 1 aparece' ,lista4.count(1), 'vezes' )
print('O 2 aparece' ,lista4.count(2), 'vezes' )
print('O 3 aparece' ,lista4.count(3), 'vezes' )
print('O 5 aparece' ,lista4.count(5), 'vezes' )

''' Index verifica se o item esta na lista e sua posiçao, se tiver mais de um mostrara so a primeira ocorrencia '''
print('INDEX')
print(lista4.index(1))
print(lista4.index(2))
print(lista4.index(3))

''' A função sum soma todos os elementos daquela lista'''
lista_sum = [10,20,30,40]
soma1 = sum(lista_sum)
print(soma1)

''' Min e max verificam qual o menor e maior elemento da lista'''
lista5 = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
print(lista5)
print(min(lista5))
print(max(lista5))

''' Sort ordena a lista em ordem crescente e decrescente'''
lista6 = [10,2,5,1,6]
print(f'Lista seis = {lista6}')
lista6.sort()
print(lista6)

''' Reverse faz com que a lista fique em ordem inversa(caso esteja crescente ficara descrescente e vice-versa)'''

lista6.reverse()
print(lista6)














