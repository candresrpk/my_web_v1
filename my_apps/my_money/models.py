from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Cartera(models.Model):
    nombre = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)


    def saldo_actual(self):
        movimientos = Movimiento.objects.filter(cartera=self)
        saldo = 0
        for movimiento in movimientos:
            if movimiento.movimiento == Movimiento.MovimientoChoices.INGRESO:
                saldo += movimiento.monto
            else:
                saldo -= movimiento.monto
        return saldo
    
    def saldo_por_mes(self, year, month):
        movimientos = Movimiento.objects.filter(cartera=self, fecha_creacion__year=year, fecha_creacion__month=month)
        saldo = 0
        for movimiento in movimientos:
            if movimiento.movimiento == Movimiento.MovimientoChoices.INGRESO:
                saldo += movimiento.monto
            else:
                saldo -= movimiento.monto
        return saldo
    
    def movimientos_por_categoria(self, categoria):
        movimientos = Movimiento.objects.filter(cartera=self, categoria=categoria)
        return movimientos
    
    class Meta:
        verbose_name_plural = "Carteras"

    def __str__(self):
        return f"cartera de {self.usuario.username} - {self.nombre}"


class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    cartera = models.ForeignKey(Cartera, on_delete=models.CASCADE)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Descripciones"

    def save(self, *args, **kwargs):
        self.texto = self.texto.lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.texto


class Movimiento(models.Model):
    
    class MovimientoChoices(models.TextChoices):
        INGRESO = 'Ingreso', 'Ingreso'
        GASTO = 'Gasto', 'Gasto'

    
    cartera = models.ForeignKey(Cartera, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    movimiento = models.CharField(max_length=20, choices=MovimientoChoices.choices)
    


    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    
    def save(self, *args, **kwargs):
        self.descripcion = self.descripcion.lower()
        super().save(*args, **kwargs)


    class Meta:
        verbose_name_plural = "Movimientos"
        
        

    def __str__(self):
        return f"{self.fecha_creacion} - {self.categoria} - {self.monto} - {self.movimiento}"