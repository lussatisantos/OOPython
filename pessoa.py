class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} nao pode falar comendo')
            return
        
        if self.falando:
            print(f'{self.nome} ja esta falando')
            return
        
        print(f'{self.nome} esta falando')
        self.falando = True

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
        print(f'{self.nome} parou de comer')
        self.comendo = False