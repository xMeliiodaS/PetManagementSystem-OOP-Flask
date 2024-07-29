class Pet:
    total_pets = 0

    def __init__(self, name, species, age, owner, vaccinated):
        self._name = None
        self._species = None
        self._age = None
        self._owner = None
        self._is_vaccinated = None

        self.name = name
        self.species = species
        self.age = age
        self.owner = owner
        self.is_vaccinated = vaccinated

        Pet.total_pets += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def species(self):
        return self._species

    @species.setter
    def species(self, value):
        if not value:
            raise ValueError("Species cannot be empty")
        self._species = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Age must be a non-negative integer")
        self._age = value

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value

    @property
    def is_vaccinated(self):
        return self._is_vaccinated

    @is_vaccinated.setter
    def is_vaccinated(self, value):
        if not isinstance(value, bool):
            raise ValueError("Vaccinated should be a bool")
        self._is_vaccinated = value

    @staticmethod
    def total_pets_count():
        return Pet.total_pets

    def mark_pet_as_vaccinated(self):
        self.is_vaccinated = True

    def human_age_to_pet(self):
        return self.age * 7

    def __eq__(self, other):
        if not isinstance(other, Pet):
            return False
        return self.name == other.name and self.species == other.species

    def to_dict(self):
        return {
            'name': self.name,
            'species': self.species,
            'age': self.age,
            'owner': self.owner,
            'is_vaccinated': self.is_vaccinated
        }

    def __str__(self):
        return (f"Pet(name: {self.name},"
                f" species: {self.species},"
                f" age: {self.age},"
                f" owner: {self.owner},"
                f" vaccinated: {self.is_vaccinated})")
