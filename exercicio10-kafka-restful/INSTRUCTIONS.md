Faça uso dos dois paradigmas de interação (pub-sub e cliente-servidor) para implementar um sistema mínimo onde os eventos produzidos, consumidos e processados pelos produtores/consumidores sejam utilizados para "povoar" dados em um serviço, o qual pode ser consultado por clientes. Utilize Kafka para pub-sub e RESTful para cliente/servidor (web service).

### Arquitetura geral:

(1) produtor → (2) consumidor/produtor → (3) consumidor/web service ↔ (4) cliente

### Cenário:

1. Eventos são produzidos por um sensor (ex.: leituras de temperatura sempre que ocorre uma variação significativa)
2. Eventos são processados para produzir alguma nova informação (ex.: temperatura média nas últimas 2 horas)
3. Informações produzidas são armazenadas em uma base de dados
4. Clientes fazem consultas para obter as últimas informações, informações históricas etc.

Obs.: sensores simulados.