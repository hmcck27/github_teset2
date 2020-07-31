from django.db import models
from django.conf import settings
from items.models import Item

# 둘중에 하나만 import 적용 둘다하면 안댐
# Create your models here.

'''
is_purchasable의 설정 방법
1. review가 만들어질때, is_purchasable 필드의 default 값을 함수를 통해서 결정
--> 하지만 함수의 인자로 self를 넘길 수가 없다. 아직 self가 생기지 않았기 때문?
    def get() :
        
        if Item.brand.first().is_partner == True :
            return True
        return False
'''

class Review(models.Model) :
    title = models.TextField(max_length=100)
    content = models.TextField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_purchasable = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True) 
    
    def get_purchase_url(self) :
        return self.item.purchase_url

'''
2. 인스턴스가 만들어지는 순간 self.is_purchasable 값 조정....
-> document에는 __init__을 함부러 override 하지 말라고 한다,,,

    def __init__(self, *args, **kwargs) :
        if self.item.brand.is_partner == True:
            self.is_purchasable = True
        else :
            self.is_purchasable = False
        super().__init__(*args,**kwargs)
        for key in kwargs:
           setattr(self, key, kwargs[key])
'''


'''
3. save함수를 override?
-> create 에는 괜찮지만 update시에도 save()가 쓰이기때문에 안된다. brand의 is_partner의 값이 변하지 않는이상
is_purchasable도 바꿀 수 없다. 이는 후에 함수 update_review_availability를 쓸모없게 한다,,,

    def save(self, *args, **kwargs):
        if self.item.brand.is_partner == True :
            self.is_purchasable = True
        else :
            self.is_purchasable = False

        super().save(*args,**kwargs)
'''     



