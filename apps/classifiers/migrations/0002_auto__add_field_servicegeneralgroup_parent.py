# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'ServiceGeneralGroup.parent'
        db.add_column('classifiers_servicegeneralgroup', 'parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, to=orm['classifiers.ServiceGeneralGroup']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'ServiceGeneralGroup.parent'
        db.delete_column('classifiers_servicegeneralgroup', 'parent_id')


    models = {
        'classifiers.organization': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Organization'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        'classifiers.service': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Service'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'servicegeneralgroup': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'services'", 'null': 'True', 'to': "orm['classifiers.ServiceGeneralGroup']"})
        },
        'classifiers.servicegeneralgroup': {
            'Meta': {'ordering': "('name',)", 'object_name': 'ServiceGeneralGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['classifiers.ServiceGeneralGroup']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'classifiers.stock': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Stock'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['classifiers']
