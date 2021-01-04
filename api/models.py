from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class Prodect(models.Model):
    PRDName=models.CharField(max_length=15,verbose_name=_('prodect name'))
    PRDcatogre=models.ForeignKey('Catecory',on_delete=CASCADE,blank=True,null=True)
    PRDDEC=models.TextField(blank=True,null=True)
    ImageProdect=models.ImageField(upload_to='prodects/',blank=True,null=True)
    PRDPrice=models.DecimalField(max_digits=5,decimal_places=2,verbose_name=_('price'))
    PRDdiscoust=models.DecimalField(max_digits=5,decimal_places=2,verbose_name=_('Discount price'))
    PRDcost=models.DecimalField(max_digits=5,decimal_places=2,verbose_name=_('cost'))
    PRDcreate=models.DateTimeField(verbose_name=_('time create'))
    PRDslug=models.SlugField(blank=True,null=True)
    PRDnew=models.BooleanField(default=True)
    PRDbest=models.BooleanField(default=True)
    def save(self, *args, **kwargs):
        if not self.PRDslug:
            self.PRDslug=slugify(self.PRDName)
        super(Prodect,self).save(*args, **kwargs)

        
    def __str__(self) -> str:return self.PRDName
class ProdectImage(models.Model):
    Iprodect=models.ForeignKey(Prodect,on_delete=models.CASCADE)
    ImageProdect=models.ImageField(upload_to='prodects/')
    def __str__(self) -> str: return str(self.Iprodect)


class Catecory(models.Model):
    CTName=models.CharField(max_length=15)
    CTperans=models.ForeignKey('self',limit_choices_to={"CTperans__isnull":True},on_delete=CASCADE,blank=True,null=True)
    CTdescripation=models.TextField()
    CtImage=models.ImageField(upload_to='categore/')
    def __str__(self) -> str:return self.CTName


class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    def __str__(self):
        return self.name