class ExportadorCSV:
    def __init__(self, df):
        self.df = df
        
    def salvar(self, caminho_saida):
    
        self.df.to_csv(caminho_saida, index=False)
        print(f"Ficheiro guardado com sucesso em: {caminho_saida}")
