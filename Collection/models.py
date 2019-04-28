from django.db import models
import uuid

class Products (models.Model):

    MYCOLORS = (
     ('green', 'GREEN'),
     ('red', 'RED'),
     ('black', 'BLACK'),
     ('blue', 'BLUE'),
    )

    MYSIZES = (
     ('small', 'SMALL'),
     ('large', 'LARGE'),
     ('extra-large', 'E-LARGE'),
    )
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    sizes = models.CharField(choices=MYSIZES, default='small', max_length=100)
    colors = models.CharField(choices=MYCOLORS, default='green', max_length=100)
    description = models.CharField(max_length=300)
    product_img = models.ImageField(default='default.jpg', blank=True)

    def __str__(self):
        return self.title
