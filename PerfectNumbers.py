def perfect_numbers(x, y):

    rango_numeros = [n for n in range(x, y+1)]
    divisores = []
    for valor in rango_numeros:
        for num in range(1,1001):
            
            if sum(divisores) == valor:
                return valor

            if sum(divisores) > valor:
                continue

            if (valor % num) == 0:
                divisores.append(num)
        divisores = []

print(perfect_numbers(28,497))