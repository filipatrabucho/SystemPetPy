class Animal:
    def __int__(self,id, nome, idade,raca,porte,peso,nr_chip):
        self.id=id
        self.nome=nome
        self.idade=idade
        self.raca=raca
        self.porte=porte
        self.peso=peso
        self.nr_chip=nr_chip

    def InfoAnimal(self):
        print(f"Nome: {self.nome}")

class Consulta(Animal):
    def __init__(self,id,doencas,internamento):
        super().__init__(id)
        self.doencas=doencas
        self.internamento=internamento
    
class Dono(Animal):
    def __init__(self,id,nome,contato,nif,morada):
        super().__init__(id)
        self.nome=nome
        self.contato=contato
        self.nif=nif
        self.morada=morada

    def Imprime(self):
        print(f"Nome do dono: {self.nome}")

def main():
    a2=Dono("1","Ana","987456123","123456789", "Rua Teste 23123")
    a2.Imprime()


main()