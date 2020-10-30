from django.db import models

# Create your models here.
class FundingProgramTbl(models.Model):
    program_name = models.TextField(max_length=1000)
    about_program = models.TextField(max_length=5000)
    who_can_apply = models.TextField(max_length=5000)
    deadline = models.TextField(max_length=5000)
    how_to_apply = models.TextField(max_length=5000)
    link = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.program_name

