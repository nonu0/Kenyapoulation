from django.db import models

# Create your models here.


class County(models.Model):
    name = models.CharField(max_length=50)
    area = models.FloatField()
    density = models.FloatField()
    houses = models.IntegerField()

    def __str__(self):
        return str(self.name)


class Population(models.Model):
    county = models.ForeignKey(County, on_delete=models.CASCADE)
    females = models.IntegerField()
    males = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return str(self.county)


class Provinces(models.Model):
    names = models.CharField(max_length=50)
    population = models.IntegerField()

    def __str__(self):
        return str(self.names)


class Central(models.Model):
    counties = models.CharField(max_length=50)
    area = models.FloatField(default=123.43)
    females = models.IntegerField()
    males = models.IntegerField()
    total_population = models.IntegerField()

    def __str__(self):
        return str(self.counties)


class Coast(models.Model):
    counties = models.CharField(max_length=50)
    area = models.FloatField(default=123.43)
    females = models.IntegerField()
    males = models.IntegerField()
    total_population = models.IntegerField()

    def __str__(self):
        return str(self.counties)


class RValley(models.Model):
    counties = models.CharField(max_length=50)
    area = models.FloatField(default=123.43)
    females = models.IntegerField()
    males = models.IntegerField()
    total_population = models.IntegerField()

    def __str__(self):
        return str(self.counties)


class Nyanza(models.Model):
    counties = models.CharField(max_length=50)
    area = models.FloatField(default=123.43)
    females = models.IntegerField()
    males = models.IntegerField()
    total_population = models.IntegerField()

    def __str__(self):
        return str(self.counties)


class Eastern(models.Model):
    counties = models.CharField(max_length=50)
    area = models.FloatField(default=123.43)
    females = models.IntegerField()
    males = models.IntegerField()
    total_population = models.IntegerField()

    def __str__(self):
        return str(self.counties)


class NEastern(models.Model):
    counties = models.CharField(max_length=50)
    area = models.FloatField(default=123.43)
    females = models.IntegerField()
    males = models.IntegerField()
    total_population = models.IntegerField()

    def __str__(self):
        return str(self.counties)


class Western(models.Model):
    counties = models.CharField(max_length=50)
    area = models.FloatField(default=123.43)
    females = models.IntegerField()
    males = models.IntegerField()
    total_population = models.IntegerField()

    def __str__(self):
        return str(self.counties)
