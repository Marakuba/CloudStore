# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Invoice.invoicetype'
        db.add_column('operations_invoice', 'invoicetype', self.gf('django.db.models.fields.CharField')(default=1, max_length=1), keep_default=False)

        # Changing field 'Invoice.create'
        db.alter_column('operations_invoice', 'create', self.gf('django.db.models.fields.DateTimeField')())


    def backwards(self, orm):
        
        # Deleting field 'Invoice.invoicetype'
        db.delete_column('operations_invoice', 'invoicetype')

        # Changing field 'Invoice.create'
        db.alter_column('operations_invoice', 'create', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))


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
            'cost': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'count': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['operations.Invoice']"}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['classifiers.Service']"}),
            'stock': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['classifiers.Stock']"})
        },
        'operations.invoice': {
            'Meta': {'ordering': "('create',)", 'object_name': 'Invoice'},
            'comment': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'create': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 1, 27, 17, 25, 52, 857854)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoicetype': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['classifiers.Organization']"})
        }
    }

    complete_apps = ['operations']
