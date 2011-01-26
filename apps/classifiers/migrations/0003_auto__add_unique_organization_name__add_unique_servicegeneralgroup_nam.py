# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding unique constraint on 'Organization', fields ['name']
        db.create_unique('classifiers_organization', ['name'])

        # Adding unique constraint on 'ServiceGeneralGroup', fields ['name']
        db.create_unique('classifiers_servicegeneralgroup', ['name'])

        # Adding unique constraint on 'Service', fields ['name']
        db.create_unique('classifiers_service', ['name'])

        # Adding unique constraint on 'Stock', fields ['name']
        db.create_unique('classifiers_stock', ['name'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Stock', fields ['name']
        db.delete_unique('classifiers_stock', ['name'])

        # Removing unique constraint on 'Service', fields ['name']
        db.delete_unique('classifiers_service', ['name'])

        # Removing unique constraint on 'ServiceGeneralGroup', fields ['name']
        db.delete_unique('classifiers_servicegeneralgroup', ['name'])

        # Removing unique constraint on 'Organization', fields ['name']
        db.delete_unique('classifiers_organization', ['name'])


    models = {
        'classifiers.organization': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Organization'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '512'})
        },
        'classifiers.service': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Service'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '512'}),
            'servicegeneralgroup': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'services'", 'null': 'True', 'to': "orm['classifiers.ServiceGeneralGroup']"})
        },
        'classifiers.servicegeneralgroup': {
            'Meta': {'ordering': "('name',)", 'object_name': 'ServiceGeneralGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '512'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['classifiers.ServiceGeneralGroup']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'classifiers.stock': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Stock'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '256'})
        }
    }

    complete_apps = ['classifiers']
