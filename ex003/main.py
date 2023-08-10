from random import randint

class Pessoa:
    ano_actual = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_actual - self.idade)
    
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_actual - ano_nascimento
        return cls(nome, idade)
    
    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand

# p1 = Pessoa.por_ano_nascimento('Paulo', 2001)
p1 = Pessoa('Alberto', 1994)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
print(Pessoa.gera_id())