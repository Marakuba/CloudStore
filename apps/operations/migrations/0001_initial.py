# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Invoice'
        db.create_table('operations_invoice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('create', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 1, 27, 23, 26, 20, 330888))),
            ('organization', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['classifiers.Organization'])),
            ('stock', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['classifiers.Stock'])),
            ('invoicetype', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('comment', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal('operations', ['Invoice'])

        # Adding model 'Entry'
        db.create_table('operations_entry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('invoice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['operations.Invoice'])),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['classifiers.Service'])),
            ('count', self.gf('django.db.models.fields.FloatField')()),
            ('cost', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2)),
        ))
        db.send_create_signal('operations', ['Entry'])


    def backwards(self, orm):
        
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
            'cost': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'count': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['operations.Invoice']"}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['classifiers.Service']"})
        },
        'operations.invoice': {
            'Meta': {'ordering': "('create',)", 'object_name': 'Invoice'},
            'comment': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'create': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 1, 27, 23, 26, 20, 330888)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoicetype': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['classifiers.Organization']"}),
            'stock': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['classifiers.Stock']"})
        }
    }

    complete_apps = ['operations']
