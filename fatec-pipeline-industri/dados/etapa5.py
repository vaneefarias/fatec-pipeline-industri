class RegrasNegocio:
    def __init__(self, df):
        self.df = df.copy()
        
    def adicionar_alerta_temperatura(self, limite_maximo=80.0):
        """Cria uma nova coluna indicando se a temperatura ultrapassou o limite crítico."""
        # Vamos criar uma coluna chamada 'alerta_temp' que fica com True se temperature > limite_maximo, senão False
        self.df["alerta_temp"] = self.df["temperature"] > ___
        
        return self  # Mantém o method chaining
        
    def obter_dados(self):
        return self.df
