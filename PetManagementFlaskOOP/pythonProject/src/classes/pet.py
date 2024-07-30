class Pet:
    total_pets = 0

    def __init__(self, name: str, species, age: int, owner, vaccinated: bool):
        """
        Initializes a new Pet instance with the provided name,
         species, age, owner, and vaccination status. Increments the total_pets count.
        """
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
        """
        Gets the name of the pet.
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Sets the name of the pet. Raises ValueError if the name is empty or not a string.
        """
        if not value and not isinstance(value, str):
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def species(self):
        """
        Gets the species of the pet.
        """
        return self._species

    @species.setter
    def species(self, species):
        """
        Sets the species of the pet. Raises ValueError if the species is empty or not a string.
        """
        if not species:
            raise ValueError("Species cannot be empty")
        self._species = species

    @property
    def age(self):
        """
        Gets the age of the pet and converts the pet's age to human years (multiplies by 7).
        """
        return self._age * 7

    @age.setter
    def age(self, value):
        """
        Sets the age of the pet. Raises ValueError if the age is not a non-negative integer.
        """
        if not isinstance(value, int) or value < 0:
            raise ValueError("Age must be a non-negative integer")
        self._age = value

    @property
    def owner(self):
        """
        Gets the owner of the pet.
        """
        return self._owner

    @owner.setter
    def owner(self, value):
        """
        Sets the owner of the pet.
        """
        self._owner = value

    @property
    def is_vaccinated(self):
        """
        Gets the vaccination status of the pet.
        """
        return self._is_vaccinated

    @is_vaccinated.setter
    def is_vaccinated(self, value):
        """
        Sets the vaccination status of the pet. Raises ValueError if the status is not a boolean.
        """
        if not isinstance(value, bool):
            raise ValueError("Vaccinated should be a bool")
        self._is_vaccinated = value

    @staticmethod
    def total_pets_count():
        """
        Returns the total number of Pet instances created.
        """
        return Pet.total_pets

    def mark_pet_as_vaccinated(self):
        """
        Marks the pet as vaccinated.
        """
        if not self._is_vaccinated:
            self.is_vaccinated = True

    def __eq__(self, other):
        """
        Checks equality between two Pet instances based on their name and species.
        """
        if not isinstance(other, Pet):
            return False
        return self.name == other.name and self.species == other.species

    def to_dict(self):
        """
        Converts the pet's attributes to a dictionary.
        """
        return {
            'name': self.name,
            'species': self.species,
            'age': self.age,
            'owner': self.owner,
            'is_vaccinated': self.is_vaccinated
        }

    def __str__(self):
        """
        Returns a string representation of the pet.
        """
        return (f"Pet(name: {self.name},"
                f" species: {self.species},"
                f" age: {self.age},"
                f" owner: {self.owner},"
                f" vaccinated: {self.is_vaccinated})")
