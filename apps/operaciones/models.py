from django.db import models
from django.core.exceptions import ValidationError

class Cajon(models.Model):
    """Espacios físicos de estacionamiento"""
    ESTADOS = [
        ('FUNCIONAL', 'Funcional'),
        ('MANTENIMIENTO', 'Mantenimiento'),
    ]
    
    numero = models.CharField(max_length=10, unique=True)
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='FUNCIONAL'
    )
    descripcion = models.TextField(blank=True)
    
    def clean(self):
        super().clean()
        if self.numero is not None:
            try:
                # Forzar a entero para la comparación, sea cual sea la fuente
                numero = int(self.numero)
            except (TypeError, ValueError):
                raise ValidationError({'numero': 'El número del cajón debe ser un número entero válido.'})
            if numero <= 0:
                raise ValidationError({'numero': 'El número del cajón debe ser mayor que cero.'})

    class Meta:
        db_table = 'tbl_cajones'
        verbose_name = 'Cajón'
        verbose_name_plural = 'Cajones'
        ordering = ['numero']
    
    def __str__(self):
        return f"Cajón {self.numero}"
    
    @property
    def ocupado(self):
        """Verifica si el cajón tiene un contrato activo"""
        return self.contratos.filter(activo=True).exists()
