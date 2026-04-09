# Portfolio API

Esta é uma API RESTful desenvolvida em **Django** e **Django REST Framework (DRF)** para servir os dados de um portfólio de desenvolvedor. A API gerencia projetos categorizados em três áreas distintas (Frontend, Backend e Fullstack) e os associa às tecnologias utilizadas.

## 🚀 Funcionalidades

- **Gerenciamento de Tecnologias**: Cadastro centralizado de tecnologias (model `techs`), que podem ser associadas a diferentes projetos.
- **Divisão de Projetos**: Os projetos são separados em três aplicativos distintos (`frontend`, `backend` e `fullstack`), cada um com seus campos específicos (como URLs de deploy, descrição, e listas de tecnologias).
- **Relacionamentos (M2M)**: O módulo `fullstack` vai além do básico, dividindo as tecnologias aplicadas no _Front_, _Back_ ou _Em Ambos_.
- **Chaves Primárias em UUID**: Todas as tabelas do banco de dados utilizam UUID como chave primária, garantindo maior segurança nas rotas.
- **Consultas Personalizadas**: Endpoints estruturados para listar os projetos mais recentes (`/newest/`), além de rotas exclusivas para adicionar (`add/`) ou remover (`del/`) tecnologias de um projeto sem precisar enviar o payload inteiro.

## 🛡️ Autenticação e Permissões (DRF)

O projeto conta com um sistema de permissão customizado presente no `utils/permissions.py`:
- **Leitura (GET)**: Rotas públicas. Qualquer pessoa pode visualizar o portfólio.
- **Escrita (POST, PUT, PATCH, DELETE)**: Restrita exclusivamente para **Superusuários (SuperUser)** autenticados via Token.
- Para gerar o Token, basta logar via POST em `/login/`.

## 🛠️ Tecnologias Principais

- **Python** & **Django**
- **Django REST Framework** (DRF)
- **PostgreSQL** (com `psycopg2-binary`)
- Banco configurado via `dj-database-url` para fácil deploy de produção.

## 🛣️ Rotas da API (Endpoints)

Todas as requisições estão sob o prefixo configurado em `portifolio/urls.py` (geralmente `/api/`).

### Login
- `POST /login/`: Informações de login. Retorna o token DRF do admin.

### Tecnologias (`/api/techs/`)
- `GET /` - Lista as tecnologias cadastradas.
- `POST /` - Cria uma nova tecnologia 🔒.
- `GET /<uuid>/` - Detalhes da tecnologia.
- `PUT / PATCH / DELETE /<uuid>/` - Adição, alteração ou exclusão 🔒.

### Frontend (`/api/front/`)
- `GET /` - Lista todos os projetos front-end.
- `POST /` - Cria um novo projeto 🔒.
- `GET /newest/` - Retorna os projetos do mais recente para o mais antigo.
- `GET /<uuid>/` - Detalhes do projeto front-end.
- `PUT / PATCH / DELETE /<uuid>/` - Edita/Remove o projeto 🔒.
- `PATCH /add/<uuid>/` - Adiciona ID's de tecnologias a um projeto já criado 🔒.
- `PATCH /del/<uuid>/` - Remove ID's de tecnologias associadas a um projeto 🔒.

### Backend (`/api/back/`)
- `GET /` - Lista todos os projetos back-end.
- `POST /` - Cria um novo projeto 🔒.
- `GET /newest/` - Retorna os projetos mais recentes.
- `GET /<uuid>/` - Detalhes.
- `PUT / PATCH / DELETE /<uuid>/` - Edita/Remove 🔒.
- `PATCH /add/<uuid>/` - Adiciona novas tecnologias ao projeto 🔒.
- `PATCH /del/<uuid>/` - Remove tecnologias específicas 🔒.

### Fullstack (`/api/fullstack/`)
- `GET /` - Lista os projetos fullstack.
- `POST /` - Cria projeto fullstack 🔒.
- `GET /newest/` - Lista ordenado pelas datas mais recentes.
- `GET /<uuid>/` - Detalhes de um projeto.
- `PUT / PATCH / DELETE /<uuid>/` - Edita as informações/Remove o projeto 🔒.
- `PATCH /add/<uuid>/` - Adiciona tecnologias (distribuindo entre front-end, back-end ou gerais) 🔒.
- `PATCH /del/<uuid>/` - Remove essas tecnologias do projeto correspondente 🔒.

> **Legenda:** 🔒 Requer autenticação de um *Superuser*.

## ⚙️ Como rodar localmente

1. Clone o repositório.
2. Crie e ative um ambiente virtual (venv):
   ```bash
   python -m venv venv
   source venv/bin/activate  # ou no Windows: venv\Scripts\activate
   ```
3. Instale as dependências contidas no arquivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
4. Verifique as configurações de variáveis de ambiente no `settings.py` (caso precise definir credenciais de um banco de dados) e aplique as migrações:
   ```bash
   python manage.py migrate
   ```
5. Crie seu usuário administrador com Token para consumir as APIs nas ações de write:
   ```bash
   python manage.py createsuperuser
   ```
6. Inicialize o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```
A API estará acessível em `http://127.0.0.1:8000/`.