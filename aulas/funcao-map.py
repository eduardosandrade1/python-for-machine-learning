#convertendo km por hora em milhas por hora
kmh = [10,50,40,70,90,30,100,120]
mph = []

for i in kmh:
    mph.append(i/1.61)
print(mph)


#usando a funcao map e resultando em uma lista
mph2 = list(map(lambda x: x/1.61, kmh))
print(mph2)