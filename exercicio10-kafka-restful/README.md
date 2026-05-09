[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wWsgWD6e)

## Estrutura do Projeto

- `src/sensor.py`: Produtor de eventos (Sensor simulado).
- `src/processor.py`: Consumidor e Produtor (Processamento de dados).
- `src/web_service.py`: Consumidor e Servidor REST (Armazenamento e Serviço).
- `src/client.py`: Cliente REST (Consulta de dados).
- `src/const.py`: Centralização de constantes e configurações.

## Pré-requisitos

1.  **Python 3.x**
2.  **Docker & Docker Compose** (para rodar o Kafka).

## Configuração

O projeto utiliza variáveis de ambiente para configuração, definidas no arquivo `.env` na raiz:

- `KAFKA_BOOTSTRAP_SERVERS`: Endereço do broker Kafka (`ex: localhost:9092`).
- `REST_SERVER_ADDRESS`: Endereço do servidor REST (`ex: localhost:8000`).

## Como Executar Localmente

### 1. Iniciar o Kafka (via Docker Compose)

Suba o broker Kafka utilizando o Docker Compose:
```bash
docker-compose up -d
```

### 2. Preparar o Ambiente Python

Ative o ambiente virtual e instale as dependências:
```bash
.\venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Executar os Componentes

Abra 4 terminais diferentes e execute cada script na ordem abaixo:

- **Terminal 1 (Web Service):** Armazena dados e provê a API REST.
  ```bash
  python src/web_service.py
  ```
- **Terminal 2 (Processor):** Processa médias de temperatura.
  ```bash
  python src/processor.py
  ```
- **Terminal 3 (Sensor):** Gera dados simulados.
  ```bash
  python src/sensor.py
  ```
- **Terminal 4 (Client):** Consulta os resultados via REST.
  ```bash
  python src/client.py
  ```

## Fluxo de Dados

1. `sensor.py` gera temperaturas aleatórias e envia para o tópico `raw_temperature`.
2. `processor.py` consome do `raw_temperature`, calcula a média das últimas 5 leituras e envia para `processed_temperature`.
3. `web_service.py` consome do `processed_temperature`, salva no banco SQLite (`temperature.db`) e disponibiliza via REST na porta `8000`.
4. `client.py` faz requisições HTTP para obter a última temperatura e o histórico.
