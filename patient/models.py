from django.db import models

from django.utils.translation import gettext_lazy as _


# Create your models here.
class HospitalHistory(models.Model):
    date_admitted = models.DateField(_('Date Admitted'),
                                     help_text=_('Date patient was admitted'),
                                     )
    reffered_by = models.CharField(_('Reffered By'), max_length=255)
    doctor = models.CharField(_('Doctor or Surgeon'), max_length=255)
    ward = models.CharField(_('Ward or Clinic'), max_length=255)

    date_discharged = models.DateTimeField(_('Date Discharged'),
                                           help_text=_('Date of discharge'), default=None, blank=True, null=True)

    discharged_to = models.CharField(_('Discharged To'), max_length=255)
    condition = models.TextField(_('Patient Condition on discharge'))


class Diagnosis(models.Model):
    diagnosis_date = models.DateTimeField(_('Date of diagnosis'),
                                          default=None, blank=True, null=True)
    diagnosis = models.TextField(_('Report on diagnosis'))
    code_no = models.CharField(_('Patient code No'),
                               help_text=_('Alphanumeric length of 5.'), max_length=5)
