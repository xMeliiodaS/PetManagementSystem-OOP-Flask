class Pet:
    def __init__(self, name, species, age, owner, vaccinated):
        self._name = self.set_name(name)
        self._species = self.set_species(species)
        self._age = self.set_age(age)
        self._owner = self.set_owner(owner)
        self._is_vaccinated = self.set_is_vaccinated(vaccinated)

    @property
    def name(self):
        return self.name

    def set_name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value
        return self._name

    @property
    def species(self):
        return self._species

    def set_species(self, value):
        if not value:
            raise ValueError("Species cannot be empty")
        self._species = value
        return self._species

    @property
    def age(self):
        return self._age

    def set_age(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Age must be a non-negative integer")
        self._age = value
        return self._age

    @property
    def owner(self):
        return self._owner

    def set_owner(self, value):
        self._owner = value
        return self._owner

    @property
    def is_vaccinated(self):
        return self._is_vaccinated

    def set_is_vaccinated(self, value):
        if not isinstance(value, bool):
            raise ValueError("Vaccinated should be a bool")
        self._is_vaccinated = value
        return self._is_vaccinated

    def __str__(self):
        return (f"Pet(name: {self.name},"
                f" species: {self.species},"
                f" age: {self.age},"
                f" owner: {self.owner},"
                f" vaccinated: {self.is_vaccinated})")
