from faker import Faker

fake = Faker()
fake.name()
fake.phone_number()
fake.email()
fake.city()

fake_bg = Faker("bg-BG")
fake_bg.name()
