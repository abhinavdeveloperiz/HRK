from django.db import models

# Create your models here.
class Head(models.Model):
    image = models.ImageField(upload_to='head/')
    left=models.ImageField(upload_to="head/")
    right=models.ImageField(upload_to="head/")
    def __str__(self):
        return f"Head Section {self.id}"
    

class student_gallery(models.Model):
    image = models.ImageField(upload_to='student_gallery/')
    def __str__(self):
        return f"Student Image {self.id}"


class office_gallery(models.Model):
    image = models.ImageField(upload_to='office_gallery/')
    def __str__(self):
        return f"Office Image {self.id}"
    
    
class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')
    fees=models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    duration = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    topic1=models.CharField(max_length=100, blank=True, null=True)
    topic2=models.CharField(max_length=100, blank=True, null=True)  
    topic3=models.CharField(max_length=100, blank=True, null=True)
    topic4=models.CharField(max_length=100, blank=True, null=True)
    topic5=models.CharField(max_length=100, blank=True, null=True)
    topic6=models.CharField(max_length=100, blank=True, null=True)
    topic7=models.CharField(max_length=100, blank=True, null=True)
    topic8=models.CharField(max_length=100, blank=True, null=True)
    topic9=models.CharField(max_length=100, blank=True, null=True)
    topic10=models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonial/', blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Mentor_image(models.Model):
    image=models.ImageField(upload_to="mentors_image")