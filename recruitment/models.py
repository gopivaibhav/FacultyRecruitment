from django.db import models
from django.conf import settings 
from django.utils import timezone

class Applicant(models.Model):
    ''' Model for applicants personal data '''
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=10)
    email_address = models.EmailField(max_length=255)
    gender = models.CharField(max_length=1,
                                choices=[
                                            ('M','Male'),
                                            ('F','Female'),
                                            ('O','Other'),
                                        ]
                            )
    category = models.CharField(max_length=25,
                                choices = [
                                        ('GEN', 'General'),
                                        ('SC','SC'),
                                        ('ST','ST'),
                                        ('OBC-CL', 'OBC Creamy Layer'),
                                        ('OBC-NCL', 'OBC Non Creamy Layer'),
                                        ('GEN-PWD','General Person with disabilties'),
                                        ('OBC-CL-PWD','OBC Creamy Layer Person with disabilites'),
                                        ('OBC-NCL-PWD','OBC Non Creamy Layer Person with disabilites'),
                                        ('SC-PWD','SC person with disabilites'),
                                        ('ST-PWD', 'ST person with disabilites'),
                                    ],
            )
    reservation = models.CharField(max_length=25,
                                choices = [
                                        ('GEN', 'General'),
                                        ('SC','SC'),
                                        ('ST','ST'),
                                        ('OBC-NCL', 'OBC Non Creamy Layer'),
                                        ('PWD','General Person with disabilties'),
                                        ('SERVICE','Ex-Service Man'),
                                        ('GEN-ECO', 'General Category Economically Weaker Sections'),
                                        ],
                                null=True,
                                blank=True,
            )
    current_address = models.TextField()
    permanent_address = models.TextField()

class Academic_detail(models.Model):
    applicant = models.ForeignKey(Applicant, 
                                on_delete=models.CASCADE,
                                related_name='academic_detail',
                )
    degree = models.CharField(max_length=200),
    area_of_qualification = models.CharField(max_length=200),
    #category of university
    name_of_institute = models.CharField(max_length=200),
    status = models.CharField(max_length=200, 
                            choices=[
                                    ('Passed', 'Passed'),
                                    ('Pursuing', 'Pursuing'),
                                ],
            )
    year_of_passing = models.IntegerField()
    division = models.CharField(max_length=10,
                                choices=[
                                       ('I','I'),
                                       ('II', 'II'),
                                       ('III', 'III'),
                                    ],
            )
    percentage = models.IntegerField()
    cgpa = models.FloatField()

class Profession_detail(models.Model):
    applicant = models.ForeignKey(Applicant, 
                                on_delete=models.CASCADE,
                                related_name='professional_detail',
                )
    organisation = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    from_year = models.IntegerField()
    to_year = models.IntegerField()
    role = models.CharField(max_length=250)
    pay_scale = models.IntegerField()
    #Emoluments
class Teaching_and_research_detail(models.Model):
    applicant = models.ForeignKey(Applicant, 
                                on_delete=models.CASCADE,
                                related_name='teaching_and_research_detail',
                )
    course_title = models.CharField(max_length=200)
    level = models.CharField(max_length=2,
                            choices=[
                                ('UG', 'Undergraduate'),
                                ('PG', 'Postgraduate'),
                                ],
            )
    sole_instructor = models.CharField(max_length=1,
                                        choices=[
                                            ('Y','Yes'),
                                            ('N','No'),
                                            ],
            )
    developer_of_course = models.CharField(max_length=1,
                                            choices=[
                                                ('Y','Yes'),
                                                ('N','No'),
                                                ],
            )
    role = models.CharField(max_length=200)
    pay_scale = models.IntegerField()
    #emoluments = models.
   
