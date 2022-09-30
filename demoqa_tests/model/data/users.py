from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class Subject(Enum):
    History = 'History'
    Maths = 'Maths'
    Physics = 'Pysics'


class Hobby(Enum):
    Sports = 'Sports'
    Reading = 'Reading'
    Music = 'Music'


class Gender(Enum):
    Male = 'Male'
    Female = 'Female'
    Other = 'Other'



@dataclass
class User:
    gender: Enum = Gender.Male
    first_name: str = 'Ivan'
    last_name: str = 'Petrov'
    email: str = 'test@gmail.com'
    phone_number: str = '89777777777'
    birth_day: str = '30'
    birth_month: str = 'October'
    birth_year: str = '1991'
    subjects: Tuple[Subject] = (Subject.History, Subject.Maths)
    current_address: str = 'Moscow'
    hobbies: Tuple[Hobby] = (Hobby.Sports, Hobby.Reading)
    picture_file: str = 'picture.jpg'
    state: str = 'Haryana'
    city: str = 'Karnal'


murat = User(first_name='Murat', last_name='Kubekov', gender=Gender.Male)
