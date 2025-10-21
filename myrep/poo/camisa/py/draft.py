class Tshirt:
    def __init__(self):
        self.__size: str = ""

    def setSize (self, sizeAceppt: str):
        availableSizes = ["PP", "P", "M", "G", "GG", "XG"]
        if sizeAceppt.upper() in availableSizes: 
            self.__size = sizeAceppt.upper()
            return
        print ("Esse tamanho de camisa é inválido") 
            
                   
    def getSize(self) -> str:
        return self.__size        
    
def main():
    Camisa = Tshirt()
    while Camisa.getSize() == "":
        print ("Informe o tamanho da roupa:")
        line = input()
        Camisa.setSize(line)
    print("O tamanho da sua camisa é: "+ Camisa.getSize())
main()