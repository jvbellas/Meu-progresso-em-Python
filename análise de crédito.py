import random

class Pessoa:
    def _init_(self, idade, salario, endividamento):
        self.idade = idade
        self.salario = salario
        self.endividamento = endividamento

    def setIdade(self, idade):
        self.idade = idade

    def setSalario(self, salario):
        self.salario = salario

    def setEndividamento(self, endividamento):
        self.endividamento = endividamento

    def getPessoaInfo(self):
        print("a idade é " + str(self.idade))
        print("o salário é " + str(self.salario))
        print("o endividamento é " + str(self.endividamento))

pessoa = Pessoa()
pessoa.setIdade(random.randrange(14,100))
pessoa.setSalario(random.randrange(500,10000))
pessoa.setEndividamento(random.randrange(0,100))
pessoa.getPessoaInfo()

maioridade = True if pessoa.idade >= 18 else False
salarioMinimo = True if pessoa.salario >= 1500 else False

if (maioridade == False or salarioMinimo == False):
    print("a pessoa não cumpre pré requisitos")
else:
    print("a pessoa cumpre os pré requisitos")

faixaEtaria = "a"

if (pessoa.idade >= 18 and pessoa.idade < 30):
    faixaEtaria = "jovem"
elif (pessoa.idade >=30 and pessoa.idade < 60):
    faixaEtaria = "adulto"
elif (pessoa.idade > 60):
    faixaEtaria = "idoso"

faixaSalarial = "a"

if(pessoa.salario >= 1500 and pessoa.salario < 3000):
    faixaSalarial = "baixa"
elif (pessoa.salario >= 3000 and pessoa.salario < 5000):
    faixaSalarial = "média"
elif (pessoa.salario >= 5000):
    faixaSalarial = "alta"

grauDeEndividamento = "a"

if (pessoa.endividamento <= 40):
    grauDeEndividamento = "baixo"
elif (pessoa.endividamento > 40 and pessoa.endividamento <= 60):
    grauDeEndividamento = "medio"
elif (pessoa.endividamento > 60):
    grauDeEndividamento = "alto"

risco = "a"

if (faixaSalarial == "media" and grauDeEndividamento == "baixo"):
    risco = "baixo"
elif (faixaSalarial == "alta" and grauDeEndividamento == "baixo"):
    risco = "baixo"
elif (faixaSalarial == "alta" and grauDeEndividamento == "medio"):
    risco = "medio"
else:
    risco = "alto"

print("o cliente é " + faixaEtaria + " e possui risco de crédito " + risco)
