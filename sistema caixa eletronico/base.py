from datetime import datetime

horario = datetime.now()
hora = horario.hour

class Conta():
    def __init__(self, nome, cpf, senha):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.saldo = 0

    def criar__conta(self, nome, cpf, senha):
        return Conta(nome, cpf, senha)

    def deposito(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        self.saldo -= valor
    
    def mostrar_saldo(self):
        print(f"Saldo: R$ {self.saldo}")

contas = {}

contas['12345678'] = Conta('Alberto', '12345678', '4321')

tentativas = 0

while tentativas <= 3:
    try:
        print('''
        1 - Criar conta
        2 - Entrar
        3 - Sair
    ''')

        escolha = int(input('Escolher: '))

        if escolha == 1:
            nome = input('Digite seu nome: ').lower()
            if nome.isdigit():
                print('Nome inválido')
                continue

            cpf = input('Digite um cpf válido: ')
            if len(cpf) < 8 or not cpf.isdigit():
                print('CPF Inválido')
                continue

            senha = input('Crie uma senha: ')
            if len(senha) != 4 or not senha.isdigit():
                print('Senha inválida')
                continue

            if cpf in contas:
                print('Conta já existe')
            else:
                contas[cpf] = Conta(nome, cpf, senha)
                print('Conta criada com sucesso!')

        elif escolha == 2:
            cpf_teste = input('Digite seu CPF: ')
            if cpf_teste not in contas:
                print('Conta não existe')
                continue
            
            conta = contas[cpf_teste]
            senha = input('Digite sua senha: ')
        
            if senha == conta.senha:
                while True:
                    print(f'''
                Bem vindo ao Banco! {horario.strftime("%H:%M:%S")}
                        
                    1 - Ver saldo
                    2 - Depositar
                    3 - Sacar
                    4 - Voltar        
                ''')
                    opcao = int(input('Escolher: '))
                    
                    if opcao == 1:
                        conta.mostrar_saldo()

                    elif opcao == 2:
                        quantidade = int(input('Digite o valor do deposito: '))
                        conta.deposito(quantidade)
                        print('Depósito realizado com sucesso!')

                    elif opcao == 3:
                        quantidade = int(input('Digite o valor do saque: '))
                        if 0 < quantidade <= conta.saldo:
                            conta.sacar(quantidade)
                            print('Saque realizado com sucesso!')
                        else:
                            print('Valor inválido')

                    elif opcao == 4:
                        break
            
            else:
                print('Senha incorreta')
                tentativas += 1

        elif escolha == 3:
            if hora < 13:
                print('Tenha um bom dia!')
            elif hora < 18:
                print('Tenha uma boa tarde!')
            else:
                print('Tenha uma boa noite!')
            break

    except:
        print('Código de segurança violado!')
