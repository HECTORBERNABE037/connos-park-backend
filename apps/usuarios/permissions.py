from rest_framework import permissions

class IsAdminRol(permissions.BasePermission):
    """
    Solo permite acceso a Administradores.
    """
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        return request.user.rol and request.user.rol.nombre == 'Administrador'

class CanGenerateReports(permissions.BasePermission):
    """
    Permite acceso a Administradores y Contadores.
    Bloquea a Encargados.
    """
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        # Lista blanca de roles permitidos
        allowed_roles = ['Administrador', 'Contador']
        return request.user.rol and request.user.rol.nombre in allowed_roles