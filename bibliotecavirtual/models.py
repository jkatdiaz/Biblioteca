from django.db import models

class PNF(models.Model):
    nombre = models.CharField(max_length=255)
    codigo_alfanumerico = models.CharField(max_length=50)

class TipoDeLibro(models.Model):
    nombre = models.CharField(max_length=255)

class Editorial(models.Model):
    nombre = models.CharField(max_length=255)

class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    correo = models.EmailField(max_length=255)
    contrasena = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    pnf = models.ForeignKey(PNF, on_delete=models.CASCADE)

class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    fecha_publicacion = models.DateField()
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    tipo_de_libro = models.ForeignKey(TipoDeLibro, on_delete=models.CASCADE)
    pnf = models.ForeignKey(PNF, on_delete=models.CASCADE)

class Descarga(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_descarga = models.DateTimeField(auto_now_add=True)