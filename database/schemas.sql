CREATE SCHEMA IF NOT EXISTS bronze;
CREATE SCHEMA IF NOT EXISTS silver;
CREATE SCHEMA IF NOT EXISTS gold;

CREATE TABLE IF NOT EXISTS bronze.previsoes_raw (
    id BIGSERIAL PRIMARY KEY,
    coletado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    latitude NUMERIC(10,6) NOT NULL,
    longitude NUMERIC(10,6) NOT NULL,
    dados JSONB NOT NULL
);

CREATE TABLE IF NOT EXISTS silver.previsoes_diarias (
    id BIGSERIAL PRIMARY KEY,
    latitude NUMERIC(10,6) NOT NULL,
    longitude NUMERIC(10,6) NOT NULL,
    data DATE NOT NULL,
    timezone VARCHAR(100),
    temp_max NUMERIC(6,2),
    temp_min NUMERIC(6,2),
    sens_max NUMERIC(6,2),
    sens_min NUMERIC(6,2),
    vento_max NUMERIC(8,2),
    nascer TIMESTAMP,
    por_sol TIMESTAMP,
    luz_dia NUMERIC(12,2),
    luz_sol NUMERIC(12,2),
    uv_max NUMERIC(6,2),
    criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    atualizado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uq_silver_local_data UNIQUE (latitude, longitude, data)
);

CREATE TABLE IF NOT EXISTS gold.indicadores_clima (
    id BIGSERIAL PRIMARY KEY,
    latitude NUMERIC(10,6) NOT NULL,
    longitude NUMERIC(10,6) NOT NULL,
    data DATE NOT NULL,
    temperatura_media NUMERIC(6,2),
    amplitude_termica NUMERIC(6,2),
    sensacao_media NUMERIC(6,2),
    vento_max NUMERIC(8,2),
    uv_max NUMERIC(6,2),
    criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    atualizado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uq_gold_local_data UNIQUE (latitude, longitude, data)
);

CREATE INDEX IF NOT EXISTS idx_bronze_coletado_em
    ON bronze.previsoes_raw (coletado_em);

CREATE INDEX IF NOT EXISTS idx_silver_data
    ON silver.previsoes_diarias (data);

CREATE INDEX IF NOT EXISTS idx_gold_data
    ON gold.indicadores_clima (data);
