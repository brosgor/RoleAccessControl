from domain.models.employ import Employee
from infrastructure.ProxyServer import ProxyServer
from infrastructure.RealServer import RealServer


def main():
    # Crear empleado y servidor
    intern = Employee(name="Bob", role="practicante")
    employee = Employee(name="Alice", role="empleado")
    supervisor = Employee(name="John", role="supervisor")
    manager = Employee(name="Diana", role="gerente")
    real_server = RealServer()
    proxy_server = ProxyServer(supervisor, real_server)

    # Solicitar archivo
    confidential_file = "CNF01"  # Archivo confidencial
    supervision_report = "AUD01"  # Informe de auditoría
    operations_manual = "OPS01"  # Manual operativo
    public_report = "PUB01"  # Informe público
    
    requested_file = confidential_file
    response = proxy_server.get_file(requested_file)

    print("=" * 75)
    print(response)
    print("=" * 75)


if __name__ == "__main__":
    main()
