from django.db import models

# Create your models here.

class StockFunds(models.Model):
    date=models.DateField(auto_now=False)
    name=models.CharField(max_length=200,null=True,blank=True)
    Account_No = models.CharField(max_length=12)
    ifsc=models.CharField(max_length=10)
    panNo=models.CharField(max_length=10)
    price=models.DecimalField(max_digits=7444,decimal_places=2,null=True,blank=True)
    user_email=models.CharField(max_length=100,null=True,blank=True)

class AmountAccount(models.Model):
    date=models.DateField(auto_now=False)
    price=models.DecimalField(max_digits=733,decimal_places=2,null=True,blank=True)
    loss=models.CharField(max_length=50)
    profit=models.CharField(max_length=100)
    user_email=models.CharField(max_length=100)



class Stock_form(models.Model):
    buy_sell=models.CharField(max_length=100,choices=(('sell','sell'),
                                                  ('buy','buy'),
                                                  ))
    stock_name=models.CharField(max_length=200)
    date=models.DateField(auto_now=False)
    buy_price=models.DecimalField(max_digits=10,decimal_places=2,blank=True ,null=True)
    sell_price=models.DecimalField(max_digits=10,decimal_places=2,blank=True ,null=True)
    amount=models.CharField(max_length=50)
    profit=models.CharField(max_length=100)
    buy_quantity=models.IntegerField(max_length=50,blank=True ,null=True)
    sell_quantity=models.IntegerField(max_length=50,blank=True,null=True)
    loss=models.CharField(max_length=50)
    user_email=models.CharField(max_length=100)





    


    



    

