class Owner:
    def __init__(self, name, phone_number):
        self._name = name
        self._phone_number = phone_number
        self._pets = []

    def add_pet(self, pet):
        if pet.is_vaccinated:
            self._pets.append(pet)

    def remove_pet(self, pet):
        if pet in self._pets:
            self._pets.remove(pet)

    def __str__(self):
        pet_names = list(map(lambda pet: pet.name, self._pets))
        return (f"Name: {self._name},"
                f"Phone number: {self._phone_number}"
                f"Pet's names': {pet_names}")
