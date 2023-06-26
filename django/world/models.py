from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    countrycode = models.CharField(max_length=15, blank=False, null=False)
    district = models.CharField(max_length=15, blank=False, null=False)
    population = models.IntegerField(blank=False, null=False)
  
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'city'

class Country(models.Model):
    CONTINENT = (
        ('Asia', 'Asia'),
        ('Europe', 'Europe'),
        ('North America', 'North America'),
        ('Africa', 'Africa'),
        ('Oceania', 'Oceania'),
        ('Antarctica', 'Antarctica'),
        ('South America', 'South America'),

    )
    code = models.CharField(max_length=3, blank=False, null=False,default='')
    name = models.CharField(max_length=52, blank=False, null=False,default='')
    continent = models.CharField(max_length=20, choices=CONTINENT, null=False, default="Asia")
    region = models.CharField(max_length=26, blank=False, null=False,default='')
    surfacesrea = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00) 
    indepyear = models.SmallIntegerField(default=None)
    population = models.IntegerField(default=0)
    lifeexpectancy = models.DecimalField(max_digits=3, decimal_places=1, default=None) 
    gnp = models.DecimalField(max_digits=10, decimal_places=2, default=None) 
    gnpold = models.DecimalField(max_digits=10, decimal_places=2, default=None) 
    localname = models.CharField(max_length=45, default='')
    governmentform = models.CharField(max_length=45, default=None)
    headofstate = models.CharField(max_length=60, default='')
    capital = models.IntegerField(default=None)
    Code2 = models.CharField(max_length=2, blank=False, null=False,default='')


    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'country'


class CountryLanguage(models.Model):
    IsOfficial = (
        ('T', 'T'),
        ('F', 'F'),
      

    )
    countrycode = models.CharField(max_length=3, blank=False, null=False,default='')
    language = models.CharField(max_length=15, blank=False, null=False)
    continent = models.CharField(max_length=10, choices=IsOfficial, null=False, default="F")
    gnpold = models.DecimalField(max_digits=4, decimal_places=1, null=False, default=0.0)

  
    def __str__(self):
        return self.countrycode
    
    class Meta:
        db_table = 'countrylanguage'