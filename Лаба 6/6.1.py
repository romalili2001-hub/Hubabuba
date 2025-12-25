class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password  # приватный атрибут
    
    def set_password(self, new_password):
        self.__password = new_password
    
    def check_password(self, password):
        return password == self.__password

# Использование
user = UserAccount("ivan", "ivan@mail.ru", "12345")
user.set_password("qwerty")
print(user.check_password("qwerty"))  # True
print(user.check_password("12345"))   # False
