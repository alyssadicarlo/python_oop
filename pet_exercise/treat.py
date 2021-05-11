class Treat:
    def __init__(self, fill=10, joy=10):
        self.fill = fill
        self.joy = joy
        
    
class ColdPizza(Treat):
    def __init__(self):
        super().__init__(10, 10)

class Bacon(Treat):
    def __init__(self):
        super().__init__(5,5)

class VeganSnack(Treat):
    def __init__(self):
        super().__init__(1,0)