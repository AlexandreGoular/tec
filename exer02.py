# 2. A fim de representar empregados em uma firma, crie uma classe chamada
# Empregado que inclui as três informações a seguir como atributos:
# • um primeiro nome,
# • um sobrenome, e
# • um salário mensal.
# Sua classe deve ter um construtor que inicializa os três atributos. Forneça um
# método
# set e get para cada atributo. Se o salário mensal não for positivo, configure-o
 #como 0.0. Escreva um aplicativo de teste que demonstra as capacidades da classe. 
#Crie duas instâncias da classe e exiba o salário anual de cada instância. 
#Então dê a cada
# empregado um aumento de 10% e exiba novamente o salário anual de cada empregado.

class Empregado:
    def __init__(self):
        self.primeiroNome = None 
        self.sobrenome = None 
        self.salario = None 

    def setPrimeiroNome(self, novoNome):
        self.primeiroNome = novoNome
    
    def setSobrenome(self, novoSobrenome):
        self.sobrenome = novoSobrenome

    def setSalario(self, novoSalario):
        self.salario = novoSalario

    def getPrimeiroNome(self):
        return self.primeiroNome

    def getSobrenome(self):
        return self.sobrenome

    def getSalario(self):
        if(self.salario < 1):
            self.salario = 0
            return self.salario
        else:
            return self.salario

    def salarioAnual(self):
        self.salarioAnual = (self.salario * 12)
        return self.salarioAnual

    def salarioAumento(self):
        self.salarioAumento = (self.salarioAnual * 0.10) + self.salarioAnual
        return self.salarioAumento

empregadoUm = Empregado()

nome = empregadoUm.primeiroNome = "Cleyton"
sobre = empregadoUm.sobrenome = "Jeyro"
salario = empregadoUm.salario = 1000

anosalario = empregadoUm.salarioAnual()
aumentoSalario = empregadoUm.salarioAumento()

print("O empregado {} {} recebe {} ao ano e com aumento receve {}".format(nome, sobre, anosalario, aumentoSalario))