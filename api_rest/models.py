from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True, null=False)

    def __str__(self):
        return (
            f"id: {self.id}"
            f"first_name: {self.first_name}"
            f"last_name: {self.last_name}"
            f"email: {self.email}"
        )
