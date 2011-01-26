# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Unitmeas'
        db.create_table('classifiers_unitmeas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=500)),
        ))
        db.send_create_signal('classifiers', ['Unitmeas'])

        # Adding field 'Service.unitmeas'
        db.add_column('classifiers_service', 'unitmeas', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['classifiers.Unitmeas'], null=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'Unitmeas'
        db.delete_table('classifiers_unitmeas')

        # Deleting field 'Service.unitmeas'
        db.delete_column('classifiers_service', 'unitmeas_id')


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
            'servicegeneralgroup': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'services'", 'null': 'True', 'to': "orm['classifiers.ServiceGeneralGroup']"}),
            'unitmeas': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['classifiers.Unitmeas']", 'null': 'True'})
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
        },
        'classifiers.unitmeas': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Unitmeas'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '500'})
        }
    }

    complete_apps = ['classifiers']
