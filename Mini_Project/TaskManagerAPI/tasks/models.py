from django.db import models





class Task(models.Model):
    class Task_Status(models.TextChoices):
        DONE = ('D', 'Done')
        NOT_DONE = ('ND', 'Not Done')
        WORKING_ON_IT = ('W', 'Working on it')
        STUCK = ('S', 'Stuck')
    class Priority(TextChoices):
        URGENT = ('U', 'Urgent')
        IMPORTANT = ('I', 'Important')
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices = Task_Status.choices,  default=Task_Status.NOT_DONE)
    priority = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)

