import string

class BasePasswordManager:
    def __init__(self):
        self.old_passwords = ["welcome"]

    def get_password(self):
        return self.old_passwords[-1]

    def is_correct(self, password):
        return password == self.get_password()

class PasswordManager(BasePasswordManager):
    def set_password(self, old_password, new_password):
        if not self.is_correct(old_password):
            return False

        if len(new_password) < 6:
            return False

        # check security level of new password
        if self.get_level(new_password) < self.get_level(old_password):
            return False

        self.old_passwords.append(new_password)
        return True

    def get_level(self, password):
        if any(char in string.punctuation for char in password):
            return 2
        elif any(char.isdigit() for char in password):
            return 1
        else:
            return 0
pw = PasswordManager()
pw.set_password("welcome","sanjay")
ans=pw.get_password()
pw.set_password("sanjay","ram@12345")
ans=pw.get_password()
ans2 = pw.is_correct("ram@12345")
ans3 = pw.get_level("ram@12345")
print(ans)
print(ans2)
print(ans3)