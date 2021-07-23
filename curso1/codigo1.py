class Conta:
    def __init__(self,numero,titular,saldo,limite):
        self.__numero=numero
        self.__titular=titular
        self.__saldo=saldo
        self.__limite=limite
        self.__codigo_banco='001'

    def __str__(self):
        
        return f'\nnumero da conta :{self.__numero}\ntitular da conta : {self.__titular}\nsaldo da conta : {self.__saldo}\nlimite da conta : {self.__limite}'
        
    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular}')
    
    def deposita(self,valor):

            self.__saldo+=valor
         
    def saca(self,valor):
        if self.__pode_saca(valor):
            self.__saldo-=valor
        else:
            print(f'o valor do limite {self.__limite} e do saldo {self.__saldo}')
    
    def __pode_saca(self,valor):
        valor_disponivel=self.__limite+self.__saldo
        return valor<=valor_disponivel


    def transfere(self,valor,destino):
        self.saca(valor)
        destino.deposita(valor)
    


    @property
    def saldo(self):
        return self.__saldo
       
    @property
    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite  

    @limite.setter
    def limite(self,limite):
        self.__limite=limite

    @staticmethod
    def codigo_banco(): #metodo estatico
        return '001'