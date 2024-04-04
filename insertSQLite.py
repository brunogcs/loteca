import sqlite3
import pandas as pd

# Importa o arquivo XLSX com o caminho completo
file_path = 'Loteca.xlsx'
dfBase = pd.read_excel(file_path)

# Filtra as colunas desejadas
dfFiltro = pd.DataFrame(dfBase, columns=[
    'Concurso', 'Jogo 1', 'Jogo 2', 'Jogo 3', 'Jogo 4', 'Jogo 5',
    'Jogo 6', 'Jogo 7', 'Jogo 8', 'Jogo 9', 'Jogo 10', 'Jogo 11',
    'Jogo 12', 'Jogo 13', 'Jogo 14'
])

# Insere os dados filtrados no SQLite
conn = sqlite3.connect('loteca.db')
dfFiltro.to_sql('loteca_table', conn, if_exists='replace', index=False)
conn.close()

print("Dados filtrados inseridos no banco de dados SQLite.")

# Realiza o SELECT para obter os dados inseridos
conn = sqlite3.connect('loteca.db')
query = "SELECT * FROM loteca_table"
dfResultadoQuery = pd.read_sql_query(query, conn)
conn.close()

# Apresenta o resultado final
print("\nResultado Query:")
print(dfResultadoQuery)
