saque=int(input('Valor do saque (min=10 reais / max = 600 reais) >> '))

# Notas
notas100=saque//100
notas50=saque//50
notas10=saque//10
notas5=saque//5
notas1=saque//1


# bloco PARA NOTAS DE CINQUENTA
aux=notas100*100
saque=saque-aux
notas50=saque//50

# bloco PARA NOTAS DE DEZ
aux=notas50*50
saque=saque-aux
notas10=saque//10

#bloco PARA NOTAS DE CINCO
aux=notas10*10
saque=saque-aux
notas5=saque//5

#bloco PARA NOTAS DE UM
aux=notas5*5
saque=saque-aux
notas1=saque//1

print(notas100,'notas de cem')
print(notas50,'notas de cinquenta')
print(notas10,'notas de dez')
print(notas5,'notas de cinco')
print(notas1,'notas de um')
	
