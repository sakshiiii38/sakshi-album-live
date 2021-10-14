from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200 , null=False, blank=False)

    def _str_(self):
        return self.name


class photo(models.Model):
    category = models.ForeignKey(Category, on_delete = models.SET_NULL , null=True, blank=True)
    image = models.ImageField(blank=False, null=False)
    description = models.TextField()

    def _str_(self):
        return self.description