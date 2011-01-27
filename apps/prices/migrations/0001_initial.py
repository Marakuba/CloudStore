# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Currency'
        db.create_table('prices_currency', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('prices', ['Currency'])

        # Adding model 'CurrRate'
        db.create_table('prices_currrate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('create', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 1, 27, 23, 26, 56, 101143))),
            ('rete', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2)),
            ('currency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prices.Currency'])),
        ))
        db.send_create_signal('prices', ['CurrRate'])

        # Adding model 'PriceType'
        db.create_table('prices_pricetype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(default=u'', max_length=50, db_index=True)),
            ('currency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prices.Currency'])),
        ))
        db.send_create_signal('prices', ['PriceType'])

        # Adding model 'PriceRete'
        db.create_table('prices_pricerete', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('create', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 1, 27, 23, 26, 56, 103745))),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['classifiers.Service'])),
            ('price', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2)),
            ('pricetype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prices.PriceType'])),
        ))
        db.send_create_signal('prices', ['PriceRete'])

        # Adding model 'ConvfactorRete'
        db.create_table('prices_convfactorrete', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('create', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 1, 27, 23, 26, 56, 105241))),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['classifiers.Service'])),
            ('convfactor', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2)),
        ))
        db.send_create_signal('prices', ['ConvfactorRete'])


    def backwards(self, orm):
        
        # Deleting model 'Currency'
        db.delete_table('prices_currency')

        # Deleting model 'CurrRate'
        db.delete_table('prices_currrate')

        # Deleting model 'PriceType'
        db.delete_table('prices_pricetype')

        # Deleting model 'PriceRete'
        db.delete_table('prices_pricerete')

        # Deleting model 'ConvfactorRete'
        db.delete_table('prices_convfactorrete')


    models = {
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
        'classifiers.unitmeas': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Unitmeas'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '500'})
        },
        'prices.convfactorrete': {
            'Meta': {'object_name': 'ConvfactorRete'},
            'convfactor': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'create': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 1, 27, 23, 26, 56, 105241)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['classifiers.Service']"})
        },
        'prices.currency': {
            'Meta': {'object_name': 'Currency'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'prices.currrate': {
            'Meta': {'object_name': 'CurrRate'},
            'create': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 1, 27, 23, 26, 56, 101143)'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['prices.Currency']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rete': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'})
        },
        'prices.pricerete': {
            'Meta': {'object_name': 'PriceRete'},
            'create': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 1, 27, 23, 26, 56, 103745)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'pricetype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['prices.PriceType']"}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['classifiers.Service']"})
        },
        'prices.pricetype': {
            'Meta': {'object_name': 'PriceType'},
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['prices.Currency']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "u''", 'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['prices']
