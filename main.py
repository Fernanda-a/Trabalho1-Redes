#from gepeto2 import enviar_dados
class DefaultPage:
    PAGES = dict()

    def __init__(self, brython):
        self.brython = brython
        self.page = self.chat()
        #[item.bind("click", self.link) for item in self.items]

    def show(self):
    # Primeiro ela limpa o HTML
        self.brython.document["changingPart"].html = ""
        # Depois bota a página como filho da div pydiv
        _ = self.brython.document["changingPart"] <= self.page

    def build_body(self):
        return ()
    
    def chat(self):
        h = self.brython.html
        cnt = h.DIV(self.build_body())
        return cnt

        
class OptionsPage(DefaultPage):
    def __init__(self, brython):
        super().__init__(brython)

# Executa a função principal quando o script é iniciado
        if __name__ == "__main__":
            main()

    def build_body(self):
        def enter(ev):
            if ev.key == "Enter":
                msg = self.brython.document['messageInput'].value      
        
                while True:                       
                    if msg == '1':
                        return SignUpPage(self.brython).show()                
                    elif msg == '2':
                        return LoginPage(self.brython).show()
                    elif msg == '3':
                        return MessagePage(self.brython).show()
                    elif msg == '0':
                        print("Encerrando o cliente.")
                        return OptionsPage(self.brython).show()
                    else:
                        print("Opção inválida. Tente novamente.")

        def click(ev):
            if ev.target.id == "sendButton":
                msg = self.brython.document['messageInput'].value      
        
                while True:                       
                    if msg == '1':
                        return SignUpPage(self.brython).show()                
                    elif msg == '2':
                        return LoginPage(self.brython).show()
                    elif msg == '3':
                        return MessagePage(self.brython).show()
                    elif msg == '0':
                        print("Encerrando o cliente.")
                        return OptionsPage(self.brython).show()
                    else:
                        print("Opção inválida. Tente novamente.")

        h = self.brython.html
        inf = h.DIV("", Class="informationModal container is-flex is-justify-content-center is-align-items-center")
        
        tit = h.P("Escolha uma das opções", Class="title", style={'textShadow':'0.3rem 0rem 0.2rem black'})
        tex = h.P("1 - Criar usuário <br> 2 - Login <br> 3 - Enviar mensagens <br> 0 - Sair", Class="informationModal is-size-5 has-text-weight-bold",  style={'color':'white', 'textShadow':'0.3rem 0rem 0.2rem black'})
        inpdiv = h.DIV("", Class="is-flex is-justify-content-spa ce-between is-absolute mt-6", style={'position': 'fixed', 'bottom': '7%', 'right': '19%', 'width': '58rem'})

        inp = h.INPUT(type="text", Id="messageInput", Class="input is-rounded mr-2", placeholder="Escolha uma opção...")
        inpbut = h.BUTTON("Send", type="button", Id="sendButton", Class="button is-rounded")

        inpbut.bind("click", click)  
        inp.bind("keydown", enter)      

        inpdiv <= ((inp, inpbut))
        return (tit, inf, tex, inpdiv)
    
class SignUpPage(DefaultPage):
    #the client must be created and verified with this page :)
    def __init__(self, brython):
        super().__init__(brython)

    def click(self, ev=None):
        doc = self.brython.document
        username = doc["username"].value
        password = doc["password"].value

        dados = {
        "flag": 3,
        "User": username,
        "Pass": password
        }        
        return LoginPage(self.brython).show()
    
    def build_body(self):   
        h = self.brython.html
        tit = h.P("CADASTRO", Class="title", style={'textShadow':'0.3rem 0rem 0.2rem black'})
        inpdiv = h.DIV("", Class="messageInput is-justify-content-space-between is-absolute", style={'width': '40rem'})
        usr = h.INPUT(type="text",Id="username", Class="input is-rounded mr-2", placeholder="Nome de usuário")
        pas = h.INPUT(type="text",Id="password", Class="input is-rounded mr-2 mt-4", placeholder="Sua senha")
        inpbut = h.BUTTON("Send", type="button",Id="sendButton", Class="button is-rounded mt-4")

        inpbut.bind("click", self.click)
        inpdiv <= ((tit, usr, pas, inpbut))
        return (inpdiv)
    
class LoginPage(DefaultPage):
    def click(self, ev=None):
        doc = self.brython.document
        username = doc["username"].value
        password = doc["password"].value

        dados = {
        "flag": 0,
        "User": username,
        "Pass": password
        }

        return MessagePage(self.brython).show() 

    def build_body(self):
        h = self.brython.html
        tit = h.P("LOGIN", Class="title", style={'textShadow':'0.3rem 0rem 0.2rem black'})
        inpdiv = h.DIV("", Class="messageInput is-justify-content-space-between is-absolute", style={'width': '40rem'})
        usr = h.INPUT(type="text",Id="username", Class="input is-rounded mr-2", placeholder="Nome de usuário")
        pas = h.INPUT(type="text",Id="password", Class="input is-rounded mr-2 mt-4", placeholder="Senha")
        inpbut = h.BUTTON("Send", type="button",Id="sendButton", Class="button is-rounded mt-4")

        input.bind("click", self.click)

        inpdiv <= ((tit, usr, pas, inpbut))
        return (inpdiv)        
    
class MessagePage(DefaultPage):
    def __init__(self, brython):
        super().__init__(brython)

    def build_body(self):
        def click(self, ev=None):
            doc = self.brython.document
            remetente = doc["username"].value
            destinatario = doc["destiny"].value
            conteudo_email = doc["message"].value

            dados = {
            "flag": 1,
            "User": remetente,
            "User": remetente,
            "destinatario": destinatario,
            "conteudo_email": conteudo_email
            }
            

        h = self.brython.html
        inpdiv = h.DIV("", Class="messageInput is-absolute", style={'position': 'fixed', 'top': '18%', 'left': '21%', 'width': '25rem'})
        usr = h.INPUT(type="text",Id="username", Class="disabled input is-rounded", placeholder="Usuário...") #botar o nome que a pessoa usou no login
        des = h.INPUT(type="text",Id="destiny", Class="input is-rounded ml-2", placeholder="Destinatário...")
        udd = h.DIV("", Class="is-flex")
        udd <= ((usr, des))
        msgdiv = h.DIV("", Class="is-flex is-align-items-center", style={'position': 'fixed', 'bottom': '7%', 'right': '20%', 'width': '58rem'})
        msg = h.INPUT(type="text",Id="message", Class="input is-rounded ml-3", placeholder="Mensagem...")
        inpbut = h.BUTTON("Send", type="button",Id="sendButton", Class="button is-rounded ml-2")

        inpbut.bind("click", click)

        msgdiv <= ((msg, inpbut))
        inpdiv <= ((udd, msgdiv))
        wrp = h.DIV("", Class='')
        wrp <= ((inpdiv, msgdiv))
        return (wrp)
    
class Site:
    def __init__(self, br):
        self.brython = br

    def start(self):
        br = self.brython

        _main = OptionsPage(br)
        _main.show()
        return _main


def main(br):
    return Site(br).start()