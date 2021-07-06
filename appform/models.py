from django.db import models

# Create your models here.

class Application_Form(models.Model):
    l_name = models.CharField('Last Name', max_length=100)
    m_name = models.CharField('Middle Name', max_length=100)
    f_name = models.CharField('First Name', max_length=100)
    gender = models.CharField('Gender', max_length=100)
    date_of_birth = models.CharField('Date of Birth', max_length=100)
    school = models.CharField('School', max_length=100)
    classification = models.CharField('Classification', max_length=50)
    sport = models.CharField('Sport', max_length=50)
    position = models.CharField('Position', max_length=60)
    email = models.EmailField('Email', max_length=100)
    phone_number = models.CharField('Phone Number', max_length=30)
    address_1 = models.CharField('Address 1', max_length=100)
    address_2 = models.CharField('Address 2', max_length=100)
    city = models.CharField('City', max_length=100)
    state = models.CharField('State', max_length=100)
    zipcode = models.CharField('Zipcode', max_length=100)
    sport_background = models.TextField('Please Describe Your Sport Background', max_length=300)
    sport_play = models.TextField('What Other Sports You have Played in the Past', max_length=200)
    dominant_hand = models.CharField('What is Your Dominant Hand', max_length=100)
    programs = models.CharField('Please Choose Program(s) You are Interested', max_length=100)

    def __str__(self):
        return self.l_name
