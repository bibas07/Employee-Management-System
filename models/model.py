class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_username(self):
        return self.username

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password


class Register:
    def __init__(self, username, password, password2, age, address, fullname, email):
        self.username = username
        self.password = password
        self.password2 = password2
        self.age = age
        self.address = address
        self.fullname = fullname
        self.email = email

    def set_username(self, username):
        self.username = username

    def get_username(self):
        return self.username

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password

    def set_password2(self, password2):
        self.password2 = password2

    def get_password2(self):
        return self.password2

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address

    def set_fullname(self, fullname):
        self.fullname = fullname

    def get_fullname(self):
        return self.fullname

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email


class DataRecord:
    def __init__(self, post_id, position, job_type, language, exp_time, company):
        self.post_id = post_id
        self.position = position
        self.job_type = job_type
        self.language = language
        self.exp_time = exp_time
        self.company = company

    def set_post_id(self, post_id):
        self.post_id = post_id

    def get_post_id(self):
        return self.post_id

    def set_position(self, position):
        self.position = position

    def get_position(self):
        return self.position

    def set_job_type(self, job_type):
        self.job_type = job_type

    def get_job_type(self):
        return self.job_type

    def set_language(self, language):
        self.language = language

    def get_language(self):
        return self.language

    def set_exp_time(self, exp_time):
        self.post_id = exp_time

    def get_exp_time(self):
        return self.exp_time

    def set_company(self, company):
        self.company = company

    def get_company(self):
        return self.company


class ChangeProfile:
    def __init__(self, username, age, address, fullname, email):
        self.username = username
        self.age = age
        self.address = address
        self.fullname = fullname
        self.email = email

    def get_username(self):
        return self.username

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address

    def set_fullname(self, fullname):
        self.fullname = fullname

    def get_fullname(self):
        return self.fullname

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email
