from asyncio.windows_events import NULL

from django.db import models


class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.category_name}"

class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    publisher_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.publisher_name}"

class Books(models.Model):
    id = models.AutoField(primary_key=True)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.title}"

class Bookdetails(models.Model):
    book = models.OneToOneField(Books, on_delete=models.CASCADE, default=NULL)
    id = models.AutoField(primary_key=True)
    isbn = models.CharField(max_length=100)
    pages = models.IntegerField()
    language = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.isbn}"
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    books = models.ManyToManyField(Books)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.name}"
