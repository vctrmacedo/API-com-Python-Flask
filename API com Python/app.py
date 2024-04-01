from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'nome': 'As 48 leis do poder',
        'autor': 'Robert Greene'
    },
    {
        'id': 2,
        'nome': 'Pense em Python',
        'autor': 'Allen B. Downey'
    },
    {
        'id': 3,
        'nome': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K Howling'
    }
]

#Página Inicial
@app.route('/')
def home():
    return 'Olá, essa é a página inicial da API'

#Consultar todos os livros
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

#Obter Livro por id
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livros_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

#Editar Livro por id
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
        
#Adicionar um livro
@app.route('/livros', methods=['POST'])
def adicionar_novo_livro():
   novo_livro = request.get_json()
   livros.append(novo_livro)
   return jsonify(livros)

#Excluir livro
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)

    
####### Exemplos de como criar uma API, aqui eu poderia ter feito a conexão com algum banco de dados, porém usei o próprio python. #####

app.run(port=5000, host='localhost', debug=True)