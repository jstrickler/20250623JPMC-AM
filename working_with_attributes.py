from president import President

p = President(26)
print(p)

print(dir(p))
print()
print(p.first_name, p.last_name)
print("party" in dir(p))
print(hasattr(p, "party"))
party = getattr(p, "party")
print(party, type(party))
# dir() getattr() hasattr() setattr() delattr()

class Dog:
    pass

d = Dog()

def woof(self):
    print("Woof! Woof!")

setattr(Dog, "bark", woof)

d.bark()
setattr(d, "breed", "English Shepherd")
print(d.breed)

for attr_name in dir(p):
    if attr_name.startswith("__"):
        continue
    attr_value = getattr(p, attr_name)
    attr_type = type(attr_value)
    print(f"{attr_name:12s} {attr_type} {attr_value}")