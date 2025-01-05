from domain.interfaces.ServerInterface import ServerInterface


class RealServer(ServerInterface):
    """
    Servidor real que entrega el contenido de un archivo si se solicita con el nombre amigable.

    Métodos:
        get_file(file_name): Devuelve el contenido del archivo.
    """

    def __init__(self):
        # Mapeo de nombres amigables a rutas internas
        self.file_mapping = {
            "CNF01": "data/CNF01.txt",
            "AUD01": "data/AUD01.txt",
            "OPS01": "data/OPS01.txt",
            "PUB01": "data/PUB01.txt",
        }

    def get_file(self, file_name):
        """
        Devuelve el contenido del archivo solicitado.

        Args:
            file_name (str): El nombre amigable del archivo.

        Returns:
            str: Contenido del archivo.

        Raises:
            FileNotFoundError: Si el archivo no está definido o no existe físicamente.
        """
        # Validar que el archivo exista en el mapeo
        if file_name not in self.file_mapping:
            raise FileNotFoundError(
                f"El archivo '{file_name}' no está definido en el sistema."
            )

        # Obtener la ruta interna y leer el contenido del archivo
        file_path = self.file_mapping[file_name]
        try:
            with open(file_path, "r") as file:
                return file.read()
        except FileNotFoundError:
            raise FileNotFoundError(
                f"El archivo físico '{file_path}' no existe en el servidor."
            )
