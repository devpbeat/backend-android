from django.db import models

# Create your models here.

GENDER_OPTION = (
        ('Masculino','Masculino'),
        ('Femenino','Femenino'),
        ('Otro','Otro',)
    ) 

class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
    

class Person(models.Model):
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    birth_date = models.DateField()
    address = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField()
    gender = models.CharField(max_length=200,
                              choices=GENDER_OPTION,
                              default='No especificado')
    user = models.OneToOneField('auth.User', on_delete=models.PROTECT, null=True, blank=True)
    document_number = models.CharField(max_length=200)


    class Meta:
        abstract = True

    def __str__(self):
        return self.name

