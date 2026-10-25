from django.db import models

# Create your models here.

class JobDb(models.Model):
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    job_type_choices = (
                        ('full_time','Full Time'),
                        ('part_time','Part Time'),
                        ('internship','Internship')
                        )
    job_type = models.CharField(max_length=100,choices=job_type_choices) 
    experience_choices = (
                          ('fresher','Fresher'),
                          ('experienced','Experienced'))
    experience_level = models.CharField(max_length=100,choices=experience_choices)
    salary = models.PositiveIntegerField()
    department = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    published_date = models.DateTimeField(auto_now_add=True)

class ApplicationDb(models.Model):
    applicant_name = models.CharField(max_length=100)
    applicant_email = models.EmailField()
    job = models.IntegerField()
    qualification = models.CharField(max_length=100)
    experience_years = models.PositiveIntegerField(default=0)
    status_choices = (
                       ('pending','Pending'),
                       ('shortlisted','Shortlisted'),
                       ('rejected','Rejected'),
                       ('selected','Selected')
                     )
    status = models.CharField(max_length=100,choices=status_choices,default='pending')
    application_date = models.DateTimeField(auto_now_add=True)
