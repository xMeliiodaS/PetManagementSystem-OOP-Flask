import json
from src.classes.owner import Owner


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
                self.save_owner_pets(owner_phone_number)
                self.save_owners()
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

    def save_pet(self, phone):
        """
        Save the current state of the library (books) to a JSON file.
        """
        with open(self.filename, 'w') as file:
            json.dump([owner.to_dict() for owner in self.owners], file)

    def save_owner_pets(self, owner_phone_number):
        """
        Save pets for a specific owner to the JSON file.

        Args:
        - owner_phone_number (str): Phone number of the owner whose pets need to be saved.
        """
        # Find the owner
        for owner in self.owners:
            if owner.phone_number == owner_phone_number:
                owner_data = owner.to_dict()
                # Update only the pets information in the JSON file
                with open(self.filename, 'r+') as file:
                    data = json.load(file)
                    file.seek(0)  # Go back to the beginning of the file
                    for i, item in enumerate(data):
                        if item['phone_number'] == owner_phone_number:
                            data[i] = owner_data
                            break
                    file.truncate()  # Remove any remaining data after the new data
                    json.dump(data, file, indent=4)
                break

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
