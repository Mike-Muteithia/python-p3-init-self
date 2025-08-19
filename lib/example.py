class Dog:
    def __init__(self, name, favorite_toy="Any"):
        # print(f"{name} is born!")
        self.name = name
        self.favorite_toy = favorite_toy

    def bark(self):
        print("Woof!")

    def get_adopted(self, owner_name):
        self.owner = owner_name

    # def showing_self(self):
        # return self


fido = Dog("Fido")

print(fido.favorite_toy)

# fido.get_adopted("Sophie")
# fido.owner = "Sophie"
# print(fido.owner)

# print(fido.name)
# print(fido)

# fido.breed = "Dalmatian"
# print(fido.breed)

# print(fido.showing_self())
# print(fido is fido.showing_self())

snoopy = Dog("Snoopy", "Tennis Ball")

print(snoopy.favorite_toy)

# print(snoopy.name)
# print(snoopy)
# snoopy.breed = "Beagle"
# print(snoopy.breed)


# old_yeller = Dog()










