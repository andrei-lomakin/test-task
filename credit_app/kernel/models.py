from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contract(models.Model):
    contract_id = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Создаем CreditApplication, если его еще нет
        if not hasattr(self, 'credit_application'):
            CreditApplication.objects.create(contract=self)

    def __str__(self):
        return self.contract_id


class CreditApplication(models.Model):
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE, related_name='credit_application')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Credit Application for Contract {self.contract.contract_id}"


class Product(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='products')
    credit_application = models.ForeignKey(CreditApplication, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
