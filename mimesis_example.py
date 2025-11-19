from mimesis import Finance, Person
from mimesis.locales import Locale

person = Person(Locale.JA)

print(person.email())
print(person.name())
print(person.phone_number())

finance = Finance(Locale.DA)
print(finance.company())
print(finance.bank())
print(finance.price(minimum=100, maximum=1000))
print(finance.stock_name())
