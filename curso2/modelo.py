class Programa:
    def __init__(self,nome,ano):
        self._nome=nome.title()
        self.ano=ano  
        self._likes=0

    def dar_like(self):
        self._likes+=1

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome.title()
        
    @nome.setter
    def nome(self,nome):
        self._nome=nome

    def __str__(self):
        return f'nome : {self.nome}, ano: {self.ano}, likes: {self.likes}'



class Filme(Programa):
    def __init__(self,nome,ano,duracao):
        super().__init__(nome,ano)
        self.duracao=duracao
    def __str__(self):
        return 'Filme\n'+ super().__str__()+f', duracao: {self.duracao} minutos\n'



class Serie(Programa):
    def __init__(self,nome,ano,temporadas):
        super().__init__(nome,ano)
        self.temporadas=temporadas
    def __str__(self):
        return 'Serie\n'+ super().__str__()+f', temporadas: {self.temporadas}\n'


class Playlist:
    def __init__(self,nome,programas):
        self.nome=nome
        self._programas=programas
    
    def __getitem__(self,item):
        return self._programas[item]
    

    def __len__(self):
        return len(self._programas)

    
        


f1=Filme('vingadores',2019,160)
f1.dar_like()
f1.nome='Luca'
s1=Serie('modern family',2019,11)
s1.dar_like()
f2=Filme('everest',2006,100)
s2=Serie('death note',2015,1)



filmes_series=[f1,s1,f2,s2]
fds=Playlist('fim de semana ',filmes_series)


print(len(fds))
for programa in fds:
    print(programa)
    


# Inicialização	__init__
# Representação	__str__, __repr__
# Container, sequência	__contains__, __iter__, __len__, __getitem__
# Numéricos	__add__, __sub__, __mul__, __mod__