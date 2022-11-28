# Django
from django.db import models

# Project
from apps.authors.models import Author
from apps.categories.models import Category

LANGUAGE = [
    ('EN', 'English'),
    ('UZ', 'Uzbek'),
    ('RU', 'Russian')
]


class Product(models.Model):
    name = models.CharField("Book Name", max_length=200)
    category = models.ManyToManyField(Category, related_name='category', verbose_name="Book Category")
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, verbose_name="Book Author")
    description = models.TextField("Book Description")

    file = models.FileField("File of this Book", upload_to="files/books/%Y/%m/%d")
    image = models.ImageField("Image of this Book", upload_to='files/images/%Y/%m/%d')
    video = models.FileField("Video of this Book", upload_to='files/videos/%Y/%m/%d', blank=True, null=True)

    year = models.IntegerField("Year of Publication of the Book")
    language = models.CharField("Language od Book", max_length=7, choices=LANGUAGE)
    size = models.FloatField("Book Size (DO NOT WRITE)", blank=True, null=True)
    size_type = models.CharField("Type of Book Size (DO NOT WRITE)", max_length=10, blank=True, null=True)
    file_type = models.CharField("Type of Book File (DO NOT WRITE)", max_length=20, blank=True, null=True)

    rate = models.IntegerField("Rate. (DO NOT WRITE)", blank=True, null=True)

    created_date = models.DateTimeField("Created Date", auto_now_add=True)
    last_update = models.DateTimeField("Last Update", auto_now=True)

    def __str__(self):
        return f'name: {self.name},' \
               f'category:z {self.category},' \
               f'created_date: {self.created_date}'

    def save(self, *args, **kwargs):
        x = self.file.size
        y = 512000
        if x < y:
            self.size = round(x/1000, 2)
            self.size_type = "kb"
        elif x < y*1000:
            self.size = round(x/1000000, 2)
            self.size_type = "mb"
        else:
            self.size = round(x/1000000000, 2)
            self.size_type = "gb"

        self.file_type = str(self.file).split(".")[-1].upper()
        super(Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
