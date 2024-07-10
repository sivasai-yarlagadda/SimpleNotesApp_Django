from django.db import models
from django.shortcuts import reverse,redirect

# Create your models here.
LABEL_CHOICES = (
    ('P', 'Primary'),
    ('SE', 'Secondary'),
    ('S', 'Success'),
    ('DA', 'Danger'),
    ('W', 'Warning'),
    ('I', 'Info'),
    ('L', 'light'),
    ('D', 'dark')
)


class Note(models.Model):
    title = models.CharField(max_length=100)
    due_date = models.DateTimeField()
    # image = models.ImageField(upload_to='images/')
    label = models.CharField(choices=LABEL_CHOICES, max_length=2)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_finish_item_url(self):
        return reverse("finish-note-item",kwargs={
            'id':self.id
        })
    def get_recover_item_url(self):
        return reverse("recover-note-item",kwargs={
            'id':self.id
        })
    def get_delete_item_url(self):
        return reverse("delete-note-item",kwargs={
            'id':self.id
        })

    