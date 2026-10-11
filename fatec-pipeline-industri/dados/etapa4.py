import pandas as pd

class TransformadorDados:
    def __init__(self, df):
        self.df = df.copy()
        
    def converter_tipos_numericos(self):
        """Converte as colunas de métricas físicas para valores numéricos."""
        colunas_numericas = ["temperature", "pressure", "vibration", "humidity"]
        
        for coluna in colunas_numericas:
     
            self.df[coluna] = pd.___ (self.df[coluna], errors='coerce')
            
        return self 
        
    def obter_dados(self):
        return self.df