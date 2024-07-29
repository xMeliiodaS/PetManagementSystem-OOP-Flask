class Owner:
    def __init__(self, name, phone_number):
        self._name = name
        self._phone_number = phone_number
        self._pets = []

    @property
    def name(self):
        return self._name

    @property
    def phone_number(self):
        return self._phone_number

    def add_pet(self, pet):
        if pet.is_vaccinated:
            self._pets.append(pet)

    def remove_pet(self, pet):
        if pet in self._pets:
            self._pets.remove(pet)

    def get_all_pet_names(self):
        return list(map(lambda pet: pet.name, self._pets))

    def to_dict(self):
        return {
            'name': self._name,
            'phone_number': self._phone_number,
            'pets': [pet.to_dict() for pet in self._pets]
        }

    def __str__(self):
        return (f"Name: {self._name},"
                f"Phone number: {self._phone_number},"
                f"Pet's names': {self.get_all_pet_names()}")
