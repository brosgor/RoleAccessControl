from domain.models.employ import Employee
from infrastructure.ProxyServer import ProxyServer
from infrastructure.RealServer import RealServer


def main():
    # Crear empleado y servidor
    intern = Employee(name="Bob", role="manager")
    real_server = RealServer()
    proxy_server = ProxyServer(intern, real_server)

    # Solicitar archivo
    file_name = "confidential_file"
    response = proxy_server.get_file(file_name)
    print(response)


if __name__ == "__main__":
    main()
