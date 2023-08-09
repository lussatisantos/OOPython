from pessoa import Pessoa
from datetime import date

p1 = Pessoa('Lussati', 20)
p2 = Pessoa('Santos', 19)


p1.falar('Geopolitica internacional')
p2.falar('POO')


print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())