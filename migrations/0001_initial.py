# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'department'
        db.create_table(u'eForm_department', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('no', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eForm.department'], null=True, blank=True)),
        ))
        db.send_create_signal(u'eForm', ['department'])

        # Adding model 'staff'
        db.create_table(u'eForm_staff', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sid', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('current_year_balance', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=1)),
            ('last_years_balance', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=1)),
            ('pending_deduction', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=1)),
            ('supervisor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eForm.staff'], null=True, blank=True)),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eForm.department'])),
        ))
        db.send_create_signal(u'eForm', ['staff'])

        # Adding model 'supervisor_list'
        db.create_table(u'eForm_supervisor_list', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('supervisor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eForm.staff'])),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('memo', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
        ))
        db.send_create_signal(u'eForm', ['supervisor_list'])

        # Adding model 'request_form'
        db.create_table(u'eForm_request_form', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('request_no', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eForm.staff'])),
            ('staff_id', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('supervisor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eForm.supervisor_list'])),
            ('leave_type', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('date_from', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 14, 0, 0))),
            ('date_from_am', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_from_pm', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_to', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 14, 0, 0))),
            ('date_to_am', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_to_pm', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('attachment', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('remark', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
        ))
        db.send_create_signal(u'eForm', ['request_form'])

        # Adding model 'acts'
        db.create_table(u'eForm_acts', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('acting_person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eForm.staff'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('duty', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('acted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eForm.request_form'])),
            ('memo', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
        ))
        db.send_create_signal(u'eForm', ['acts'])


    def backwards(self, orm):
        # Deleting model 'department'
        db.delete_table(u'eForm_department')

        # Deleting model 'staff'
        db.delete_table(u'eForm_staff')

        # Deleting model 'supervisor_list'
        db.delete_table(u'eForm_supervisor_list')

        # Deleting model 'request_form'
        db.delete_table(u'eForm_request_form')

        # Deleting model 'acts'
        db.delete_table(u'eForm_acts')


    models = {
        u'eForm.acts': {
            'Meta': {'object_name': 'acts'},
            'acted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'acting_person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['eForm.staff']"}),
            'duty': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'memo': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['eForm.request_form']"})
        },
        u'eForm.department': {
            'Meta': {'object_name': 'department'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'no': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['eForm.department']", 'null': 'True', 'blank': 'True'})
        },
        u'eForm.request_form': {
            'Meta': {'object_name': 'request_form'},
            'attachment': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'date_from': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 8, 14, 0, 0)'}),
            'date_from_am': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'date_from_pm': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_to': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 8, 14, 0, 0)'}),
            'date_to_am': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_to_pm': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leave_type': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['eForm.staff']"}),
            'remark': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'request_no': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'staff_id': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'supervisor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['eForm.supervisor_list']"})
        },
        u'eForm.staff': {
            'Meta': {'object_name': 'staff'},
            'current_year_balance': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '1'}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['eForm.department']"}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_years_balance': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '1'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'pending_deduction': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '1'}),
            'sid': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'supervisor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['eForm.staff']", 'null': 'True', 'blank': 'True'})
        },
        u'eForm.supervisor_list': {
            'Meta': {'object_name': 'supervisor_list'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'memo': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'supervisor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['eForm.staff']"})
        }
    }

    complete_apps = ['eForm']