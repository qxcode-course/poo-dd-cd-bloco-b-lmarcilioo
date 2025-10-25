class Pessoa:
    def __init__ (self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def __str__ (self):
        return f"{self.nome}:{self.idade}"
    
class moto:     
    def __init__ (self, potencia: int = 1, tempo: int = 0):
        self.__potencia = potencia
        self.__pessoa: Pessoa | None = None
        self.__tempo = tempo
    
    def getPessoa (self):
        return self.__pessoa
    
    def getPotencia (self):
        return self.__potencia
    
    def getTempo (self):
        return self.__tempo
    

    def __str__ (self):
         return f"power:{self.getPotencia()}, time:{self.getTempo()}, person:({self.getPessoa() if self.getPessoa() is not None else "empty"})"
    
    def inserir (self, pessoa: Pessoa) -> bool:
        if self.__pessoa != None:
            print ("fail: busy motorcycle")
            return False
        else:
            self.__pessoa = pessoa
            return True
        
    def remove (self) -> Pessoa | None:
        if self.__pessoa == None:
            print ("fail: empty motorcycle")
        saiuPessoa = self.__pessoa
        self.__pessoa = None
        return saiuPessoa
    
    def comprarTempo(self, amount: int):
        self.__tempo += amount
    
    def drive(self, time:int):
        if self.__tempo == 0:
            print("fail: buy time first")


def main ():
    motoca = moto()
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split (" ")
        if args [0] == "end":
            break
        if args [0] == "init":
            motoca = moto(potencia=int(args[1]))
        if args [0] == "show":
            print (motoca)
        if args [0] == "enter":
            pessoa: Pessoa = Pessoa(nome = args[1], idade=int(args[2]))
            motoca.inserir(pessoa)
        if args [0] == "leave":
            saiuPessoa = motoca.remove()
            if saiuPessoa != None:
                print(saiuPessoa)
        if args [0] == "buy":
            amount:int = int(args[1])
            motoca.comprarTempo(amount)
        if args [0] == "drive":
            motoca.drive(int(args[1]))



main ()