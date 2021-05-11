from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=150)
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
    title = models.CharField(max_length=300)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    summary = models.TextField()
    rating = models.FloatField(default=0)
    genre = models.ManyToManyField(Genre)
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    book_cover = models.ImageField(verbose_name='Book Cover',
                                   blank=True, 
                                   upload_to='books',
                                   default='/books/default.jpg')
    
    def __str__(self):
        return self.title

class Rating(models.Model):
    # status = models.
    pass

class Review(models.Model):
    pass
