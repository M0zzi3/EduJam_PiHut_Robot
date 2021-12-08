from ServerClass import server
from RobotClass import Robot

rob = Robot()
server = server()


while True:
    try:
        client_input = server.listen()

        print("Revice : " + client_input)

        if client_input == "END":
            server.end_connection()

        elif client_input == "Man":
            while True:
                rob_command = server.listen()

                if rob_command != "end":
                    rob.execute(rob_command)
                else:
                    break
    except ConnectionResetError:
        server.accept_client()