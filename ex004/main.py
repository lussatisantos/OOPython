class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * percentual / 100)

    # Getter
    @property
    def preco(self):
        return self._preco

    #Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('AOA', ''))
        self._preco = valor

p1 = Produto('Camisa', 2500)
p1.desconto(7)
print(p1.nome, p1.preco)

p2 = Produto('Caneca', 'AOA 4500')
p2.desconto(20)
print(p2.nome, p2.preco)