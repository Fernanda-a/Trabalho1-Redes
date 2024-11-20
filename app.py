from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def enter(ev):
    if ev.key == "Enter":
        msg = self.brython.document['messageInput'].value      

        while True:                       
            if msg == '1':
                return render_template('signUp.html')
            elif msg == '2':
                return render_template('login.html')
            elif msg == '3':
                return render_template('message.html')
            elif msg == '0':
                print("Encerrando o cliente.")
                return render_template('/')
            else:
                print("Opção inválida. Tente novamente.")

def click(ev):
    if ev.target.id == "sendButton":
        msg = self.brython.document['messageInput'].value      

        while True:                       
            if msg == '1':
                return render_template('signUp.html')
            elif msg == '2':
                return render_template('login.html')
            elif msg == '3':
                return render_template('message.html')
            elif msg == '0':
                print("Encerrando o cliente.")
                return render_template('/')
            else:
                print("Opção inválida. Tente novamente.")


@app.route("/signup", methods=['POST', 'GET'])

@app.route("/login", methods=['POST', 'GET'])

@app.route("/messages")
