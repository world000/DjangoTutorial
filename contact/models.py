from django.db import connection, models
from django.contrib.localflavor.us.models import USStateField

# Create your models here.

class PersonManager(models.Manager):
    def first_names(self, last_name):
        cursor = connection.cursor()
        cursor.execute("""
            select distinct first_name 
            from contact_person
            where last_name = %s""", [last_name])
        return [row[0] for row in cursor.fetchall()]

class Person(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(blank=False)
    address = models.CharField(max_length = 100)
    city = models.CharField(max_length = 50)
    state = USStateField()
    
    objects = PersonManager() 
    
    def baby_boomer_status(self):
        "Returns the person's baby-boomer status."
        if self.birth_date == None:
            return 'bad parameter'
        import datetime
        if datetime.date(1945, 8, 1) <= self.birth_date <= datetime.date(1964, 12, 31):
            return 'Baby bommer'
        if self.birth_date < datetime.date(1945, 8, 1):
            return 'Pre-boomer'
        return 'Post-boomer'
    
    def is_midwestern(self):
        "Return True if the person is from the Midwest."
        return self.state in ('IL', 'WI', 'MI', 'IN', 'OH', 'IA', 'MO')
    
    def _get_full_name(self):
        "Return the person's full name."
        return u'%s %s' % (self.first_name, self.last_name)
    full_name = property(_get_full_name)
