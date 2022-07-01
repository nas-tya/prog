# Разработать прототип приложения «Регистрация на конференцию на основе фрагмента технического задания с использованием ООП


class NewRegistration:
    def __init__(self,
                 first_name="",
                 second_name="",
                 email="",
                 password="",
                 address="",
                 postal_code="",
                 city="",
                 country=""):
        self.__first_name, self.__email, self.__second_name, self.__password, self.__address, self.__city, self.__country, self.__postal_code = first_name, email, second_name, password, address, city, country, postal_code

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, new_first_name):
        if new_first_name != "":
            self.__first_name = new_first_name

    @property
    def second_name(self):
        return self.__second_name

    @second_name.setter
    def second_name(self, new_second_name):
        if new_second_name != "":
            self.__second_name = new_second_name

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        self.__password = new_password

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email):
        self.__email = new_email

    @property
    def postal_code(self):
        return self.__postal_code

    @postal_code.setter
    def postal_code(self, new_postal_code):
        self.__postal_code = new_postal_code

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, new_city):
        self.__city = new_city

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, new_country):
        self.__country = new_country

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, new_address):
        self.__address = new_address

    def __repr__(self):
        string_1 = 'Name: {0}\nSurname: {1}\nEmail: {2}\nPassword: {3}\nAddress:' \
                   ' {4}\nPostal code: {5}\n'
        string_2 = 'City: {6}\nCountry: {7}\n'
        return (string_1 + string_2).format(self.first_name, self.second_name, self.email, self.password, self.address, self.postal_code, self.city, self.country)

test_user_1 = NewRegistration('John', 'Doe', 'john@gmail.com', 'Qwerty123o', 'st. of Streets, b.6', '123123132', 'London', 'England')
print(test_user_1)
