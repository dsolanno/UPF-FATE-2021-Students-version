## Content of synthetic_data_generator.py
## Creating our dataset
import pandas as pd
import numpy as np

import random

from faker import Faker
from faker.providers import phone_number, credit_card
import gender_guesser.detector as gender

random.seed(99)
Faker.seed(2441)
fake = Faker('es_ES')
fake.add_provider(phone_number)
fake.add_provider(credit_card)

conditions_array = [
    "Asthma",
    "Bird flu",
    "Common cold and flu",
    "COVID-19 (Novel coronavirus)"]

bcn_zipcodes = ["08001",
                "08002",
                "08003",
                "08004",
                "08011",
                "08012",
                "08013",
                "08014"]

birth_dates = ["20000101", #2000 ## YYYYMMDD
               "20000109",
               "20000110",
               "20000111",
               "20001001",
               "20001009",
               "20001010",
               "20001011",
               "20010101", #2001
               "20010109",
               "20010110",
               "20010111",
               "20011001",
               "20011009",
               "20011010",
               "20011011"]

names = []
zipcodes = []
credit_card = []
phone_numbers = []
texts = []
neighbourhoods = []
births = []
conditions = []
ssns = []
ids=[]
weights = []
heights = []
genders = []


d = gender.Detector()


for n in range(100):
    name = fake.name()
    names.append(name)
    credit_card.append(fake.credit_card_full())
    phone_numbers.append(fake.phone_number())
    texts.append(fake.text())
    ssns.append(fake.ssn())
    ids.append(1000 + n)
    weights.append(random.randint(55,95))
    heights.append(int(np.random.normal(175, 10)))
    g = d.get_gender(u"{}".format(name.split(" ")[0]))
    if g == "male":
        _g = "Male"
    else:
        _g = "Female"
    genders.append(_g)

    
for n in range(100):
    zipcodes.append(str(random.choice(bcn_zipcodes)))
    conditions.append(random.choice(conditions_array))
    births.append(random.choice(birth_dates))
    
    
df = pd.DataFrame(columns=["PatientName", "SSN", "PatientID", "Phone", "Gender", "BirthDate", "ZipCode", "Health Condition"])

df["PatientName"] = names
df["SSN"] = ssns
df["PatientID"] = ids
df["Gender"] = genders
df["BirthDate"] = births
df["ZipCode"] = zipcodes
df["Health Condition"] = conditions
df["Weight"] = weights
df["Height"] = heights
df['Phone'] = phone_numbers


df.to_csv("Data/health_dataset.csv", index=False)
