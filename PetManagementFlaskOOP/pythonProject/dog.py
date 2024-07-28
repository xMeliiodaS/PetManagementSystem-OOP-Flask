from pet import Pet


class Dog(Pet):
    def __init__(self, breed, name, species, age, owner, vaccinated):
        super().__init__(name, species, age, owner, vaccinated)
        self._breed = breed

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        self._breed = value

    def __str__(self):
        return f"{super().__str__()}, breed={self._breed}"
