import rclpy
from rclpy.node import Node
import socket

class TcpSenderNode(Node):
    def __init__(self):
        super().__init__('tcp_sender_node')
        
        # Configuration du client TCP
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_ip = '10.89.2.196'  # Remplacez par l'adresse IP du FiPy
        self.server_port = 1234  # Le même port que celui utilisé par le serveur TCP
        
        # Connexion au serveur
        self.connect_to_server()

        # Création d'un timer pour envoyer des messages périodiquement
        self.create_timer(5.0, self.send_message)  # Envoi tous les 5 secondes

    def connect_to_server(self):
        try:
            self.client_socket.connect((self.server_ip, self.server_port))
            self.get_logger().info(f'Connecté au serveur TCP {self.server_ip}:{self.server_port}')
        except Exception as e:
            self.get_logger().error(f'Échec de la connexion au serveur TCP: {e}')

    def send_message(self):
        try:
            message = 'Bonjour du nœud ROS 2'
            self.client_socket.sendall(message.encode())
            self.get_logger().info(f'Message envoyé: {message}')
        except Exception as e:
            self.get_logger().error(f'Échec de l\'envoi du message: {e}')

def main(args=None):
    rclpy.init(args=args)
    node = TcpSenderNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

