class Tshirt:
    def __init__(self):
        self.__size: str = " "

    def setSize (self, sizeAceppt: str):
        if sizeAceppt != "PP" and sizeAceppt!= "P" and sizeAceppt!= "M" and sizeAceppt!= "G" and sizeAceppt!= "GG" and sizeAceppt!= "XG":
           print ("fail: Valor inválido, tente PP, P, M, G, GG ou XG") 
        else:
            self.__size = sizeAceppt
            return 
                   
    def getSize(self) -> str:
        return self.__size        
    
def main():
    Camisa = Tshirt()
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split (" ")
        if args [0] == "show":
           print (f"size: {Camisa}")
        if args [0] == "size":
            main()