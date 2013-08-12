
# Create your models here.
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=80)
    birthday = models.DateField()
    def __unicode__(self):
        return u"%s was born in %s" % (self.name, self.birthday.strftime("%B of %Y"))
    def as_dict(self):
        return {'name':self.name, 'birthday':self.birthday.strftime("%B of %Y")}