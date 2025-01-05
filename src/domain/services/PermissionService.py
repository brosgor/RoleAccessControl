class PermissionService:
    """
    Servicio encargado de manejar la validación de permisos de acceso a archivos.

    Atributos:
        permissions (dict): Diccionario que mapea roles a los archivos que pueden acceder.
    """

    def __init__(self):
        self.permissions = {
            "gerente": ["CNF01", "AUD01", "OPS01", "PUB01"],
            "supervisor": ["AUD01", "OPS01", "PUB01"],
            "empleado": ["OPS01", "PUB01"],
            "practicante": ["PUB01"],
        }

    def has_permission(self, role, file_name):
        """
        Verifica si un rol tiene permiso para acceder a un archivo.

        Args:
            role (str): El rol del empleado.
            file_name (str): El nombre del archivo solicitado.

        Returns:
            bool: True si el acceso está permitido, False de lo contrario.
        """
        return file_name in self.permissions.get(role, [])
