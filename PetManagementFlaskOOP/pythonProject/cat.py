from pet import Pet


class Cat(Pet):
    def __init__(self, name, species, age, owner, vaccinated, indoor):
        super().__init__(name, species, age, owner, vaccinated)
        self._indoor = None
        self.indoor = indoor

    @property
    def indoor(self):
        return self._indoor

    @indoor.setter
    def indoor(self, value):
        if not isinstance(value, bool):
            raise ValueError("Indoor should be a bool")
        self._indoor = value

    def __str__(self):
        return f"{super().__str__()}, indoor={self._indoor}"
