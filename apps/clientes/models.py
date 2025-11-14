from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import re

class Cliente(models.Model):
    """Modelo principal de cliente/inquilino"""
    telefono_validator = RegexValidator(
        regex=r'^(?:\+52)?\s?(?:\(?\d{2,3}\)?[\s-]?)?\d{7}$',
        message='Ingrese un número de teléfono válido en formato mexicano, con o sin código de país +52.'
    )
    nombre_validator = RegexValidator(
        regex=r'^[A-Za-zÁÉÍÓÚáéíóúÑñÜü\s]+$',
        message='El nombre solo puede contener letras y espacios.'
    )
    nombre = models.CharField(
        max_length=100,
        validators=[nombre_validator]
    )

    telefono = models.CharField(
        max_length=15,
        validators=[telefono_validator]
    )

    def clean(self):
        #llamar al clean original para validar regex
        super().clean()

        #limpiar el campo telefono: quitar todo menos digitos
        telefono_limpio = re.sub(r'\D', '', self.telefono)

        if not (len(telefono_limpio) == 10 or (len(telefono_limpio) == 12 and telefono_limpio.startswith('52'))):
            raise ValidationError({
                'telefono': 'El teléfono debe contener 10 dígitos (lada + número) o 12 dígitos con código de país +52.'
            })
    
    direccion = models.TextField()
    def clean(self):
        if self.direccion and len(self.direccion) < 10:
            raise ValidationError({'direccion': "La dirección debe tener al menos 10 caracteres."})
        if self.direccion and not self.direccion.lower().startswith('calle'):
            raise ValidationError({'direccion': "La dirección debe iniciar con 'Calle' o incluir un formato similar."})
    correo = models.EmailField(unique=True)
    activo = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'tbl_clientes'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre


class Vehiculo(models.Model):
    """Vehículos asociados a clientes"""
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='vehiculos'
    )
    placa = models.CharField(max_length=20, unique=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    año = models.PositiveIntegerField()
    
    class Meta:
        db_table = 'tbl_vehiculos'
        verbose_name = 'Vehículo'
        verbose_name_plural = 'Vehículos'
    
    def __str__(self):
        return f"{self.placa} - {self.marca} {self.modelo}"


class Documento(models.Model):
    """Documentos asociados a clientes (fotos de contrato y vehículo)"""
    TIPOS_DOCUMENTO = [
        ('CONTRATO', 'Fotografía de Contrato'),
        ('VEHICULO', 'Fotografía de Vehículo'),
    ]
    
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='documentos'
    )
    tipo = models.CharField(max_length=20, choices=TIPOS_DOCUMENTO)
    archivo = models.FileField(upload_to='documentos/%Y/%m/%d/')
    fecha_subida = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'tbl_documentos'
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'
