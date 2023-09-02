import sqlite3

# Conectando ao banco de dados ou criando-o se não existir
conn = sqlite3.connect('db/dataBasePython.db')
cursor = conn.cursor()

# Criando a tabela se ela não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Recursos (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        quantidade INTEGER
    )
''')
conn.commit()

def inserir_recurso(nome, quantidade):
    cursor.execute('INSERT INTO Recursos (nome, quantidade) VALUES (?, ?)', (nome, quantidade))
    conn.commit()
    print("Recurso inserido com sucesso!")

def listar_recursos():
    cursor.execute('SELECT * FROM Recursos')
    recursos = cursor.fetchall()
    for recurso in recursos:
        print(f"ID: {recurso[0]}, Nome: {recurso[1]}, Quantidade: {recurso[2]}")

def atualizar_produto(id, novo_nome, nova_quantidade):
    cursor.execute('UPDATE Recursos SET nome=?, quantidade=? WHERE id=?', (novo_nome, nova_quantidade, id))
    conn.commit()
    print("Recurso atualizado com sucesso!")

def excluir_produto(id):
    cursor.execute('DELETE FROM Recursos WHERE id=?', (id,))
    conn.commit()
    print("Recurso excluído com sucesso!")

# Usando
inserir_recurso('Café', 10)
inserir_recurso('Pão', 20)
listar_recursos()
atualizar_produto(1, 'Outro Café', 100)
excluir_produto(2)
listar_recursos()
conn.close()