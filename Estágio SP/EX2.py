while True:
    try:
        valor = int(input("Digite um valor: "))
        break
    except ValueError:
        print("Digite apenas números inteiros.")

n1 = 0
n2 = 1
contador = 0
fibonacci = [0,1]

if valor <= 0:
    print("Digite apenas números positivos.")
else:
    while contador < valor:
        n3 = n1 + n2
        fibonacci.append(n3)
        n1 = n2
        n2 = n3
        contador += 1

if valor in fibonacci:
    print("Este número pertence à sequência de Fibonacci.")
else:
    print("Este número não pertence à sequência de Fibonacci.")