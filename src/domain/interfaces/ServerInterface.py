
class ServerInterface:
    """
    Interfaz para los servidores. Define el contrato básico que deben implementar.
    
    Métodos:
        get_file(file_name): Devuelve el contenido de un archivo.
    """
    def get_file(self, file_name):
        raise NotImplementedError("Este método debe ser implementado por una subclase.")

