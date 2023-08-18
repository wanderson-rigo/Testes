lista = list(range(0,20,2))
print(lista)

# Definindo tuplas para informações de livros
livro1 = ("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
livro2 = ("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997)
livro3 = ("1984", "George Orwell", 1949)

# Acessando elementos da tupla
print("Título do livro 1:", livro1[0])
print("Autor do livro 2:", livro2[1])
print("Ano de publicação do livro 3:", livro3[2])

# Desempacotamento de tuplas
titulo, autor, ano = livro1
print("Título:", titulo)
print("Autor:", autor)
print("Ano de publicação:", ano)

def calcular_valores(a, b):
    soma = a + b
    diferenca = a - b
    produto = a * b
    return soma, diferenca, produto

# Chamando a função e recebendo os valores de retorno em uma tupla
resultado = calcular_valores(10, 5)

# Desempacotando os valores da tupla
soma, diferenca, produto = resultado

print("Soma:", soma)
print("Diferença:", diferenca)
print("Produto:", produto)


# conjunto
vogais = {'a', 'e', 'i', 'o', 'u'}
print('Vogais:', vogais)

# Definindo uma função lambda que calcula o quadrado de um número
square = lambda x: x ** 2
cube = lambda x: x ** 3 


# Usando a função lambda para calcular o quadrado de um número
number = 5
squared_number = square(number)

print(f"O quadrado de {number} é {squared_number}")

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)

# Criando um dicionário que armazena informações de uma pessoa
person = {
    "nome": "Alice",
    "idade": 30,
    "cidade": "São Paulo"
}

# Acessando valores do dicionário
print(f"Nome: {person['nome']}")
print(f"Idade: {person['idade']}")
print(f"Cidade: {person['cidade']}")

# Adicionando uma nova chave-valor ao dicionário
person["profissao"] = "Engenheira"

# Modificando o valor de uma chave existente
person["idade"] = 31

# Exibindo o dicionário completo
print(person)

x = 5
print(x)  # Saída: 5
print(id(x))

x = 9
print(x)  # Saída: 9
print(id(x))