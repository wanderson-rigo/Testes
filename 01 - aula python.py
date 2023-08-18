# encoding: iso-8859-1

def soma_numeros_pares():
    soma = 0
    for numero in range(0, 101, 2):
        soma += numero
    return soma

resultado = soma_numeros_pares()
print("A soma dos números pares de 0 a 100 é:", resultado)

# outra
print(sum(numero for numero in range(0, 101) if numero % 2 == 0))

# outra
pares = 0;
for nPar in range (0,101,2):
    pares += nPar

print("A soma é: ", pares)