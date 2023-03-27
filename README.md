# Pré-requisitos
**Antes de começar, certifique-se de ter o seguinte software instalado em seu sistema:**

Docker

Docker Compose

Python 3.8 ou superior

pip (gerenciador de pacotes Python)

# Início

**Clone o repositório:**

git clone https://github.com/seuusername/desafio-dev.git

cd desafio-dev

**Instale os pacotes Python necessários:**

pip install -r requirements.txt

**Construa e execute os containers Docker usando o Docker Compose:**

docker-compose build

docker-compose up

**A aplicação FastAPI estará disponível em http://localhost:8000 e o banco de dados PostgreSQL será executado na porta 5432.**


# Endpoints
A aplicação fornece os seguintes endpoints:

POST /upload-cnab: Faz o upload de um arquivo CNAB e armazena seu conteúdo no banco de dados.


# Documentação da API
A documentação da API está disponível em http://localhost:8000/docs quando a aplicação estiver em execução.

# Executando Testes
Para executar a suíte de testes, execute o seguinte comando:

pytest