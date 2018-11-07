
print("Digite 3 números para os lados do triangulo")
lado1=input("digite o valor do primeiro lado")
lado2=input("digite o valor do segundo lado")
lado3=input("digite o valor do terceiro lado")

lado1 =int(lado1)
lado2 =int(lado2)
lado3 =int(lado3)

if lado1<=0 or lado2<=0 or lado3<=0:
	print("não é triangulo")

elif lado1==lado2 and lado2==lado3 :
	print("triangulo equilátero")

elif lado1==lado2 or lado2==lado3 or lado3==lado1 :
	print("triangulo isóceles")

else:
	print("triangulo escaleno") 