1. Clone o repositório
```
https://github.com/treborbrz/api_flask_example.git
```
1. Acesso o diretório, crie a virtualenv
```
cd api_flask_example
python3 -m venv venv
source venv/bin/activate
```
1. Instale as dependencias
```
pip install -r requirements.txt
```
1. Inice o banco
```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```
1. Inice a API
```
python run
```