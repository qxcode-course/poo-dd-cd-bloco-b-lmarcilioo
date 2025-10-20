class Watch:
    def __init__(self, hora: int, min: int, seg: int):
        self.__hora = hora
        self.__min = min
        self.__seg = seg

    def __str__(self) -> str:
        return f"{self.__hora:02}:{self.__min:02}:{self.__seg:02}"

    def setHora(self, valor: int):
        if valor > 23 or valor < 0:
            print("fail: hora invalida")
            return
        self.__hora = valor

    def getHora (self):
        return self.__hora

    def setMin (self, valor:int):
        if valor > 59 or valor < 0:
            print()    

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
        if args [0] == "set":
            hora: int = int(args[1])
            min: int = int(args [2])
            seg: int = int(args [3])
            relogio = Watch(hora,min,seg)
            relogio.setHora(hora)
main()