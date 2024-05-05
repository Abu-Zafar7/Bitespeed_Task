from django.db import models


class Contact(models.Model):
    phoneNumber = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    linkedId = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    linkPrecedence = models.CharField(max_length=10, choices=(('primary', 'primary'), ('secondary', 'secondary')), default='primary')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    deletedAt = models.DateTimeField(null=True, blank=True)
    

    def __str__(self) -> str:
        return self.email