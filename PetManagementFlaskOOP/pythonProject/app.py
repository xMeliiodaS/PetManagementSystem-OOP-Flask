from flask import Flask, render_template, request, redirect, url_for
from owner_management import OwnerManagement
from pet_management.owner import Owner

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


@app.route('/add_pet/<owner_phone_number>')
def add_pet(owner_phone_number):
    # Implement the logic to add a pet to the owner
    return f"Add pet for owner with phone number {owner_phone_number}"


@app.route('/pets_list/<owner_phone_number>')
def pets_list(owner_phone_number):
    # Implement the logic to list pets for the owner
    return f"List of pets for owner with phone number {owner_phone_number}"


if __name__ == '__main__':
    app.run(debug=False)
