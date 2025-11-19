from faker import Faker

fake = Faker("ru_RU")
print(fake.name())
print(fake.email())
print(fake.address())
print(fake.phone_number())
print(fake.password())
print(fake.color())
print(fake.company())
print(fake.date_of_birth())


def generate_user():
    return {
        "username": fake.user_name(),
        "email": fake.email(domain="gmail.com"),
        "password": fake.password(length=10, digits=True, upper_case=True, lower_case=True),
        "birthdate": fake.date_of_birth(minimum_age=18, maximum_age=60),
        "phone": fake.phone_number(),
        "job": fake.job(),
        "company": fake.company(),
    }


user = generate_user()
print(user)
