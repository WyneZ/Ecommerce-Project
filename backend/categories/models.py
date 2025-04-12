from django.db import models


class Category(models.Model):
    category_name = models.CharField(200)
    category_code = models.CharField(20) # must be all uppercase
    description = models.TextField(null=True, default=None)
    parent_id = models.IntegerField(null=True) # for sub categories
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name