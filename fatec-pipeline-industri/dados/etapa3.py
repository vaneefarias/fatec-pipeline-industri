from pipeline import CarregadorCSV, LimpadorDados

def executar_pipeline():
    caminho_arquivo = r"C:\\Users\\Geovanna\\Downloads\\equipment_anomaly_data.csv" 
    colunas_obrigatorias = ["temperature","pressure","vibration","humidity","equipment","location","faulty"] 
    
    
    carregador = CarregadorCSV(caminho_arquivo, colunas_obrigatorias)
    df_bruto = carregador.carregar()
    
    
    limpador = LimpadorDados(df_bruto)
    
    
    df_limpo = (
        limpador
        .padronizar_colunas()
        .remover_nulos(subset=["temperature","pressure","vibration","humidity","equipment","location","faulty"])
        .obter_dados()
    )
    
    print("Dados limpos com sucesso!")
    print(df_limpo.head())

if __name__ == "__main__":
    executar_pipeline()