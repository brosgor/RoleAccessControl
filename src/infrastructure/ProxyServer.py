from domain.interfaces.ServerInterface import ServerInterface


class ProxyServer(ServerInterface):
    """
    Proxy que maneja la solicitud de archivos y verifica permisos de acceso.
    Atributos:
        - employee: Un objeto que representa al empleado que realiza la solicitud.
        - real_server: Una instancia del servidor real que maneja las operaciones.
    """

    def __init__(self, employee, real_server):
        self.employee = employee
        self.real_server = real_server

    def has_permission(self, role, file_name):
        """
        Verifica si un rol tiene permiso para acceder a un archivo.

        si el acceso está permitido, retorna la lista de archivos permitidos para ese rol.
        """
        permissions = {
            "gerente": ["CNF01", "AUD01", "OPS01", "PUB01"],
            "supervisor": ["AUD01", "OPS01", "PUB01"],
            "empleado": ["OPS01", "PUB01"],
            "practicante": ["PUB01"],
        }

        return file_name in permissions.get(role, [])

    def get_file(self, file_name):
        """
        Verifica permisos, maneja errores y solicita el archivo al servidor real si están autorizados.
        Args:
            file_name (str): El nombre del archivo solicitado.
        Returns:
            str: Contenido del archivo si el acceso es permitido o un mensaje de error.
        """
        try:
            # Usar PermissionService para validar permisos
            if not self.has_permission(self.employee.role, file_name):
                return (
                    f"Error: Acceso denegado al archivo '{file_name}' para el usuario "
                    f"{self.employee.name} con rol {self.employee.role}."
                )

            # Solicitar al servidor real
            return self.real_server.get_file(file_name)
        except FileNotFoundError:
            return f"Error: El archivo '{file_name}' no se encontró en el servidor."
