from django.db import models
from django.conf import settings 
from django.utils import timezone



class Applicant(models.Model):
    ''' Model for applicants personal data '''
    application_no = models.CharField(primary_key=True, max_length=20)
    date = models.DateField(default=timezone.now())
    post = models.CharField(max_length=100)
    department = models.CharField(max_length=20)
    Research_Domain=models.TextField(default=None)
    
    def __str__(self):
        return str(self.application_no)

class Research_Exp(models.Model):
    '''Model for the research experience of the applicant''' 
    From = models.CharField(max_length=20)
    to = models.CharField(max_length=20)
    applicant = models.ForeignKey(Applicant, 
                                on_delete=models.CASCADE,
                                related_name='research_exp',
                )
    duration = models.CharField(max_length=20)
    def __str__(self):
        return str(self.applicant)

class Seminar_Articles(models.Model):
    '''Model for the details of seminars taken by the applicant'''
    article_title = models.TextField()
    seminar_subject = models.TextField()
    location = models.CharField(max_length=100)
    duration = models.CharField(max_length=20)
    published = models.TextField()
    applicant = models.ForeignKey(Applicant, 
                                on_delete=models.CASCADE,
                                related_name='seminar_articles',
                )
    duration = models.CharField(max_length=20)
    def __str__(self):
        return str(self.applicant)

class Newspaper_Article(models.Model):
    article_title = models.TextField()
    journal_name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    date_published = models.CharField(max_length=20)
    referred = models.TextField()
    level=models.CharField(max_length=20)
    naas = models.TextField()
    isbn_issn = models.TextField()
    applicant = models.ForeignKey(Applicant, 
                                on_delete=models.CASCADE,
                                related_name='newspaper_article',
                )
    def __str__(self):
        return str(self.applicant)

class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    date_publish = models.CharField(max_length=20)
    isbn= models.TextField()
    applicant = models.ForeignKey(Applicant, 
                                on_delete=models.CASCADE,
                                related_name='books',
                )
    def __str__(self):
        return str(self.applicant)

class Chapters(models.Model):
    book_title = models.CharField(max_length=100)
    chapter = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    date_of_publisher = models.CharField(max_length=100)
    isbn_issn = models.TextField()
    applicant = models.ForeignKey(Applicant, 
                                on_delete=models.CASCADE,
                                related_name='applicant',
                )
    def __str__(self):
        return str(self.applicant)

class Educational_qualifications(models.Model):
    ''' Model for educational qualifications of applicant.'''
    degree = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    marks = models.CharField(max_length=10)
    subjects = models.CharField(max_length=200)
    year_of_passing = models.IntegerField()
    applicant = models.ForeignKey(Applicant, 
                                on_delete=models.CASCADE,
                                related_name='Educational_qualifications',
                )
    def __str__(self):
        return str(self.applicant.name)


class Employment_exp(models.Model):
    '''Model for Employment experience of applicant'''
    name = models.CharField(max_length=200)
    post = models.CharField(max_length=250)
    from_year = models.IntegerField()
    to_year = models.IntegerField()
    salary = models.IntegerField()
    nature = models.CharField(max_length=200)
    applicant = models.ForeignKey(Applicant, 
                                on_delete=models.CASCADE,
                                related_name='Employment_exp',
                )

    def __str__(self):
        return str(self.applicant.name)


class General(models.Model):
    full_name = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now())
    father_name = models.CharField(max_length=200)
    address_perm = models.CharField(max_length=200)
    telephone_perm = models.CharField(max_length=20)
    address_mail = models.CharField(max_length=200)
    telephone_mail = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    marital_status = models.CharField(max_length = 10,choices = (
                                                        ("Married", "Married"),
                                                        ("Not Married", "Not Married"),
                                                        ))
    nationality = models.CharField(max_length=20)
    state = models.CharField(max_length=50)
    category = models.CharField(max_length = 10,choices = (
                                                        ("General", "General"),
                                                        ("OBC-CL", "OBC-CL"),
                                                        ("OBC-NCL", "OBC-NCL"),
                                                        ("ST", "ST"),
                                                        ("SC", "SC"),
                                                        ("Gen-PwD", "Gen-PwD"),
                                                        ("OBC-CL-PwD", "OBC-CL-PwD"),
                                                        ("OBC-NCL-PwD", "OBC-NCL-PwD"),
                                                        ("ST-PwD", "ST-Pwd"),
                                                        ("SC-PwD", "SC-PwD"),
                                                        ))
    reservation = models.CharField(max_length = 3,choices = (
                                                        ("Yes", "Yes"),
                                                        ("No", "No"),
                                                        ))
    present_employer = models.CharField(max_length=200)
    applicant = models.ForeignKey(Applicant, 
                                on_delete=models.CASCADE,
                                related_name='General',
                )
    def __str__(self):
        return str(self.applicant.full_name)


class PhD(models.Model):
    PhD_awarded = models.CharField(max_length = 3,choices = (
                                                        ("Yes", "Yes"),
                                                        ("No", "No"),
                                                        ))
    title_of_thesis = models.CharField(max_length=100)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='PhD')


class other_info(models.Model):
    membership = models.TextField()
    responsibilities = models.TextField()
    academic_year_break = models.TextField()
    college_punishment = models.TextField()
    judicial_punishment = models.TextField()
    unfit_for_position = models.TextField()
    references = models.TextField()
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='other_info')

class sponsored_project(models.Model):
    tot_number = models.CharField(max_length=10)
    ongoing = models.TextField()
    completed = models.TextField()
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='sponsored_project')
    def __str__(self):
        return str(self.applicant)    

class Experiments(models.Model):
    tot_number = models.CharField(max_length=10)
    ongoing = models.TextField()
    completed = models.TextField()
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='Experiments')
    def __str__(self):
        return str(self.applicant)
class Thesis(models.Model):
    ongoing_phd = models.TextField()
    completed_phd = models.TextField()
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='Thesis')
    def __str__(self):
        return str(self.applicant)
class administrative_details(models.Model):
    details = models.TextField()
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='administrative_details')
    def __str__(self):
        return str(self.applicant)



# class File(models.Model):
#     applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='files')
#     publications = models.FileField(upload_to='uploads/', null=True, blank=True)
#     image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    # caste_certificate = models.FileField(upload_to='uploads/', null=True, blank=True)