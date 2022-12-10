from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Tag(models.Model):
    label = models.CharField(max_length=255)



# Para hacer la relacion con una clase de la otra aplicacion, se puede importar en este modulo from store.models import Product, pero para garantizar la independencia entre apps. esta app no deberia tener ninguna relacion con la otra 
# Se debe utilizar una manera generica de identificar el objeto a relacionar, por ende: se utiliza contenType el cual es una app 
class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE) 
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
# content_type, Oobject_id y content_object son necesaios para crear la relacion gnerica 


