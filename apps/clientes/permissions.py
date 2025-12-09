from rest_framework import permissions

class CanEditClientData(permissions.BasePermission):
    """
    - Lectura (GET): Permitido a todos los usuarios autenticados.
    - Escritura (POST, PUT, PATCH, DELETE): Solo Administrador y Contador.
    """
    def has_permission(self, request, view):
        # 1. Si no está logueado, adiós.
        if not request.user or not request.user.is_authenticated:
            return False

        # 2. Si es una petición segura (GET, HEAD, OPTIONS), pase adelante.
        if request.method in permissions.SAFE_METHODS:
            return True

        # 3. Si quiere editar/borrar, verificamos el rol.
        allowed_roles = ['Administrador', 'Contador']
        return request.user.rol and request.user.rol.nombre in allowed_roles