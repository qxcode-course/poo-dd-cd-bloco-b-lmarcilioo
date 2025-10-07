class Tshirt:
    def __init__(self):
        self.__size: str = ""

    def setSize (self, sizeAceppt: str):
        if sizeAceppt != "PP" and sizeAceppt!= "P" and sizeAceppt!= "M" and sizeAceppt!= "G" and sizeAceppt!= "GG" and sizeAceppt!= "XG":
           print ("Esse tamanho de camisa é inválido") 
        else:
            self.__size = sizeAceppt
            return
                   
    def getSize(self) -> str:
        return self.__size        
    
def main():
    Camisa = Tshirt()
    while True:
        print ("Informe o tamanho da roupa:")
        line = input()
        Camisa.setSize(line)

        print("O tamanho da sua camisa é: " + Camisa.getSize())
        break
main()