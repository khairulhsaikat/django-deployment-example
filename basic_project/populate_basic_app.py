import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','basic_project.settings')

import django
django.setup()

import random
from basic_app.models import AccessRecord,Topic,Webpage,User
from faker import Faker

fake_gen = Faker()
topics = ['Search','Social Media','Marketplace','News','Games','Entertainment']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):

        top = add_topic()

        fake_url = fake_gen.url()
        fake_date = fake_gen.date()
        fake_name = fake_gen.company()

        wp = Webpage.objects.get_or_create(topic=top,name=fake_name,url=fake_url)[0]
        ar = AccessRecord.objects.get_or_create(name=wp,date=fake_date)[0]

def populate_user(N=10):
    for entry in range(N):
        fake_f_name = fake_gen.first_name()
        fake_l_name = fake_gen.last_name()
        fake_email = fake_gen.email()

        u = User.objects.get_or_create(first_name=fake_f_name,last_name=fake_l_name,email=fake_email)

if __name__ == '__main__':
    print("Populating Script!!!")
    #populate(20)
    populate_user(10)
    print("Populating Complete!!!")
