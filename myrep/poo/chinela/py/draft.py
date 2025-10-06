class Slipper: 
    def __init__(self):
        self.__tamanho = 0

    def __str__(self):
        return(f"Seu tamanho de chinel é:{self.__tamanho}")
    
    def setTamanho(self, value: int):
        if value < 20 or value > 50 and value % 2 != 0:
            print ("Esse tamanho de chinela é inválido")
            return
        
        self.__tamanho = value
        


    def getTamanho(self) -> int:
        return self.__tamanho
    

def main():
    Chinela = Slipper()
    while Chinela.getTamanho() == 0:
        print ("Digite o tamanho da sua chinela:")
        line = int(input())
        Chinela.setTamanho(line)
        
    print ("sua chinela de tamanho", Chinela.getTamanho())
    
main()


    
