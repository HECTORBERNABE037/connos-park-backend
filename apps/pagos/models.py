from django.db import models
from apps.contratos.models import Contrato
from django.core.exceptions import ValidationError

class Pago(models.Model):
    """Historial de pagos recibidos"""
    contrato = models.ForeignKey(
        Contrato,
        on_delete=models.PROTECT,
        related_name='pagos'
    )
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField()
    periodo_inicio = models.DateField()
    periodo_fin = models.DateField()
    comentario = models.TextField(blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    def clean(self):
        super().clean()
        # Validación para que el monto sea positivo y mayor a cero
        if self.monto is not None and self.monto <= 0:
            raise ValidationError({'monto': 'El monto debe ser un valor positivo y mayor a cero.'})

    class Meta:
        db_table = 'tbl_pagos'
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'
        ordering = ['-fecha_pago']
    
    def __str__(self):
        return f"Pago ${self.contrato.cliente.nombre} - ${self.monto}"
