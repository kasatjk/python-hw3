
class Account:

    def __init__(self, login: str, email: str, password: str) -> None:
        self.login = login
        self.email = email
        self.password = password

    @property
    def login(self) -> str:
        return self._login
    
    @property
    def email(self) -> str:
        return self._email
    
    @property
    def password(self) -> str:
        return self._password
    
    @login.setter
    def login(self, login: str) -> None:
        if not isinstance(login, str):
            raise ValueError("Login must be a string!")
        if not login:
            raise ValueError("Login cannot be empty!")
        if len(login) < 3 or len(login) > 20:
            raise ValueError("Login must be between 3 and 20 characters!")
        if not all(char.isalnum() or char == "_" for char in login):
            raise ValueError("Login can only contain letters, numbers, and underscores!")
        self._login = login

    @email.setter
    def email(self, email: str) -> None:
        if not isinstance(email, str) or email.count("@") != 1:
            raise ValueError("Invalid email format!")
        local_part, domain = email.rsplit("@", 1)
        if not local_part or "." not in domain or domain.startswith(".") or domain.endswith("."):
            raise ValueError("Invalid email format!")
        self._email = email

    @password.setter
    def password(self, password: str) -> None:
        if not isinstance(password, str) or not password:
            raise ValueError("Password cannot be empty!")
        if len(password) < 8 or len(password) > 30:
            raise ValueError("Password must be between 8 and 30 characters!")
        if not any(char.islower() for char in password):
            raise ValueError("Password must contain a lowercase letter!")
        if not any(char.isupper() for char in password):
            raise ValueError("Password must contain an uppercase letter!")
        if not any(char.isdigit() for char in password):
            raise ValueError("Password must contain a digit!")
        self._password = password

    def verify_password(self, input_password: str) -> bool:
        return self._password == input_password

    def change_password(self, old_password: str, new_password: str) -> None:
        if not self.verify_password(old_password):
            raise ValueError("Old password does not match!")
        if old_password == new_password:
            raise ValueError("New password cannot be the same as the old password!")
        self.password = new_password

    def update_email(self, new_email: str) -> None:
        if self._email == new_email:
            raise ValueError("New email is identical to the current one.")
        self.email = new_email

    def update_login(self, new_login: str) -> None:
        if self._login == new_login:
            raise ValueError("New login is identical to the current one.")
        self.login = new_login

    def display_info(self) -> None:
        print(f"Account(login='{self.login}', email='{self.email}')")
