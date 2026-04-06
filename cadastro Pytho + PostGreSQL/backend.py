def validar_cadastro(nome, sobrenome, email, telefone, endereco):
    coleta = []
    if nome == '' or nome.isdigit():
        coleta.append(1)
    
    if sobrenome == '' or sobrenome.isdigit():
        coleta.append(2)
    
    if '@' and '.com' not in email or len(email) < 4:
        coleta.append(3)

    if len(telefone) < 10:
        coleta.append(1)
    
    return sum(coleta)

import psycopg2

#de acordo com seu proprioservidor
def conectar():
    conn = psycopg2.connect(
        host="",
        database="",
        user="",
        password="",
        port=""
    )
    return conn    

def inserir_usuario(nome, sobrenome, email, telefone, endereco):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO usuarios (nome, sobrenome, email, telefone, endereco)
        VALUES (%s, %s, %s, %s, %s)
    """, (nome, sobrenome, email, telefone, endereco))

    conn.commit()
    cursor.close()
    conn.close()

def buscar_usuario(email):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT nome, sobrenome, telefone, endereco
        FROM usuarios
        WHERE email = %s
    """, (email,))

    resultado = cursor.fetchone()

    cursor.close()
    conn.close()

    return resultado

def buscar_recentes():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT nome, email, telefone
        FROM usuarios
        ORDER BY id DESC
        LIMIT 5
    """)

    dados = cursor.fetchall()

    cursor.close()
    conn.close()

    return dados
