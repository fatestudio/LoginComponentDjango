# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table('try_user', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('major', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('student_status', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('ucsb_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('gmail_account', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('qq_account', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('renren_account', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('facebook_account', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('profile_photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('try', ['User'])

        # Adding model 'Admin'
        db.create_table('try_admin', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['try.User'])),
        ))
        db.send_create_signal('try', ['Admin'])

        # Adding model 'NewStudent'
        db.create_table('try_newstudent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['try.User'])),
            ('arrival_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('arrival_method', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('try', ['NewStudent'])

        # Adding model 'Album'
        db.create_table('try_album', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['try.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('try', ['Album'])

        # Adding model 'Photo'
        db.create_table('try_photo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['try.User'])),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['try.Album'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('img', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('try', ['Photo'])

        # Adding model 'Event'
        db.create_table('try_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['try.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=50000)),
            ('begin_date', self.gf('django.db.models.fields.TimeField')()),
            ('end_date', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal('try', ['Event'])

        # Adding M2M table for field album on 'Event'
        db.create_table('try_event_album', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm['try.event'], null=False)),
            ('album', models.ForeignKey(orm['try.album'], null=False))
        ))
        db.create_unique('try_event_album', ['event_id', 'album_id'])

        # Adding model 'File'
        db.create_table('try_file', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['try.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=50000)),
            ('_file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('try', ['File'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table('try_user')

        # Deleting model 'Admin'
        db.delete_table('try_admin')

        # Deleting model 'NewStudent'
        db.delete_table('try_newstudent')

        # Deleting model 'Album'
        db.delete_table('try_album')

        # Deleting model 'Photo'
        db.delete_table('try_photo')

        # Deleting model 'Event'
        db.delete_table('try_event')

        # Removing M2M table for field album on 'Event'
        db.delete_table('try_event_album')

        # Deleting model 'File'
        db.delete_table('try_file')


    models = {
        'try.admin': {
            'Meta': {'object_name': 'Admin'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['try.User']"})
        },
        'try.album': {
            'Meta': {'object_name': 'Album'},
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['try.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'try.event': {
            'Meta': {'object_name': 'Event'},
            'album': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['try.Album']", 'symmetrical': 'False'}),
            'begin_date': ('django.db.models.fields.TimeField', [], {}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['try.User']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50000'}),
            'end_date': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'try.file': {
            'Meta': {'object_name': 'File'},
            '_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['try.User']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'try.newstudent': {
            'Meta': {'object_name': 'NewStudent'},
            'arrival_method': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'arrival_time': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['try.User']"})
        },
        'try.photo': {
            'Meta': {'object_name': 'Photo'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['try.Album']"}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['try.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'try.user': {
            'Meta': {'object_name': 'User'},
            'facebook_account': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'gmail_account': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'major': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'profile_photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'qq_account': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'renren_account': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'student_status': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ucsb_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'})
        }
    }

    complete_apps = ['try']