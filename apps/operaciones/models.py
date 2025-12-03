from django.db import models
# Ya no necesitas importar ValidationError si no vas a validar nada extra aquí

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
    
    # ELIMINAMOS el método clean() o lo dejamos vacío si no hay más reglas
    # Django ya valida automáticamente que 'numero' no se repita (unique=True) y que no exceda 10 caracteres.

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