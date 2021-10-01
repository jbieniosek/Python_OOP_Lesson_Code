class Tiger():

    scientific_name_var = "Panthera tigris"

    @classmethod
    def friendly_tiger(cls):
        return cls(True, "my house", "rawr", "super cute")


    @staticmethod
    def scientific_name():
        return Tiger.scientific_name_var

    def __init__(self, stripes = True, habitat = "Jungle", sound = "roar", toe_beans = "adorable"):
        self.stripes = stripes
        self.habitat = habitat
        self.sound = sound
        self.toe_beans = toe_beans
    
    def __str__(self):
        return f"My tiger lives in {self.habitat}, makes a {self.sound} and has {self.toe_beans} toe beans"