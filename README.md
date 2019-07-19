# Instalação

1. Clone o repositório
```
git clone https://github.com/treborbrz/api_flask_example.git
```
2. Acesso o diretório, crie a virtualenv
```
cd api_flask_example
python3 -m venv venv
source venv/bin/activate
```
3. Instale as dependencias
```
pip install -r requirements.txt
```
4. Inice o banco
```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```
5. Inice a API
```
python run.py
```