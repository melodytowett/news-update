from logging import Manager
from xmlrpc.client import Server
from app import create_app
app = create_app('development')
manager = Manager(app)
#manager.add_commad('server', Server)

if __name__ == '__main__':
    manager.run()
