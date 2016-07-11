from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# This code is triggered whenever a new user has been created and saved to the database
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
# Create your models here.

class Article(models.Model):
    name = models.CharField(max_length=50)
    idtype = models.ForeignKey('TypeArticle', models.DO_NOTHING, db_column='idtype')

    class Meta:
        managed = False
        db_table = 'article'


class DetailArticle(models.Model):
    idresto = models.ForeignKey('Structure', models.DO_NOTHING, db_column='idresto', unique=True)
    idarticle = models.ForeignKey(Article, models.DO_NOTHING, db_column='idarticle', unique=True)
    prix = models.FloatField()
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'detail_article'


class DetailSession(models.Model):
    idsess = models.ForeignKey('Session', models.DO_NOTHING, db_column='idsess')
    tache = models.CharField(max_length=250)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'detail_session'


class Evenement(models.Model):
    libelle = models.CharField(max_length=250)
    description = models.TextField()
    idtype = models.ForeignKey('TypeEvenement', models.DO_NOTHING, db_column='idtype', unique=True)
    idstruct = models.IntegerField(unique=True)
    dateexec = models.DateTimeField()
    location = models.FloatField()

    class Meta:
        managed = False
        db_table = 'evenement'


class Session(models.Model):
    iduser = models.ForeignKey('Utilisateur', models.DO_NOTHING, db_column='iduser')
    debut = models.DateTimeField()
    fin = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'session'


class Structure(models.Model):
    name = models.CharField(max_length=250)
    adresse = models.CharField(max_length=250)
    phone = models.CharField(max_length=20)
    location = models.FloatField()
    idtype = models.ForeignKey('TypeStructure', models.DO_NOTHING, db_column='idtype', unique=True)
    idadmin = models.ForeignKey('Utilisateur', models.DO_NOTHING, db_column='idadmin', unique=True)
    email = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'structure'


class TypeArticle(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'type_article'


class TypeEvenement(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'type_evenement'


class TypeStructure(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'type_structure'


class TypeUser(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'type_user'


class Utilisateur(models.Model):
    name = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    idtype = models.ForeignKey(TypeUser, models.DO_NOTHING, db_column='idtype')

    class Meta:
        managed = False
        db_table = 'utilisateur'