from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Todo(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_todos")
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assigned_todos")
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True, null=True)
    add_file=models.FileField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({'Done' if self.is_completed else 'Pending'})"



# class Todo(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos")
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     is_completed = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     due_date = models.DateTimeField(blank=True, null=True)

#     # def __str__(self):
#         # return f"{self.title} ({'Done' if self.is_completed else 'Pending'})"

# class AssignedTodo(models.Model):
#     todo=models.ForeignKey(Todo,on_delete=models.CASCADE, related_name='assignments')
#     assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todo_assignments")

