from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name





class Codeeditor(models.Model):
    title = models.CharField(max_length=50)
    description = RichTextUploadingField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    @staticmethod
    def get_all_products():
        return  Codeeditor.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return  Codeeditor.objects.filter(category=category_id)
        else:
            return  Codeeditor.get_all_products()