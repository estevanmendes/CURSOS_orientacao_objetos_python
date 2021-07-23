def run_conta():
    from codigo1 import Conta
    c1=Conta(123,'estevan',1000,1000)
    c2=Conta(213,'elias',1000,1000)
    c2.transfere(100,c1)
    print(c1.limite)
    c1.saca(10000)
    print(c1.saldo)
    print(c1.limite)
    # print(c2,c1)
    c1._conta

def run_cliente():
    from cliente import Cliente
    c1=Cliente('estevan augusto')
    c1.nome='joao augusto'
    print(c1.nome)

run_conta()