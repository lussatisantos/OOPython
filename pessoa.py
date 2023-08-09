class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} ja esta comendo')
            return
        print(f'{self.nome} esta comendo {alimento}')
        self.comendo = True
    
    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} nao esta comendo')
            return
        print(f'{self.nome} nao parou de comer')
        self.comendo = False