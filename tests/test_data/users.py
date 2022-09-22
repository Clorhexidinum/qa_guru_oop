from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class Subject(Enum):
    History = 'History'
    Maths = 'Maths'
    Physics = 'Pysics'


class Hobby(Enum):
    Sports = '1'
    Reading = '2'
    Music = '3'


class Gender(Enum):
    Male = 'Male'
    Female = 'Female'
    Other = 'Other'


print(type(Gender.Male))


@dataclass
class User:
    gender: Enum = Gender.Male
    first_name: str = 'Ivan'
    last_name: str = 'Petrov'
    email: str = 'test@gmail.com'
    user_number: str = '89777777777'
    birth_day: str = '30'
    birth_month: str = 'October'
    birth_year: str = '1991'
    subjects: Tuple[Subject] = (Subject.History, Subject.Physics)
    current_address: str = 'bla bla bla'
    hobbies: Tuple[Hobby] = (Hobby.Sports, Hobby.Reading)
    picture_file: str = 'for_test_dont_remove.jpg'
    state: str = 'Haryana'
    city: str = 'Karnal'


murat = User(first_name='Murat', last_name='Kubekov', gender=Gender.Male)
