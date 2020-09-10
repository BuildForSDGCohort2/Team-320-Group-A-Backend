from django.db import models
from django.utils.crypto import get_random_string

from django.utils.translation import gettext_lazy as _

# Create your models here.
import hospital
from authentication.models import User


class Patient(models.Model):
    date_admitted = models.DateField(_('Date Issued'),
                                     help_text=_('Date of Registration'),
                                     auto_now_add=True)
    code_no = models.CharField(_('Registration No'), max_length=255, default=get_random_string(length=5), unique=True,
                               db_index=True)
    surname = models.CharField(_('Surname'), max_length=30)
    middle_name = models.CharField(_('Middle Name'), max_length=30)
    first_name = models.CharField(_('First Name'), max_length=30)
    phone_number = models.CharField(_('Phone Number'), max_length=14)
    email = models.EmailField(_('Email Address'), max_length=255, unique=True, db_index=True)
    occupation = models.CharField(_('Occupation'), max_length=255, )
    GENDER_CHOICES = (
        (u'M', u'Male'),
        (u'F', u'Female'),
    )
    gender = models.CharField(_('Sex'), max_length=2, choices=GENDER_CHOICES)
    Age = models.IntegerField(_('Age'))
    dob = models.DateField(_('Date of Birth'))
    MARITAL_CHOICES = (
        (u'M', u'Married'),
        (u'S', u'Single'),
    )
    marital_status = models.CharField(_('Marital Status'), max_length=2, choices=MARITAL_CHOICES)
    BLOOD_CHOICES = (
        (u'A', u'A'),
        (u'B', u'B'),
        (u'AB', u'AB'),
        (u'O', u'O'),
    )
    blood_group = models.CharField(_('Blood Group'), max_length=2, choices=BLOOD_CHOICES)
    GENOTYPE_CHOICES = (
        (u'AO', u'AO'),
        (u'AA', u'AA'),
        (u'BO', u'BO'),
        (u'BB', u'BB'),
        (u'AB', u'AB'),
        (u'OO', u'OO'),
    )
    genotype = models.CharField(_('GENOTYPE'), max_length=2, choices=GENOTYPE_CHOICES)
    hospitals = models.ForeignKey('hospital.Hospital', null=True, blank=True, on_delete=models.CASCADE,
                                  )
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)


class HospitalHistory(models.Model):
    code_no = models.CharField(_('Registration No'), max_length=255, default=get_random_string(length=5))

    date_admitted = models.DateField(_('Date Admitted'),
                                     help_text=_('Date patient was admitted'),
                                     )
    reffered_by = models.CharField(_('Reffered By'), max_length=255)
    doctor = models.CharField(_('Doctor or Surgeon'), max_length=255)
    ward = models.CharField(_('Ward or Clinic'), max_length=255)

    date_discharged = models.DateField(_('Date Discharged'),
                                       help_text=_('Date of discharge'), default=None, blank=True, null=True)

    discharged_to = models.CharField(_('Discharged To'), max_length=255)
    condition = models.TextField(_('Patient Condition on discharge'))
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='patients')


class Diagnosis(models.Model):
    diagnosis_date = models.DateTimeField(_('Date of diagnosis'),
                                          default=None, blank=True, null=True)
    diagnosis = models.TextField(_('Report on diagnosis'))
    code_no = models.CharField(_('Patient code No'),
                               help_text=_('Alphanumeric length of 5.'), max_length=5)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='patients')
