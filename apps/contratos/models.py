from django.db import models
from apps.clientes.models import Cliente
from apps.operaciones.models import Cajon

class Contrato(models.Model):
    """Contratos entre clientes y cajones"""
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name='contratos'
    )
    cajon = models.ForeignKey(
        Cajon,
        on_delete=models.PROTECT,
        related_name='contratos'
    )
    fecha_inicio = models.DateField()
    monto_mensual = models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'tbl_contratos'
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'
        constraints = [
            models.UniqueConstraint(
                fields=['cajon', 'activo'],
                condition=models.Q(activo=True),
                name='unique_cajon_activo'
            )
        ]
    
    def __str__(self):
        return f"Contrato {self.cliente.nombre} - Cajón {self.cajon.numero}"
