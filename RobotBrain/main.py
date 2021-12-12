from ServerClass import server
from RobotClass import Robot

rob = Robot()
server = server()


while True:
    try:
        client_input = server.listen()

        print("Revice : " + client_inpuadt)

        if client_input == "Man":
            while True:
                rob_command = server.listen()
                print("Robot command : "+rob_command)

                if rob_command == "end":
                    break
                elif rob_command == "color" or rob_command == "distance":
                    print(rob.manual_commands.get(rob_command)())
                else:
                    try:
                        rob.manual_commands.get(rob_command)()
                    except:
                        pass


    except ConnectionResetError:
        server.accept_client()