from django.db import models

class Contact(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    country = models.TextField()
    email = models.EmailField(primary_key=True)
    contactnumber = models.CharField(max_length=10)
    query = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.country} {self.email} {self.contactnumber} {self.query}"