class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * percentual / 100)

p1 = Produto('Camisa', 2500)
p1.desconto(7)
print(p1.preco)

p2 = Produto('Caneca', 4500)
p2.desconto(20)
print(p2.preco)