class Tshirt:
    def __init__(self):
        self.__size: str = ""

    def __str__ (self):
        return f"size: ({self.__size})"

    def setSize (self, sizeAceppt: str):
        availableSizes = ["PP", "P", "M", "G", "GG", "XG"]
        if sizeAceppt.upper() in availableSizes: 
            self.__size = sizeAceppt.upper()
            return
        print ("fail: Valor inválido, tente PP, P, M, G, GG ou XG") 
            
                   
    def getSize(self) -> str:
        return self.__size        
    
def main():
    Camisa = Tshirt()
    while True:
        line: str = input()
        print ("$"+ line)
        args: list[str] = line.split(" ")
        if args [0] == "end":
            break
        elif args [0] == "show":
            print(Camisa)
        elif args [0] == "size":
            Camisa.setSize(args[1])

main()