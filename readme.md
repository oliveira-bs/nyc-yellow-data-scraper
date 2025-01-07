# NYC Yellow Data Scraper

See [readme_english](./readme_english.md)

## Objetivo
O projeto **NYC Yellow Data Scraper** tem como propósito principal extrair, filtrar e organizar dados relacionados ao registro de viagens dos táxis amarelos disponíveis no site oficial da NYC TLC (Taxi and Limousine Commission).  
Esses dados são cruciais para análises futuras e previsões de comportamento do serviço, contribuindo para o entendimento de padrões de transporte e melhorias no planejamento urbano. Além disso, o projeto fornece uma base estruturada para estudos preditivos e iniciativas de data-driven decision-making.

---

## Pré-requisitos
Para executar o projeto com sucesso, é necessário garantir que os seguintes itens estejam configurados no ambiente:

1. **Python 3.8+** instalado e configurado.
2. **Bibliotecas Python necessárias** listadas no arquivo `requirements.txt`.
3. **Scrapy** devidamente instalado.
4. Configuração de uma pasta local para armazenar os dados extraídos.

---

## Comandos Básicos
Execute os seguintes comandos no terminal para rodar o projeto:

1. Instale as dependências do projeto:  
   ```
   pip install -r requirements.txt
   ```

2. Navegue até o diretório do projeto Scrapy:  
   ```
   cd yellow_tlc
   ```

3. Execute o crawler com a seguinte linha de comando:  
   ```
   scrapy crawl yellow_tripdata
   ```

Para configurar datas específicas ou alterar a pasta de destino dos downloads, personalize as variáveis no arquivo `settings.py` ou passe argumentos ao executar o crawler.

---

## Estrutura de Diretórios
Abaixo está a estrutura do projeto Scrapy:

```
yellow_tlc/
├── landing/                # Diretório para armazenar os arquivos extraídos
├── spiders/                # Diretório contendo os arquivos dos spiders
│   └── yellow_tripdata.py  # Spider principal para extração dos dados
│   └── ...                 # Outros arquivos nativos do Scrapy
│   └── settings.py         # Configurações do Scrapy
├── scrapy.cfg               
├── readme.md               
├── readme_english.md               
└── requirements.txt        # Bibliotecas necessárias
```

---

## Controle de Requisições
O seguinte trecho de código no arquivo `settings.py` foi implementado para gerenciar as requisições do crawler:

```python
# Configuração para evitar sobrecarga do servidor
DOWNLOAD_DELAY = 2  # Define um atraso de 2 segundos entre as requisições
AUTOTHROTTLE_ENABLED = True  # Habilita o controle automático de requisições
AUTOTHROTTLE_START_DELAY = 1  # Atraso inicial para o autotrottle
AUTOTHROTTLE_MAX_DELAY = 10  # Máximo atraso entre requisições
```

### Impacto
Essa configuração reduz a frequência de requisições consecutivas, ajudando a evitar bloqueios e garantindo que o servidor-alvo seja respeitado.

---

## Conclusão e Flexibilidade
O projeto **NYC Yellow Data Scraper** oferece uma abordagem robusta e configurável para extração de dados dos táxis amarelos de Nova York. O crawler foi projetado para permitir a customização de variáveis importantes, como `start_urls`, `start_date`, `end_date`, e `landing_dir` diretamente no crawler.  

Além disso, o projeto pode ser facilmente integrado a pipelines de automação, como aqueles orquestrados pelo **Apache Airflow**, tornando-o uma ferramenta poderosa e flexível para aplicações de grande escala.
