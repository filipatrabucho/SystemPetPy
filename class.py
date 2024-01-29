class Animal:
    def __init__(self,nr_chip,nome, idade,raca,porte,peso):
        self.nr_chip=nr_chip
        self.nome=nome
        self.idade=idade
        self.raca=raca
        self.porte=porte
        self.peso=peso 
      

    def InfoAnimal(self):
        return self.nome

class Consulta(Animal):
    def __init__(self,nr_chip,nome, idade,raca,porte,peso,doencas,internamento):
        Animal.__init__(self, nr_chip,nome, idade,raca,porte,peso)
        self.doencas=doencas
        self.internamento=internamento
    
    def Doencas(self):
        return self.doencas

class Dono(Animal):
    def __init__(self,nr_chip,nome, idade,raca,porte,peso,dono,contato,nif,morada):
        Animal.__init__(self, nr_chip,nome, idade,raca,porte,peso)
        self.dono=dono
        self.contato=contato
        self.nif=nif
        self.morada=morada

    def Imprime(self):
       print(f"Numero chip: {self.nr_chip}\nNome: {self.nome}\nIdade: {self.idade}\nPeso: {self.peso}\nDono: {self.dono}\nContato: {self.contato}\nNif: {self.nif}\nMorada: {self.morada}")

def main():
    pessoa = Dono(23, "Bolinhas",5,"Rafeiro","Medio",15, "James",919874563,223654987,"Rua Teste")
    pessoa.Imprime()

main()