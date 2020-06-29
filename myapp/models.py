from django.db import models

class MyModel(models.Model):
    file=models.FileField(upload_to='files/encrypted')
    password=models.CharField(max_length=100,blank=True,null=True,default=None)

class DecryptModel(models.Model):
    encryptedFile=models.FileField(upload_to='files/decrypted')
    password=models.CharField(max_length=100,blank=True,null=True,default=None)
