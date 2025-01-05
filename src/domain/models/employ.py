# --- Entidades ---
class Employee:
    """
    Representa un empleado con un nombre y un rol.
    
    Atributos:
        name (str): Nombre del empleado.
        role (str): Rol del empleado (ejemplo: "manager", "employee").
    """
    def __init__(self, name, role):
        self.name = name
        self.role = role