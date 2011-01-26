# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ServiceGeneralGroup'
        db.create_table('classifiers_servicegeneralgroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('classifiers', ['ServiceGeneralGroup'])

        # Adding model 'Service'
        db.create_table('classifiers_service', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('servicegeneralgroup', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='services', null=True, to=orm['classifiers.ServiceGeneralGroup'])),
        ))
        db.send_create_signal('classifiers', ['Service'])

        # Adding model 'Stock'
        db.create_table('classifiers_stock', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('classifiers', ['Stock'])

        # Adding model 'Organization'
        db.create_table('classifiers_organization', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=512)),
        ))
        db.send_create_signal('classifiers', ['Organization'])


    def backwards(self, orm):
        
        # Deleting model 'ServiceGeneralGroup'
        db.delete_table('classifiers_servicegeneralgroup')

        # Deleting model 'Service'
        db.delete_table('classifiers_service')

        # Deleting model 'Stock'
        db.delete_table('classifiers_stock')

        # Deleting model 'Organization'
        db.delete_table('classifiers_organization')


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
