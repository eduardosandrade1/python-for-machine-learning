#forma mais simples que o .map()
kmh = [40, 50, 56, 64, 73, 79, 85, 96, 100, 120]

mph = [x/1.61 for x in kmh]
print(mph)

caracteres = [i for i in 'eduardo']
print(caracteres)