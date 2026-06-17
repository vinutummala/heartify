import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'a_machine_learning_approach_using_statistical_models.settings')
django.setup()

from Remote_User.models import ClientRegister_Model

# Add users from the SQL dump
users = [
    ('Gopalan', 'Gopalan123@gmail.com', 'Gopalan', '9535866270', 'India', 'karnataka', 'Bangalore'),
    ('Manjunath', 'tmksmanju14@gmail.com', 'Manjunath', '9535866270', 'India', 'Karnataka', 'Bangalore')
]

for username, email, password, phoneno, country, state, city in users:
    ClientRegister_Model.objects.get_or_create(
        username=username,
        email=email,
        password=password,
        phoneno=phoneno,
        country=country,
        state=state,
        city=city
    )

print("Users added successfully")
