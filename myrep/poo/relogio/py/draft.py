
class Watch:
    def __init__(self, hora: int, min: int, seg: int):
        self.__hora = 0
        self.__min = 0
        self.__seg = 0
        self.setHora(hora)
        self.setMin(min)
        self.setSeg(seg)
    def __str__(self) -> str:
        return f"{self.__hora:02}:{self.__min:02}:{self.__seg:02}"

    def setHora(self, valor: int):
        if valor > 23 or valor < 0:
            print("fail: hora invalida")
            return
        self.__hora = valor

    def getHora (self):
        return self.__hora
    
    def getMin (self):
        return self.__min
    
    def getSeg (self):
        return self.__seg

    def setMin (self, valor:int):
        if valor > 59 or valor < 0:
            print("fail: minuto invalido") 
            return
        self.__min = valor

    def setSeg (self, valor: int):
        if valor > 59 or valor < 0:
            print ("fail: segundo invalido")
            return
        self.__seg = valor   

    def nextSecond (self):
        if self.getSeg() != 59:
            self.setSeg(self.getSeg()+1)

        else:
            self.setSeg(0) 
            if self.getMin() != 59:
                self.setMin(self.getMin()+1)
            else: 
                self.setMin(0)
                if self.getHora() != 23:
                    self.setHora (self.getHora()+1)
                else:
                    self.setHora(0)

def main():
    relogio = Watch(0,0,0)
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split (" ")
        if args [0] == "end":
            break
        if args [0] == "show":
            print(relogio)
        if args [0] == "init":
            hora: int = int(args[1])
            min: int = int(args [2])
            seg: int = int(args [3])
            relogio = Watch(hora, min, seg)
        if args [0] == "set":
            hora: int = int(args[1])
            min: int = int(args [2])
            seg: int = int(args [3])
            relogio.setHora(hora)
            relogio.setMin(min)
            relogio.setSeg(seg)
        if args [0] == "next":
            relogio.nextSecond()
main()