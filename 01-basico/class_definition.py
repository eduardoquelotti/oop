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

    def filtrar_por_colunas_sem_recursividade(self, colunas, atributos):
        # Filtrar as linhas do dataframe a partir de um vetor de colunas e atributos
        if len(colunas) != len(atributos):
            raise ValueError('Informe um mesmo número de colunas e atributos')
        
        elif len(colunas) == 0:
            return self.df
        
        else:
            # Aplicar filtro iterativamente para cada par coluna-atributo
            for coluna, atributo in zip(colunas, atributos):
                self.df = self.df[self.df[coluna] == atributo]
    
    def filtrar_por_colunas_com_recursividade(self, colunas, atributos, df=None):
        # Verificar se o número de colunas e atributos são iguais
        if len(colunas) != len(atributos):
            raise ValueError('Informe um mesmo número de colunas e atributos')
        
        # Inicializar o DataFrame na primeira chamada
        if df is None:
            df = self.df
        
        # Base da recursão: se não há mais colunas para filtrar, retorne o DataFrame atual
        if len(colunas) == 0:
            return df
        
        coluna_atual = colunas[0]
        atributo_atual = atributos[0]

        # Filtrar o DataFrame atual
        df_filtrado = df[df[coluna_atual] == atributo_atual]

        # Continuar a recursão com o DataFrame filtrado
        return self.filtrar_por_colunas_com_recursividade(colunas[1:], atributos[1:], df_filtrado)

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
    
    def processar_generico_sem_recursividade(self, colunas, atributos):
        # Carregar CSV, remover células vazias e filtrar por estado
        self.carregar_csv()
        self.remover_celulas_vazias()
        self.filtrar_por_colunas_sem_recursividade(colunas, atributos)
        
        return self.df
    
    def processar_generico_com_recursividade(self, colunas, atributos):
        # Carregar CSV, remover células vazias e filtrar por estado
        self.carregar_csv()
        self.remover_celulas_vazias()
        # Corrigir para retornar o DataFrame filtrado pela função recursiva
        df_filtrado = self.filtrar_por_colunas_com_recursividade(colunas, atributos)
        
        return df_filtrado