from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class Author(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    bio = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
#choices needed as a tuple of tuples. the first value is the value stored in the DB and the second value is the human readable form
    GENRE_CHOICE = (
        ("fiction", "Fiction"),
        ("adventure", "Adventure"),
        ("action", "Action")
    )

    STATUS_CHOICES = (
        ('available', 'Available'),
        ('borrowed', 'Borrowed')
    )

    title = models.CharField(max_length=250)
    genre = models.CharField(max_length=200, choices=GENRE_CHOICE)
    publication_year = models.IntegerField()
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default='available')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def clean(self):
        if self.publication_year > timezone.now().year:
            raise ValidationError(
                {
                    "publication_year" : "Publication Year can't be larger than the current year"
                }
            )

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Member(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    membership_date = models.DateField()
    email = models.EmailField()

    def clean(self):
        if self.membership_date > timezone.now().date():
            raise ValidationError(
                {
                    "membership_date" : "Memebership date can't be in the future"
                }
            )
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class BorrowRecord(models.Model):
    borrow_date = models.DateField(default=timezone.now().date())
    return_date = models.DateField(blank=True, null=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="book_records")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="member_records")

    def clean(self):
        if self.return_date and self.return_date < self.borrow_date:
            raise ValidationError(
                {"return_date": "Return date cannot be larger than borrow date"}
                )
        
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.id
    



