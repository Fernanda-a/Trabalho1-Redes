import socket
import json
import base64
import hashlib
from cryptography.fernet import Fernet

# Gera a chave para criptografia, que deve ser a mesma usada no servidor
KEY = base64.urlsafe_b64encode(hashlib.sha256(b'qweasd').digest())
cipher_suite = Fernet(KEY)

# Função que estabelece conexão com o servidor, envia dados criptografados e recebe uma resposta criptografada
def enviar_dados(data, host='127.10.10.1', port=7444):
    try:
        # Cria um socket TCP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            data_serializada = json.dumps(data).encode()
            encrypted_data = cipher_suite.encrypt(data_serializada)
            data_length = f"{len(encrypted_data):<10}".encode()
            client_socket.sendall(data_length + encrypted_data)
            
            encrypted_length = int(client_socket.recv(10).decode().strip())
            encrypted_response = client_socket.recv(encrypted_length)
            response_data = cipher_suite.decrypt(encrypted_response).decode()
            response = json.loads(response_data)
            
            return response
    except Exception as e:
        print("Erro na comunicação com o servidor:", e)
        return None

# Função que coleta nickname e senha do usuário e envia uma solicitação para criar um novo usuário no servidor
def criar_usuario():
    nickname = input("Digite o nome do usuário: ")
    senha = input("Digite a senha: ")
    dados = {
        "flag": 3,
        "User": nickname,
        "Pass": senha
    }
    return enviar_dados(dados)

# Função que coleta nickname e senha e envia uma solicitação de autenticação ao servidor
def autenticar_usuario():
    nickname = input("Digite o nome do usuário: ")
    senha = input("Digite a senha: ")
    dados = {
        "flag": 0,
        "User": nickname,
        "Pass": senha
    }
    return enviar_dados(dados)

# Função que coleta remetente, destinatário e conteúdo e envia uma mensagem ao servidor
def enviar_mensagem(remetente):
    remetente = input("Digite o seu nome de usuário: ")
    destinatario = input("Digite o nome do destinatário: ")
    conteudo_email = input("Digite a mensagem: ")
    dados = {
        "flag": 1,
        "User": remetente,
        "destinatario": destinatario,
        "conteudo_email": conteudo_email
    }
    return enviar_dados(dados)

# Função principal que exibe um menu de opções para o usuário interagir com o servidor
def main():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Criar usuário")
        print("2 - Autenticar usuário")
        print("3 - Enviar mensagem")
        print("0 - Sair")
        
        opcao = input("Opção: ")
        
        if opcao == '1':
            resposta = criar_usuario()
            print("Resposta do servidor:", resposta)
        elif opcao == '2':
            resposta = autenticar_usuario()
            print("Resposta do servidor:", resposta)
        elif opcao == '3':
            resposta = enviar_mensagem()
            print("Resposta do servidor:", resposta)
        elif opcao == '0':
            print("Encerrando o cliente.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa a função principal quando o script é iniciado
if __name__ == "__main__":
    main()
