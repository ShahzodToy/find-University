from django.db import models
from common.models import BaseModel, Media
from django.core.validators import FileExtensionValidator


class University(BaseModel):
    class UniversityType(models.TextChoices):
        PRIVATE = 'private', 'Private'
        PUBLIC = 'public', 'Public'
        INTERNATIONAL = 'international', 'International'

    title = models.CharField(max_length=250)
    univer_type = models.CharField(max_length=120, choices=UniversityType.choices)
    date_registration = models.DateTimeField()
    contract_sum_range = models.CharField(max_length=120)
    license_pdf = models.FileField(upload_to='univer_license/', validators=[
        FileExtensionValidator(allowed_extensions=['pdf', 'doc'])
    ])
    description = models.TextField()
    grand_description = models.TextField()
    logo = models.ImageField(upload_to='univer_logo/')
    media_file = models.ManyToManyField(Media)
    contact_info = models.ForeignKey('ContactInfo', on_delete=models.CASCADE, related_name='universities')

    def __str__(self):
        return self.title


class ContactInfoDetail(BaseModel):
    name = models.CharField(max_length=120)
    link = models.URLField()
    logo = models.ImageField(upload_to='contact_info/', validators=[
        FileExtensionValidator(allowed_extensions=['jpg','web','png','jpeg'])
    ])


class ContactInfo(BaseModel):
    univer_info = models.ManyToManyField(ContactInfoDetail)
    longitute = models.CharField(max_length=120)
    langitute = models.CharField(max_length=120)
    social_media = models.ForeignKey('SocialMedia', on_delete=models.CASCADE, related_name='contact_infos')

    def __str__(self):
        return f'{self.universities.title} contact info'


class SocialMedia(BaseModel):
    name = models.CharField(max_length=120)
    link = models.URLField()

    def __str__(self):
        try:
            university = self.contact_infos.first().universities.first().title
            return f'Social media--{university}'
        except AttributeError:
            return 'Social media--No university linked'


class UniversityFaculty(BaseModel):
    class EducationDegree(models.TextChoices):
        BACHOLAR = 'bacholor', 'Bacholor'
        MAGISTRATURE = 'magistratura', 'Magistratura'

    title = models.CharField(max_length=120)
    degree = models.CharField(max_length=120, choices=EducationDegree.choices)
    description = models.TextField()
    education_lang = models.ManyToManyField('EducationLanguage')
    price_faculty_type = models.ManyToManyField('PriceFaculty')
    is_grant = models.BooleanField(default=False)
    requirements = models.TextField()

    def __str__(self):
        return f'{self.title} faculty'

    

class EducationLanguage(BaseModel):
    name = models.CharField(max_length=120)

    def __str__(self):
        return f'{self.name} language'


class PriceFaculty(BaseModel):
    name = models.CharField(max_length=120)
    price = models.CharField(max_length=120)

    def __str__(self):
        return f'{self.name} and {self.price}'


class UniversityDirections(BaseModel):
    title = models.CharField(max_length=120)
    logo = models.ImageField(upload_to='univer_direction/', validators=[
        FileExtensionValidator(allowed_extensions=['jpg','web','png','jpeg'])
    ])
    university_faculty = models.ManyToManyField(UniversityFaculty)

    def __str__(self):
        return f'{self.title} university direction'












