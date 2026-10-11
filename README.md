```markdown
# 🚀 Pipeline ETL Orientado a Objetos para Análise de Anomalias em Equipamentos

> Um projeto de engenharia de dados robusto, desenvolvido com foco em modularidade, boas práticas de Clean Code e Programação Orientada a Objetos (POO) em Python.

---

## 📌 Sobre o Projeto
Este repositório apresenta a implementação de um pipeline de dados do tipo **ETL (Extract, Transform, Load)** de ponta a ponta, estruturado para processar o dataset real `equipment_anomaly_data.csv`. 

O objetivo principal foi abandonar scripts procedurais lineares e construir uma arquitetura limpa, escalável e de fácil manutenção, separando cada fase do processamento de dados em classes independentes e reutilizáveis.

---

## 🛠️ Arquitetura e Engenharia de Software
O projeto foi construído seguindo princípios estritos de engenharia de software:
- **Programação Orientada a Objetos (POO):** Encapsulamento de responsabilidades em classes dedicadas.
- **Method Chaining (`return self`):** Permite o encadeamento fluído de métodos de limpeza e transformação.
- **Validação de Schema:** Verificação rigorosa de colunas obrigatórias e tipos de dados no carregamento.
- **Engenharia de Atributos:** Criação de regras de negócio dinâmicas (ex: alertas de temperatura crítica).

---

## 📂 Estrutura do Pipeline (Módulos)

O fluxo de dados está dividido em etapas modulares e orquestradas por um script central (`main.py`):

1. **`CarregadorCSV`**: Responsável pela leitura segura do ficheiro bruto e validação de schema.
2. **`LimpadorDados`**: Padroniza nomes de colunas e remove valores nulos utilizando *method chaining*.
3. **`TransformadorDados`**: Converte e padroniza os tipos de dados numéricos essenciais (`float`/`int`).
4. **`RegrasNegocio`**: Aplica regras específicas de domínio (como a criação de bandeiras lógicas de anomalia por temperatura).
5. **`ExportadorCSV`**: Persiste os dados limpos e tratados num novo ficheiro pronto para consumo (`equipment_anomaly_tratado.csv`).

---

## 💻 Como Executar o Projeto

1. Clone o repositório na sua máquina:
   ```bash
   git clone [https://github.com/vaneefarias/fatec-pipeline-industri.git](https://github.com/vaneefarias/fatec-pipeline-industri.git)

```

2. Certifique-se de ter o Python e a biblioteca `pandas` instalados:
```bash
pip install pandas

```


3. Ajuste os caminhos de entrada e saída no ficheiro `main.py` e execute o pipeline:
```bash
python main.py

```



---

## 🎯 Objetivo Profissional

Projeto desenvolvido como parte da jornada em **Big Data para Indústria**, unindo conceitos de engenharia de dados, qualidade de software e automação de processos analíticos.

```


```
