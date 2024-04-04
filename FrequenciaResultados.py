import sqlite3
import pandas as pd

# Realiza o SELECT para obter os dados inseridos
conn = sqlite3.connect('loteca.db')
query = "SELECT * FROM loteca_table"
dfResultadoQuery = pd.read_sql_query(query, conn)
conn.close()


# Calculando a frequência de resultados
def calcular_frequencia_resultados(dfResultadoQuery):
    # Inicialize contadores para cada coluna (1, X, 2)
    contagem_coluna_1 = 0
    contagem_coluna_X = 0
    contagem_coluna_2 = 0

    # Itere pelas linhas da DataFrame
    for _, row in dfResultadoQuery.iterrows():
        for coluna in range(1, 15):  # Considerando as colunas Jogo 1 a Jogo 14
            resultado = row[f'Jogo {coluna}']
            if resultado == 'Coluna 1':
                contagem_coluna_1 += 1
            elif resultado == 'Coluna do meio':
                contagem_coluna_X += 1
            elif resultado == 'Coluna 2':
                contagem_coluna_2 += 1

    # Calcule as frequências
    total_jogos = len(dfResultadoQuery)
    frequencia_coluna_1 = contagem_coluna_1 / total_jogos
    frequencia_coluna_X = contagem_coluna_X / total_jogos
    frequencia_coluna_2 = contagem_coluna_2 / total_jogos

    return frequencia_coluna_1, frequencia_coluna_X, frequencia_coluna_2

# Chamando a função e exibindo os resultados
frequencia_1, frequencia_X, frequencia_2 = calcular_frequencia_resultados(dfResultadoQuery)
print(f"Frequência de vitória do time da casa (Coluna 1): {frequencia_1:.2%}")
print(f"Frequência de empate (Coluna X): {frequencia_X:.2%}")
print(f"Frequência de vitória do time visitante (Coluna 2): {frequencia_2:.2%}")
