from pipeline import (
    CarregadorCSV, 
    LimpadorDados, 
    TransformadorDados, 
    RegrasNegocio, 
    ExportadorCSV
)

def executar_pipeline_completo():
    
    caminho_entrada = r"C:\Users\Geovanna\Downloads\equipment_anomaly_data.csv"
    caminho_saida = r"C:\Users\Geovanna\Downloads\equipment_anomaly_tratado.csv"
    
    colunas_obrigatorias = ["temperature", "pressure", "vibration", "humidity", "equipment", "location", "faulty"]
    
    
    carregador = CarregadorCSV(caminho_entrada, colunas_obrigatorias)
    df_bruto = carregador.carregar()
    
   
    df_processado = (
        ___(df_bruto)                #
        .padronizar_colunas()
        .remover_nulos(subset=colunas_obrigatorias)
        .obter_dados()
    )
    
    df_processado = (
        ___(df_processado)          
        .converter_tipos_numericos()
        .obter_dados()
    )
    
    df_final = (
        ___(df_processado)          
        .adicionar_alerta_temperatura(limite_maximo=80.0)
        .obter_dados()
    )
    
    
    exportador = ExportadorCSV(df_final)
    exportador.salvar(caminho_saida)
    
    print("Pipeline executado com sucesso de ponta a ponta!")

if __name__ == "__main__":
    executar_pipeline_completo()
