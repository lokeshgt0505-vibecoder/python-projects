import time
import menu
command =""
started = False
print("welcome to paradise\n"
      "where adreline grows high speed\n ")
print("start , stop , quit")
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
                   print(" car has already started ")
        else:
             print(" igniting engine....")
             time.sleep(0.2)
        print("vroom vroom vrommm,,!!!!1")
        time.sleep(0.2)
        print("vroom vroom vrommmmm,,!!!!1")
        time.sleep(0.3)
        print("vroom vroom vrommmmmmm,,!!!!1")
        time.sleep(0.4)
        print("vroom vroom vrommmmmmmm,,!!!!1")
        time.sleep(0.7)

        print("Car started!" )
        time.sleep(0.2)
        print("Let's go!!!!")
        started = True

    elif command == "stop":
        if not started:
            print("car has been stopped")
        else:
            print("engine shutting down...!!!!")
            time.sleep(0.2)
            print("engine is off ")
            started = False
    elif command == "help":
        print("\n"
              "start : start the game\n"
              "stop : stop the game\n"
              "quit: game quiting \n")
    elif command == "quit":
          break
    else:
          print("invalid command")
