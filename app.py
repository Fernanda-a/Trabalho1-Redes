from flask import Flask, render_template, request, flash, jsonify,redirect
from gepeto2 import enviar_dados

app = Flask(__name__)
app.config["SECRET_KEY"] = "8jUCWYBssHyW72CkhmEWOw"

@app.route("/", methods = ["POST", "GET"])
def home():   
        if request.method == 'POST':
            msg = request.form.get('optionsInput')
                           
            if msg == '1':
                return redirect("/signup")
            elif msg == '2':
                return redirect("/login")
            elif msg == '3':
                return redirect("/messages")
            elif msg == '0':
                return redirect("/")
            else:
                print("Opção inválida. Tente novamente.")
                return render_template('index.html')
        else:
             return render_template('index.html')
            
@app.route("/signup", methods=['POST', 'GET'])
def criar_usuario():
    if request.method == 'POST':
        data = request.form
        nickname = data.get("User")
        senha = data.get("Pass")
        dados = {"flag": 3, "User": nickname, "Pass": senha}

        response = enviar_dados(dados)
        print(response)

        if (response):
            flash('User Created!', category='error')
            return redirect("/login")
        else:
            flash('Error. Try again.', category='error')
            return render_template('signUp.html')
    else:
        return render_template('signUp.html')

@app.route("/login", methods=['POST', 'GET'])
def autenticar_usuario():
    if request.method == 'POST':
        data = request.form
        nickname = data.get("User")
        senha = data.get("Pass")
        dados = {"flag": 0, "User": nickname, "Pass": senha}

        response = enviar_dados(dados)
        print(response)

        if (response):
            return redirect("/messages")
        else:
            flash('Error. Cant authenticate. Try again.', category='error')
            return render_template('login.html')

    else:
        return render_template("login.html")

@app.route("/messages", methods=['POST', 'GET'])
def enviar_mensagem():
    if request.method == 'POST':
        data = request.form
        remetente = data.get("remetente")
        destinatario = data.get("destinatario")
        conteudo_email = data.get("messageInput")
        dados = {"flag": 1, "User": remetente, "destinatario": destinatario, "conteudo_email": conteudo_email}
        response = enviar_dados(dados)

        if (response):
            return jsonify(enviar_dados(dados))
        else:
            flash('Error. Cant authenticate. Try again.', category='error')
            return render_template('messages.html')
    
    else:
        return render_template('messages.html')
