class User:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Yosh manfiy bo'lishi mumkin emas!")
        self._age = value


user = User("Ali", 25)
print(user.age)
user.age = 30
print(user.age)
