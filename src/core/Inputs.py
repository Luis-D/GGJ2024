class Gamepad:
    def Reset(self):
        self.izq = False
        self.der = False
        self.arr = False
        self.aba = False
        self.acc = False
        self.can = False
        self.esc = False
    def __init__ (self):
        self.Reset()

Controles = Gamepad()

