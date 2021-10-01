from tiger import Tiger
from white_tiger import WhiteTiger

def cat_named_tommy(sound_fn):
    def add_tommy():
        print("Tommy says:")
        sound_fn()
    return add_tommy



@cat_named_tommy
def meow():
    print("meow")

@cat_named_tommy
def hiss():
    print("hiss")

def purr():
    print("purr")

tommy_purrs = cat_named_tommy(purr)

#tommy_purrs()

#meow()

#hiss()

tiger = Tiger(toe_beans = "big ones!")
tiger2 = Tiger(stripes = False, habitat = "snow")
#print(tiger.scientific_name())
#print("Not an instance:")
#print(Tiger.scientific_name())

friendly_tiger = WhiteTiger.friendly_tiger()
print(friendly_tiger)
