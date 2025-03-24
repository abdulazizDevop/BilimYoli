from django.db import models
from django.forms import TextInput, ModelForm

# Create your models here.
class Settings(models.Model):
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    phone = models.CharField(blank=True, max_length=20)
    email = models.CharField(blank=True, max_length=100)
    address = models.CharField(blank=True, max_length=255)
    youtue = models.CharField(blank=True, max_length=100)
    telegram = models.CharField(blank=True, max_length=100)
    instagram = models.CharField(blank=True, max_length=100)
    facebook = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.title
    

class ContactMessage(models.Model):
    STATUS = (('New', 'New'),
              ('Read', 'Read'),
              ('Closed', 'Closed'),
    )
    name = models.CharField(blank=True, max_length=20)
    phone = models.CharField(blank=True, max_length=20)
    subject = models.CharField(blank=True, max_length=50)
    message = models.TextField(blank=True, max_length=255)
    email = models.CharField(blank=True, max_length=50)
    status = models.TextField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    


class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'phone', 'subject', 'message', 'email']
        widjets = {
            'name': TextInput(attrs={'class': 'input', 'placeholder': 'Enter your name'}),
            'phone': TextInput(attrs={'class': 'input', 'placeholder': 'Enter phone number'}),
            'subject': TextInput(attrs={'class': 'input', 'placeholder': 'Enter your Subject'}),
            'message': TextInput(attrs={'class': 'input', 'placeholder': 'Your Message', 'rows': '5'}),
            'email': TextInput(attrs={'class': 'input', 'placeholder': 'Enter your email'})
        }



class Cuorses(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(blank=True, upload_to='images/')
    price = models.IntegerField()
    day = models.TextField()
    oportunities = models.TextField()

    def __str__(self):
        return self.title
