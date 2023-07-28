from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 36, blank = False, unique = True)
    description = models.TextField(max_length = 256, blank = True)
    price = models.DecimalField(max_digits = 3, decimal_places = 2, default = 0)
    published = models.DateField(blank = True, null = True, default = None)
    is_published = models.BooleanField(default = False)
    cover = models.ImageField(upload_to = "covers/", blank = True)

    # 這個方式可以在管理者進入 Book管理介面時，列表中指定呈現特定欄位 (方便查看)
    def __str__(self):
        return self.title