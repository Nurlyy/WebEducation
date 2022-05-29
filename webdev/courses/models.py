from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    class Meta:
        ordering=["title"]
        
    def __str__(self):
        return self.title


class Theme(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    first_title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    first_text = models.TextField()
    second_title = models.CharField(max_length=100, blank=True)
    second_text = models.TextField(blank=True)
    third_title = models.CharField(max_length=100, blank=True)
    third_text = models.TextField(blank=True)
    file_field = models.FileField(upload_to="files/", blank=True)
    video_url = models.URLField(blank=True)
    
    
    
    def remove_on_image_update(self):
        try:
            # is the object in the database yet?
            obj = Theme.objects.get(id=self.id)
        except Theme.DoesNotExist:
            # object is not in db, nothing to worry about
            return
        # is the save due to an update of the actual image file?
        if obj.file_field and self.file_field and obj.file_field != self.file_field:
            # delete the old image file from the storage in favor of the new file
            obj.file_field.delete()

    def delete(self, *args, **kwargs):
        # object is being removed from db, remove the file from storage first
        self.file_field.delete()
        return super(Theme, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        # object is possibly being updated, if so, clean up.
        self.remove_on_image_update()
        return super(Theme, self).save(*args, **kwargs)
    
    class Meta:
        ordering=["first_title"]
    
    def __str__(self):
        return self.first_title
    

class QuestionParent(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    theme=models.ForeignKey(Theme,on_delete=models.CASCADE)
    class Meta:
        ordering=["title"]
        
    def __str__(self):
        return self.title
    
    
class Question(models.Model):
    parent = models.ForeignKey(QuestionParent, on_delete=models.CASCADE)
    question=models.CharField(max_length=600)
    option1=models.CharField(max_length=200, null=False)
    option2=models.CharField(max_length=200, null=False)
    option3=models.CharField(max_length=200, null=False)
    option4=models.CharField(max_length=200, null=False)
    cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
    answer=models.CharField(max_length=200,choices=cat)
    class Meta:
        ordering=["question"]
        
    def __str__(self):
        return self.question    