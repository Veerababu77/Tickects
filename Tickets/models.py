from django.db import models
import uuid
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length = 50, unique = True)
    phone_number = models.CharField(max_length = 10, null = True, blank = True)
    password = models.CharField(max_length = 20)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    profile = models.ImageField( upload_to = 'profiles/', null = True, blank = True)
    unique_id = models.UUIDField(default = uuid.uuid4, unique= True,null = True, blank = True)
    user_status = models.BooleanField(default = True)
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-created']
        
class TicketsModel(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'tickets')
    ticket_id = models.UUIDField(default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    ticket_status = models.CharField(max_length = 20, choices = (
        ('open','open'),
        ('close','close'),
        ('in_progress','in_progress')), default = 'open')
    ticket_mode = models.CharField(max_length = 20, choices = (
        ('urgent','urgent'),
        ('low','low'),
        ('medium','medium')), default = 'low')
    ticket_title = models.TextField(max_length= 250, null = True, blank = True)
    ticket_description = models.TextField(max_length= 250, null = True, blank = True)
    
    
    def __str__(self):
        return self.ticket_title
    
    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
        ordering = ['-created']
        
    
    
    
