
class Lead:
    def __init__ (self, thickness: int, hardness: str, size: int):
      self.__thickness = None
      self.__hardness = hardness
      self.__size = size

   
    def getThickness (self):
       return self.__thickness
    
    def getHardness (self):
       return self.__hardness
    
    def getSize (self):
       return self.__size
    
    def usagePerSheet (self, value:int):
       if self.getHardness == "HB":
          value -= 1
       elif self.getHardness == "2B":
          value -= 2
       elif self.getHardness == "4B":
          value -= 4
       elif self.getHardness == "6B":
          value -= 6
          

class Pencil:
   def __init__ (self):
       self.thickness: float = 0.0
       self.tip = Lead | None

   def hasGrafite(self) -> bool:
      return self.tip is not None
      
   def __str__ (self):
      return f"calibre: {self.thickness}, grafite:{self.tip}"

def main():
   grafite = Pencil
   while True:
      line = input ()
      print("$" + line)
      args: list[str] = line.split (" ")
      if args [0] == "end":
         break
      if args [0] == "show":
        print (grafite)
      if args [0] == "init":
         calibre: float = float(args[1])
         grafite: str = str(args[2]) 

main()