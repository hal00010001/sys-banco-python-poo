from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(conta: Conta, transacao: Transacao):
        transacao.registrar(conta)

    def adicionar_conta(conta: Conta):
        self.contas.append(conta)

class Historico:
    def adicionar_transacao(transacao: Transacao):
        pass

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def saldo():
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        return True

    def nova_conta(cliente: Cliente, numero: int):
        cpf = input("Informe o CPF do cliente que deseja uma nova conta corrente: ")
        cliente = selecionar_cliente(cpf, clientes)

        if cliente:
            print("Conta cadastrada com sucesso!")
            # return {"agencia": agencia, "codigo_conta": codigo_conta, "cliente": cliente}
            return Conta
        
        print("Cliente não encontrado!")    

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")
            return True
        else:
            print("Operação falhou! O valor informado é inválido.")
            
        return False

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            # extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")            
        else:
            print("Operação falhou! O valor informado é inválido.")
            return False
        return True

class ContaCorrente(Conta):
    _limite: float
    _limite_saques: int

class Transacao(ABC):
    def registrar(conta: Conta):
        pass

class Saque(Transacao):
    pass

class Deposito(Transacao):
    pass





saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"
clientes = []
contas = []
codigo_conta = 1

def menu():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [c] Cadastrar cliente
    [k] Cadastrar conta corrente
    [q] Sair

    => """
    return input(menu)


def depositar(saldo, valor, extrato, /):

    


def sacar(*, saldo, valor, limite, extrato, numero_saques, limite_saques):

    

def mostrar_extrato(saldo, /, *, extrato):


def cadastrar_cliente(clientes):
    cpf = input("Informe o CPF somente com números: ")
    cliente = selecionar_cliente(cpf, clientes)

    if cliente:
        print("Este CPF já pertence a um cliente cadastrado")
        return
    
    nome = input("Informe o nome do novo cliente: ")
    nascimento = input("Informe sua data de nascimento no formato ddmmaaaa: ")
    endereco =input("Informe seu endereço completo, contendo rua, número, bairro, cidade e sigla do estado: ")

    clientes.append({"nome": nome, "nascimento": nascimento, "cpf": cpf, "endereco": endereco})
    print("Cliente cadastrado com sucesso!")

def selecionar_cliente(cpf, clientes):    
    lista_clientes = [cliente for cliente in clientes if cliente["cpf"] == cpf]
    return lista_clientes[0] if lista_clientes else None

def cadastrar_nova_conta(agencia, codigo_conta, clientes):
    cpf = input("Informe o CPF do cliente que deseja uma nova conta corrente: ")
    cliente = selecionar_cliente(cpf, clientes)

    if cliente:
        print("Conta cadastrada com sucesso!")
        return {"agencia": agencia, "codigo_conta": codigo_conta, "cliente": cliente}
    
    print("Cliente não encontrado!")



while True:

    opcao = menu()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato = sacar(saldo=saldo, valor=valor, limite=limite, extrato=extrato, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
    
    elif opcao == "e":        
        mostrar_extrato(saldo, extrato=extrato)

    elif opcao == "c":        
        cadastrar_cliente(clientes=clientes)

    elif opcao == "k":        
        conta = cadastrar_nova_conta(agencia=AGENCIA, codigo_conta=codigo_conta, clientes=clientes)
        if conta:
            contas.append(conta)
            codigo_conta += 1

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")