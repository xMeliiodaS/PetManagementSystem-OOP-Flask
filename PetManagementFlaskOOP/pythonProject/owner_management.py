import json
from pet_management.owner import Owner


class OwnerManagement:
    def __init__(self, filename="pet_database.json"):
        """
        Initialize a Library object.

        Args:
        - filename (str, optional): File name to save/load library data (default is 'library.json').
        """
        self.filename = filename
        self.owners = []
        self.load_owners()

    def add_owner(self, owner):
        """
        Add a book to the library and save library data to file.

        Args:
        - book (Book): Book object to add to the library.
        """
        self.owners.append(owner)
        self.save_owners()

    def add_pet_to_owner(self, pet, owner_phone_number):
        for owner in self.owners:
            if owner.phone_number == owner_phone_number:
                owner.add_pet(pet)
                break

    def remove_pet_from_owner(self, pet, owner_phone_number):
        for owner in self.owners:
            if owner.phone_number == owner_phone_number:
                owner.remove_pet(pet)
                break

    def list_owners(self):
        return self.owners

    def save_owners(self):
        """
        Save the current state of the library (books) to a JSON file.
        """
        with open(self.filename, 'w') as file:
            json.dump([owner.to_dict() for owner in self.owners], file)

    def load_owners(self):
        """
        Load library data from a JSON file into the library (books).
        If the file does not exist, initialize an empty library.
        """
        try:
            with open(self.filename, 'r') as file:
                owner_dicts = json.load(file)
                self.owners = [Owner(owner_dict['name'], owner_dict['phone_number']) for owner_dict in owner_dicts]
        except FileNotFoundError:
            self.owners = []
