# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'saturday_off_request'
        db.create_table(u'eForm_saturday_off_request', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('request', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eForm.request_form'])),
            ('is_off', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('day', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'eForm', ['saturday_off_request'])


    def backwards(self, orm):
        # Deleting model 'saturday_off_request'
        db.delete_table(u'eForm_saturday_off_request')


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
            'date_from': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 8, 24, 0, 0)'}),
            'date_from_am': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'date_from_pm': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_to': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 8, 24, 0, 0)'}),
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
        u'eForm.saturday_off_request': {
            'Meta': {'object_name': 'saturday_off_request'},
            'day': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_off': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'request': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['eForm.request_form']"})
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