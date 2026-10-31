# Coinbase

Projeto acadêmico de engenharia de dados desenvolvido em Python para coleta, organização e armazenamento de dados climáticos obtidos por meio da API Open-Meteo.

O projeto aplica conceitos de extração e carga de dados, organização em camadas e integração com PostgreSQL.

## Objetivo

Construir uma estrutura para coleta de dados climáticos de uma API pública, preparando os dados para armazenamento, transformação e análise.

## Arquitetura do projeto

O projeto foi estruturado considerando uma arquitetura de dados em camadas:

### Bronze

Camada destinada aos dados coletados da fonte, preservando os dados com o mínimo de transformação possível.

### Prata

Camada destinada à limpeza, padronização e transformação dos dados provenientes da camada Bronze.

### Ouro

Camada destinada aos dados preparados para consultas, indicadores, análises e visualizações.

> A estrutura das camadas Prata e Ouro faz parte da arquitetura planejada do projeto. A versão atualmente publicada contém principalmente a implementação da coleta e da camada Bronze.

## Tecnologias utilizadas

- Python
- PostgreSQL
- SQL
- API Open-Meteo
- Requests
- Git
- GitHub

## Estrutura

```text
coinbase/
├── app/
│   ├── extract/
│   └── load/
├── config/
├── data/
│   └── bronze/
├── database/
│   └── schemas.sql
├── extract/
├── load/
├── .gitignore
├── main.py
└── requirements.txt
```

## Organização

`extract/` contém componentes responsáveis pela extração dos dados.

`load/` reúne componentes relacionados à carga dos dados.

`config/` concentra as configurações utilizadas pelo projeto.

`data/bronze/` representa a camada de dados brutos atualmente versionada.

`database/schemas.sql` contém a definição do esquema utilizado no banco de dados.

`main.py` funciona como ponto de entrada da aplicação.

## Configuração

As configurações sensíveis do ambiente são mantidas em um arquivo `.env`.

Por segurança, esse arquivo não é versionado no GitHub.

## Instalação das dependências

```bash
pip install -r requirements.txt
```

## Execução

```bash
python main.py
```

## Contexto acadêmico

Projeto desenvolvido durante os estudos de Ciência de Dados, aplicando conceitos de APIs, Python, PostgreSQL, SQL e pipelines de dados.

---

Desenvolvido por **Ednaldo da Silva Lopes**  
SEPOLSE Tecnologia & Soluções Digitais