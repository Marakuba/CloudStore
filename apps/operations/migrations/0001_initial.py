# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'InvoiceType'
        db.create_table('operations_invoicetype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=256)),
        ))
        db.send_create_signal('operations', ['InvoiceType'])

        # Adding model 'Invoice'
        db.create_table('operations_invoice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('create', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['classifiers.Organization'])),
            ('invoicetype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['operations.InvoiceType'])),
        ))
        db.send_create_signal('operations', ['Invoice'])

        # Adding model 'Entry'
        db.create_table('operations_entry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('invoice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['operations.Invoice'])),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['classifiers.Service'])),
            ('stock', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['classifiers.Stock'])),
            ('count', self.gf('django.db.models.fields.FloatField')()),
            ('comment', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal('operations', ['Entry'])


    def backwards(self, orm):
        
        # Deleting model 'InvoiceType'
        db.delete_table('operations_invoicetype')

        # Deleting model 'Invoice'
        db.delete_table('operations_invoice')

        # Deleting model 'Entry'
        db.delete_table('operations_entry')


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
        },
        'operations.entry': {
            'Meta': {'ordering': "('invoice',)", 'object_name': 'Entry'},
            'comment': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'count': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['operations.Invoice']"}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['classifiers.Service']"}),
            'stock': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['classifiers.Stock']"})
        },
        'operations.invoice': {
            'Meta': {'ordering': "('create',)", 'object_name': 'Invoice'},
            'create': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoicetype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['operations.InvoiceType']"}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['classifiers.Organization']"})
        },
        'operations.invoicetype': {
            'Meta': {'ordering': "('name',)", 'object_name': 'InvoiceType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '256'})
        }
    }

    complete_apps = ['operations']
