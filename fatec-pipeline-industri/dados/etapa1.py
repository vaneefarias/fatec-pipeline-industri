from abc import ABC, abstractmethod
from pathlib import Path
import pandas as pd

class CarregadorBase(ABC):
    def __init__(self, caminho, colunas_obrigatorias=None):
        self.caminho = Path(caminho)
        self.colunas_obrigatorias = colunas_obrigatorias or []
        
    @abstractmethod
    def _ler(self):
        """Método abstrato que será implementado na subclasse."""
        pass
        
    def carregar(self):
        """Orquestra a verificação de existência e leitura do ficheiro."""
        if not self.caminho.exists():
            raise FileNotFoundError(f"O ficheiro não foi encontrado em: {self.caminho}")
            
        df = self._ler()
        
        # Correção aplicada aqui: utilizando a subtração de conjuntos (-)
        faltantes = set(self.colunas_obrigatorias) - set(df.columns)
        if faltantes:
            raise ValueError(f"Colunas obrigatórias em falta no ficheiro: {faltantes}")
            
        print(f"Carga concluída com sucesso! Dimensões: {df.shape}")
        return df

class CarregadorCSV(CarregadorBase):
    def __init__(self, caminho, colunas_obrigatorias=None):
        super().__init__(caminho, colunas_obrigatorias)
        
    def _ler(self):
        return pd.read_csv(self.caminho)