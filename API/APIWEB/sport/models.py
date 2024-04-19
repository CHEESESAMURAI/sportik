from django.db import models


class User(models.Model):
    id_user = models.IntegerField()
    first_name = models.TextField(max_length=15)
    sur_name = models.TextField(max_length=15)
    last_name = models.TextField(max_length=15)
    age = models.TextField(max_length=15)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    lsport = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.first_name


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    #about = models.TextField(max_length=100)
    #place = models.ForeignKey('place', on_delete=models.PROTECT, null=True)
    #discroption = models.TextField(max_length=15)
    #price = models.TextField(max_length=15)

    def __str__(self):
        return self.name

#class place(models.Model):
    #name = models.CharField(max_length=100, db_index=True)
    #about = models.TextField(max_length=100)
    #discroption = models.TextField(max_length=15)

    #def __str__(self):
        #return self.name