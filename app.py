# Usando framework Flask para criar uma API RESTful
# passo1: pip install flask no terminal
# passo2: importar o flask
from flask import Flask

# passo3: criar uma instancia da classe Flask
app = Flask(__name__) #instanciando a classe Flask


# passo4: criar uma rota para a API
@app.route("/")
def index():
    return "Hello World!"

#segunda rota que retorna um json
@app.route("/status/")
def homepage():
    # {"status":"OK"}
    return {"status":"OK"}

#terceira rota que retorna um texto + parâmetros
@app.route("/hello/<name>")
def hello_name(name):
    return f'Hello {name}!'

@app.route("/soma/<int:n1>/<int:n2>")
def soma(n1,n2):
    return (f'Soma de {n1} com {n2}: {n1+n2}')

# passo5: executar a aplicação
if __name__ == "__main__":
    app.run() 

'''
cmd:
\> pip install requests
\>python
>>>import requests
>>>response = requests.get('http://127.0.0.1:5000')
>>>response.text (deve retorna 'Hello World!')
'''