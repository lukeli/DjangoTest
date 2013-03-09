from django.db import models


class Author(models.Model):
    auth_name = models.CharField(max_length=100)

    def __str__(self):
        return self.auth_name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author)  # Many-to-one relationship
    """
    # Pull a book off the shelf - see below in this chapter for details on querying
    book = Book.objects.get(title="Moby Dick")
    # Get the book’s author - very simple
    author = Book.author
    # Get a set of the books the author has been credited on
    books = author.book_set.all()
    """
    def __str__(self):
        return self.title

class Book2(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)  # Many-to-Many relationship
    """
    # Pull a book off the shelf
    book = Book.objects.get(title="Python Web Development Django")
    # Get the books’ authors
    authors = Book.author_set.all()
    # Get all the books the third author has worked on
    books = authors[2].book_set.all()
    """

    def __str__(self):
        return self.title


class Author2(models.Model):
    auth_name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.auth_name


class Author3(models.Model):
    auth_name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book2)

    def __str__(self):
        return self.auth_name

class Book3(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author, through="Book3Authoring")

    def __str__(self):
           return self.title

class Book3Authoring(models.Model):
   book3 = models.ForeignKey(Book3)
   author = models.ForeignKey(Author)

   def __str__(self):
       return self.author.auth_name +': '+self.book3.title

