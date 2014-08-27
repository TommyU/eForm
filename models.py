# -*- coding: utf-8 -*-
from django.db import models
import datetime
# Create your models here.

class department(models.Model):
    no = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length= 50)
    parent = models.ForeignKey('self',null=True,blank=True)

    def __str__(self):
        return "[%s] %s" % (self.no, self.name)

    def __unicode__(self):
        return u'[%s] %s' % (self.no, self.name)

class staff(models.Model):
    sid = models.CharField(max_length= 20)
    name = models.CharField(max_length= 20)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    current_year_balance = models.DecimalField(max_digits=5,decimal_places=1)
    last_years_balance = models.DecimalField(max_digits=5,decimal_places=1)
    pending_deduction = models.DecimalField(max_digits=5,decimal_places=1)
    supervisor = models.ForeignKey('self', null=True, blank=True)
    department = models.ForeignKey(department)

    def __str__(self):
        return "[%s] %s" % (self.sid, self.name)

    def __unicode__(self):
        return u'[%s] %s' % (self.sid, self.name)

class supervisor_list(models.Model):
    supervisor = models.ForeignKey(staff)
    active = models.BooleanField(default=True)
    memo = models.CharField(max_length=512,null=True,blank=True)
    def __str__(self):
        return "[%s] %s" % (self.supervisor.sid, self.supervisor.name)

    def __unicode__(self):
        return u'[%s] %s' % (self.supervisor.sid, self.supervisor.name)
from django.utils.translation import ugettext_lazy as _
class request_form(models.Model):
    request_no = models.CharField(max_length=20, verbose_name=_("request no"))
    name = models.ForeignKey(staff, verbose_name=_("name"))
    staff_id = models.CharField(max_length=20, verbose_name=_("applier"))
    supervisor = models.ForeignKey(supervisor_list, verbose_name=_("supervisor"))
    LEAVE_TYPE_CHOICES = (
        ('Sick leave','Sick leave'),
        ('Marrage leave','Marrage leave')
    )
    leave_type = models.CharField(max_length=32,choices=LEAVE_TYPE_CHOICES, verbose_name=_("leave type"))
    date_from = models.DateField(default=datetime.date.today() + datetime.timedelta(3), verbose_name=_("date from"))
    date_from_am = models.BooleanField(default=True, verbose_name=_("from am"))
    date_from_pm = models.BooleanField(default=False, verbose_name=_("from pm"))
    date_to = models.DateField(default=datetime.date.today() + datetime.timedelta(3), verbose_name=_("date to"))
    date_to_am = models.BooleanField(default=False, verbose_name=_("to am"))
    date_to_pm = models.BooleanField(default=True, verbose_name=_("to pm"))
    attachment = models.FileField(blank=True,upload_to='generate_filename',null=True, verbose_name=_("attachment"))
    remark = models.CharField(max_length=256, null=True, blank=True, verbose_name=_("remark"))

    def __str__(self):
        return "[%s] %s" % (self.leave_type, self.name.name)

    def __unicode__(self):
        return u'[%s] %s' % (self.leave_type, self.name.name)


class acts(models.Model):
    acting_person = models.ForeignKey(staff)
    name = models.CharField(max_length=20)
    duty = models.CharField(max_length=256)
    acted = models.BooleanField(default=False)
    report = models.ForeignKey(request_form)
    memo = models.CharField(max_length=512,null=True, blank=True)

class saturday_off_request(models.Model):
    request = models.ForeignKey(request_form)
    is_off = models.BooleanField(default=False,verbose_name=_('off'))
    day = models.DateField(_('day'))

#class leave_request(models.Model):

