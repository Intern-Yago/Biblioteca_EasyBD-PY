import sqlite3
banco = sqlite3.connect('Primeiro_Banco.db')
cursor = banco.cursor()
'''cursor.execute('INSERT INTO pessoas VALUES("João",50,"joao_123@gmail.com")')
banco.commit()'''
cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())