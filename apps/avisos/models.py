from django.db import models
from apps.usuarios.models import Usuario

class Aviso(models.Model):
    """Avisos generales para todos los usuarios"""
    mensaje = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    # Opcional: Saber quién lo envió
    autor = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'tbl_avisos'
        verbose_name = 'Aviso'
        verbose_name_plural = 'Avisos'
        ordering = ['fecha_creacion'] # Orden cronológico (antiguos primero, como chat)

    def __str__(self):
        return f"Aviso {self.id} - {self.fecha_creacion.strftime('%d/%m/%Y')}"