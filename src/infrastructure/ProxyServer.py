from domain.interfaces.ServerInterface import ServerInterface


class ProxyServer(ServerInterface):
    def __init__(self, employee, real_server):
        self.employee = employee
        self.real_server = real_server

    def get_file(self, file_name):
        """
        Verifica permisos, maneja errores y solicita el archivo al servidor real si están autorizados.
        Args:
            file_name (str): El nombre del archivo solicitado.
        Returns:
            str: Contenido del archivo si el acceso es permitido o un mensaje de error.
        """
        try:
            # Validar permisos
            if not self.has_permission(self.employee.role, file_name):
                return f"Error: Acceso denegado al archivo '{file_name}' para el usuario {self.employee.name} con rol {self.employee.role}."
            
            # Solicitar al servidor real
            return self.real_server.get_file(file_name)
        except FileNotFoundError:
            return f"Error: El archivo '{file_name}' no se encontró en el servidor."
    
    def has_permission(self, role, file_name):
        """
        Simula la validación de permisos.
        """
        permissions = {
            "manager": ["confidential_file", "public_report"],
            "employee": ["public_report"],
            "intern": []
        }
        return file_name in permissions.get(role, [])
