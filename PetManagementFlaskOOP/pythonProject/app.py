from flask import Flask, render_template, request, redirect, url_for

from src.classes.pet import Pet
from src.utils.owner_management import OwnerManagement
from src.classes.owner import Owner

app = Flask(__name__)
owner_management = OwnerManagement()


@app.route('/')
def home_page():
    return render_template('home_page.html')


@app.route('/owner')
def owner_page():
    listed_owners = owner_management.list_owners()
    return render_template('owner_page.html', owners=listed_owners)


@app.route('/add_owner', methods=['GET', 'POST'])
def add_owner():
    if request.method == 'POST':
        name = request.form['name'].strip()
        phone = request.form['phone'].strip()
        owner = Owner(name, phone)
        owner_management.add_owner(owner)
        print("Added Owner: ", owner)

        return redirect(url_for('owner_page'))
    return render_template('add_owner.html')


@app.route('/add_pet/<pet_owner>', methods=['GET', 'POST'])
def add_pet(pet_owner):
    if request.method == 'POST':
        pet_name = request.form['name'].strip()
        species = request.form['species'].strip()
        age = int(request.form['age'].strip())

        vaccinated_str = request.form.get('vaccinated', '').strip().lower()
        vaccinated = vaccinated_str in ['true', '1', 'yes']

        parts = pet_owner.split(',')
        name = parts[0].split(': ')[1].strip()
        phone = parts[1].split(': ')[1].strip()

        owner = Owner(name, phone)

        pet = Pet(pet_name, species, age, owner, vaccinated)
        owner_management.add_pet_to_owner(pet, phone)
        return redirect(url_for('owner_page'))
    return render_template('add_pet.html', pet_owner=pet_owner)


@app.route('/pets_list/<pet_owner>')
def pets_list(pet_owner):
    parts = pet_owner.split(',')
    name = parts[0].split(': ')[1].strip()
    phone = parts[1].split(': ')[1].strip()

    owner = Owner(name, phone)
    owner_management.load_owners()
    pets = owner_management.load_owner_pets(name, phone)

    return render_template('pet_page.html', owner=owner, pets=pets)


if __name__ == '__main__':
    app.run(debug=False)
