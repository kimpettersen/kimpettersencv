# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Education'
        db.create_table('education_education', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('university', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.CharField')(max_length=13)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('education', ['Education'])


    def backwards(self, orm):
        # Deleting model 'Education'
        db.delete_table('education_education')


    models = {
        'education.education': {
            'Meta': {'object_name': 'Education'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'end_date': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'university': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['education']