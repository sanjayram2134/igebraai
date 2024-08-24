from django.db import models

class ChatMessage(models.Model):
    user = models.CharField(max_length=100)  # Name or ID of the user
    message = models.TextField()  # The chat message
    timestamp = models.DateTimeField(auto_now_add=True)  # When the message was sent

    def __str__(self):
        return f'{self.user}: {self.message} ({self.timestamp})'