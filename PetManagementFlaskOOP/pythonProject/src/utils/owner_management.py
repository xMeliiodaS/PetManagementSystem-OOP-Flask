import json
from src.classes.owner import Owner
from src.classes.pet import Pet


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
                self.save_owner_pets(owner_phone_number)
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
        with open(self.filename, 'a') as file:
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
        # Load existing data
        with open(self.filename, 'r') as file:
            data = json.load(file)

        # Find the owner and update the pets list
        for item in data:
            if item['phone_number'] == owner_phone_number:
                # Find the owner object
                owner = next(owner for owner in self.owners if owner.phone_number == owner_phone_number)
                owner_name = owner.name  # Get the owner's name

                # Create a list of pets with the owner's name instead of the object
                updated_pets = [
                    {
                        **pet.to_dict(),  # Convert pet object to dictionary
                        'owner': owner_name  # Ensure the owner is a name, not an object
                    }
                    for pet in owner.pets
                ]

                # Update the pets list in the item
                item['pets'] += updated_pets
                break

        # Save updated data back to the file
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)

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

    def load_owner_pets(self, name, phone_number):
        """
        Load pets for a specific owner from the JSON file.

        Args:
        - name (str): Name of the owner.
        - phone_number (str): Phone number of the owner.

        Returns:
        - List of Pet objects belonging to the owner.
        """
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                for owner_data in data:
                    if owner_data['name'] == name and owner_data['phone_number'] == phone_number:
                        return owner_data['pets']
        except FileNotFoundError:
            pass
        return []
