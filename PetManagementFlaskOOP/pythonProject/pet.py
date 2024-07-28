class Pet:
    def __init__(self, name, species, age, owner, vaccinated):
        self._name = name
        self._species = species
        self._age = age
        self._owner = owner
        self._vaccinated = vaccinated

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
    def vaccinated(self):
        return self._vaccinated

    @vaccinated.setter
    def vaccinated(self, value):
        self._vaccinated = value

    def __str__(self):
        return (f"Pet(name: {self._name},"
                f" species: {self._species},"
                f" age: {self._age},"
                f" owner: {self._owner},"
                f" vaccinated: {self._vaccinated})")
