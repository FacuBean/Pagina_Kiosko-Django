from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=7,decimal_places=2)
    categoria = models.CharField(max_length=100)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return f"Producto: {self.nombre_producto} | Precio: {self.precio} | Categoria: {self.categoria} | Stock: {self.stock}"
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"Nombre: {self.nombre} | Email: {self.email} | Telefono: {self.telefono}"

class Venta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=1)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    

   # def __str__(self):
       # return f"{self.producto} x {self.cantidad} | {self.fecha}"