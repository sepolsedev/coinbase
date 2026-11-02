# Coinbase — Pipeline ETL de Dados Meteorológicos

Projeto acadêmico em Python para coleta de dados meteorológicos da API Open-Meteo e processamento em arquitetura Bronze, Silver e Gold, com persistência em PostgreSQL.

## Estrutura

- `app/extract`: coleta dados da API Open-Meteo.
- `app/load`: salva a camada Bronze em JSON e grava dados no PostgreSQL.
- `app/transform`: transforma dados para as camadas Silver e Gold e orquestra a pipeline.
- `config`: configurações da aplicação e conexão com o banco.
- `database`: script SQL para criação dos schemas e tabelas.
- `data/bronze`: arquivos JSON brutos gerados localmente.
- `data/silver` e `data/gold`: diretórios reservados para as camadas; nesta versão, os dados tratados são persistidos no PostgreSQL.

## Camadas

### Bronze
Mantém os dados brutos retornados pela API e também registra o JSON no schema `bronze`.

### Silver
Normaliza os dados meteorológicos diários e grava em `silver.previsoes_diarias`.

### Gold
Calcula indicadores derivados, como temperatura média, amplitude térmica e sensação térmica média, gravando em `gold.indicadores_clima`.

## Instalação

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Copie `.env.example` para `.env` e informe a senha do PostgreSQL.

Crie o banco `clima` e execute `database/schemas.sql`.

Depois rode:

```bash
python main.py
```
