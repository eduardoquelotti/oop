import pandas as pd

class ProcessadorCSV:
    def __init__(self, arquivo_csv: str):
        self.arquivo_csv = arquivo_csv
        self.df = None
    
    def carregar_csv(self):
        # Carregar o arquivo CSV em um DataFrame
        self.df = pd.read_csv(self.arquivo_csv)
    
    def remover_celulas_vazias(self):
        # Verificar e remover células vazias
        self.df = self.df.dropna()
    
    def filtrar_por_estado(self, estado):
        # Filtrar as linhas pela coluna estado
        self.df = self.df[self.df['estado'] == estado]

    def filtrar_coluna_por_atributo(self, coluna, atributo):
        # Filtrar as linhas pela coluna e atributo desejado
        self.df = self.df[self.df[coluna] == atributo]

    def filtrar_por_colunas(self, colunas, atributos):
        # Filtrar as linhas do dataframe a partir de um vetor de colunas e atributos
        if len(colunas) != len(atributos):
            raise ValueError('Informe um mesmo número de colunas e atributos')
        
        elif len(colunas) == 0:
            return self.df
        
        else:
            # Aplicar filtro iterativamente para cada par coluna-atributo
            for coluna, atributo in zip(colunas, atributos):
                self.df = self.df[self.df[coluna] == atributo]
    
    def processar_por_estado(self, estado):
        # Carregar CSV, remover células vazias e filtrar por estado
        self.carregar_csv()
        self.remover_celulas_vazias()
        self.filtrar_por_estado(estado)
        
        return self.df
    
    def processar_generico(self, coluna, atributo):
        # Carregar CSV, remover células vazias e filtrar por estado
        self.carregar_csv()
        self.remover_celulas_vazias()
        self.filtrar_coluna_por_atributo(coluna, atributo)
        
        return self.df
    
    def processar_generico_2(self, colunas, atributos):
        # Carregar CSV, remover células vazias e filtrar por estado
        self.carregar_csv()
        self.remover_celulas_vazias()
        self.filtrar_por_colunas(colunas, atributos)
        
        return self.df