class LimpadorDados:
    def __init__(self, df):
        self.df = df.copy()
        
    def remover_nulos(self, subset=None):
        
        self.df.dropna(subset=subset, inplace=True)
        return self
        
    def padronizar_colunas(self):
        
        self.df.columns = (
            self.df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )
        return self
        
    def obter_dados(self):
        
        return self.df