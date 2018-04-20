'''''
    class ClassName:
        <statement-1>
        .
        .
        .
        <statement-N>
'''

class kitchen:
    a = "meat"
    b = "wheat"
    c = "meal"
    def __init__(self,material1, material2, material3):
        self.a = material1
        self.b = material2
        self.c = material3
    def displayInfo(self):
        print(self.a +"  matarial 2: "+ self.b)

k = kitchen( "sorghum", "milk", "water")
k.displayInfo()