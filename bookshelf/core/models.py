from django.db import models

class Genre(models.Model):
    name = models.CharField(max_lenght=200)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_lenght=150)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    bio = models.TextField()
    picture = models.ImageField(verbose_name='Author Image',
                                blank=True, 
                                upload_to='people/authors',
                                default='/people/default.jpg')

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_lenght=300)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    summary = models.TextField()
    rating = models.FloatField(default=0)
    genre = models.ManyToManyField(Genre)
    isbn = models.CharField('ISBN', max_lenght=13, unique=True)
    book_cover = models.ImageField(verbose_name='Book Cover',
                                   blank=True, 
                                   upload_to='books',
                                   default='/books/default.jpg')

class Review(models.Model):
    pass