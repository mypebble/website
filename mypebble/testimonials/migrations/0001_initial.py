# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Testimonial'
        db.create_table('testimonials_testimonial', (
            ('quote_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cmsplugin_randomquote.Quote'], unique=True, primary_key=True)),
            ('quote_text_full', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('testimonials', ['Testimonial'])


    def backwards(self, orm):
        # Deleting model 'Testimonial'
        db.delete_table('testimonials_testimonial')


    models = {
        'cmsplugin_randomquote.quote': {
            'Meta': {'object_name': 'Quote'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'author_url': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quote_text': ('django.db.models.fields.TextField', [], {})
        },
        'testimonials.testimonial': {
            'Meta': {'object_name': 'Testimonial', '_ormbases': ['cmsplugin_randomquote.Quote']},
            'quote_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cmsplugin_randomquote.Quote']", 'unique': 'True', 'primary_key': 'True'}),
            'quote_text_full': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['testimonials']