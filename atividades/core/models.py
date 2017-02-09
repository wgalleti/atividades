from django.db import models
from django.contrib.auth.models import User

class Level(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Priority(models.Model):
    name = models.CharField(max_length=255)
    severity = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class Cluster(models.Model):
    name = models.CharField(max_length=255)
    related = models.ForeignKey('self', null=True, blank=True)

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    user = models.ForeignKey(User)
    date_start = models.DateTimeField(auto_now_add=True)
    date_finish = models.DateTimeField(null=True, blank=True)
    status = models.ForeignKey(Status)

    def __str__(self):
        return self.title

def task_directory_path(instance, filename):
    return '{0}/{1}'.format(instance.task.id, filename)

class TaskAttachment(models.Model):
    task = models.ForeignKey(Task)
    file = models.FileField(upload_to=task_directory_path)

    def __str__(self):
        return self.task.title

class TaskConfig(models.Model):
    task = models.OneToOneField(Task, primary_key=True)
    priority = models.ForeignKey(Priority)
    sponsor = models.ForeignKey(User, related_name='sponsor')
    planned_hours = models.FloatField()
    planned_start = models.DateTimeField()
    level = models.ForeignKey(Level)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.task.title

class TaskProgress(models.Model):
    task = models.ForeignKey(Task)
    text = models.TextField()
    user = models.ForeignKey(User)
    status = models.ForeignKey(Status)
    work_start = models.DateTimeField(null=True, blank=True)
    work_end = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.task.status = self.status
        super(TaskProgress, self).save(self, *args, **kwargs)

    def __str__(self):
        return self.task.title