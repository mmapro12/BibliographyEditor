from django.db import models

# Create your models here.
class Book(models.Model):
    author_nickname = models.TextField() # Meşhur isim
    author_full_name = models.TextField() # Tam isim
    book_name = models.TextField() # Kitap Adı
    skin = models.TextField() # Cilt
    print_place = models.TextField() # Basım yeri
    printer = models.TextField() # Yayıncı
    print_year = models.TextField() # yıl
    press = models.TextField() # Baskı
    thk = models.TextField(null=True, blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.book_name[:30]
