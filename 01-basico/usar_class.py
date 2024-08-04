from class_definition import ProcessadorCSV
arquivo_csv = 'exemplo.csv'  # substitua 'exemplo.csv' pelo caminho do seu arquivo CSV
coluna = 'estado' # coluna que deseja filtrar
valor = 'SP'  # valor que você quer filtrar
colunas = ['estado', 'valor']
atributos = ['SP', 250]

# Exemplo de uso
print(">>>>> EXEMPLO 1")

processador = ProcessadorCSV(arquivo_csv)
df_filtrado = processador.processar_por_estado(valor)

print(df_filtrado)


# Exemplo de uso
print("")
print(">>>>> EXEMPLO 2")

processador = ProcessadorCSV(arquivo_csv)
df_filtrado_generico = processador.processar_generico(coluna, valor)

print(df_filtrado_generico)


# Exemplo de uso
print("")
print(">>>>> EXEMPLO 3")

processador = ProcessadorCSV(arquivo_csv)
df_filtrado_generico_sem_recursividade = processador.processar_generico_sem_recursividade(colunas, atributos)

print(df_filtrado_generico_sem_recursividade)


# Exemplo de uso
print("")
print(">>>>> EXEMPLO 4")

processador = ProcessadorCSV(arquivo_csv)
df_filtrado_generico_com_recursividade = processador.processar_generico_com_recursividade(colunas, atributos)

print(df_filtrado_generico_com_recursividade)


