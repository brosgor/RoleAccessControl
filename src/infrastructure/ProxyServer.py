from domain.interfaces.ServerInterface import ServerInterface
from domain.services.PermissionService import PermissionService


class ProxyServer(ServerInterface):
    """
    Clase ProxyServer que actúa como un intermediario entre el cliente y el servidor real.

    Esta clase implementa la interfaz ServerInterface y proporciona métodos para
    gestionar las solicitudes del cliente, delegando las operaciones al servidor real
    mientras puede agregar funcionalidades adicionales como control de acceso,
    caché de respuestas, o registro de actividades.

    Atributos:
        - employee: Un objeto que representa al empleado que realiza la solicitud.
        - real_server: Una instancia del servidor real que maneja las operaciones.
        - permision_service: Una instancia del servicio encargado de validar permisos

    Métodos:
        - get_file(file_name): Solicita un archivo al servidor real y puede
          realizar operaciones adicionales antes o después de la solicitud.
    """

    def __init__(self, employee, real_server):
        self.employee = employee
        self.real_server = real_server
        self.permission_service = (
            PermissionService()
        )  # Instancia del servicio de permisos

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
            if not self.permission_service.has_permission(
                self.employee.role, file_name
            ):
                return (
                    f"Error: Acceso denegado al archivo '{file_name}' para el usuario "
                    f"{self.employee.name} con rol {self.employee.role}."
                )

            # Solicitar al servidor real
            return self.real_server.get_file(file_name)
        except FileNotFoundError:
            return f"Error: El archivo '{file_name}' no se encontró en el servidor."
