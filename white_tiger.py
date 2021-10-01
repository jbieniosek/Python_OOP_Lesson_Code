from tiger import Tiger

class WhiteTiger(Tiger):

    def __init__(self, stripes = True, habitat = "Jungle", sound = "roar", toe_beans = "adorable"):
        super().__init__(stripes, habitat, sound, toe_beans)
        self.color = "white"
    
    def __str__(self):
        return f"My {self.color} tiger lives in {self.habitat}, makes a {self.sound} and has {self.toe_beans} toe beans"