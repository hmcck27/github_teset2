from django.db import models
from django.conf import settings
##from posts.models import Review
# Create your models here.

class Brand(models.Model) :
    name = models.CharField(max_length = 100)
    is_partner= models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
    def update_sale_prices(self,amount) :
        qs = self.item_set.all()
        ##qs.update(sale_price = 100)
        for item in qs :
            if item.original_price < 100000 :
                item.sale_price = item.original_price - amount
                item.save()
        ##print(item)
        ##if(item.original_price > 100000) :
        print('above 100000 you can`t change the price!')
        ##else :

    

class Item(models.Model) :
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    purchase_url = models.URLField()
    image_url = models.URLField()
    is_soldout = models.BooleanField(default = False)
    original_price = models.PositiveIntegerField()
    sale_price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add = True)

    
    def __str__(self):
        return self.name

    def update_review_availability(self) :
        if self.is_soldout == True :
            review_list = self.review_set.all()
            review_list.update(is_purchasable = False)
        