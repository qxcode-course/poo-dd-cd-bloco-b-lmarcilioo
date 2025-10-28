class Tamagochi:
    def __init__ (self, energy: int, clean: int):
        self.energy = energy
        self.clean = clean
        self.age = 0
    
    def __str__ (self):
        return f"E:{self.energy}, L:{self.clean}, I:{self.age}"
    
    def getClean (self):


def main ():
    bichinho = Tamagochi 
    while True: 
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args [0] == "end":
             break
        elif args [0] == "init":
            energy:int = int(args[1])
            clean: int = int(args[2])
            bichinho = Tamagochi(energy,clean)
        elif args [0] == "show":
            print(bichinho)