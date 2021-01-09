from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=300, blank=True)




    def save_author(self):
        self.save()

    def delete_author(self):
        self.delete()

    @classmethod
    def search_by_photo_category(cls,search_term):
        photo = cls.objects.filter(name__icontains = search_term)
        return photo

    def update_image(self, Name=None, category=None):
        self.name = Name if Name else self.Name
        self.photo_category = category if category else self.photo_category 
        self.save() 

    def __str__(self):
        return self.first_name


class Picture(models.Model):
    image = models.ImageField(upload_to= 'pictures/')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    location = models.ForeignKey(Location,on_delete = models.CASCADE,)
    category = models.ForeignKey(Category, on_delete = models.CASCADE,)
    author = models.ForeignKey(Author,on_delete = models.CASCADE)


    
