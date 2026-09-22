class Room:
    def __init__(self, name, left = "wall", right = "wall", forward = "wall", back = "wall"):
        self.name = name
        self.doors = {
            "left": left,
            "right": right,
            "forward": forward,
            "back": back
        }
    def add_door(self, direction, room):
        self.doors[direction] = room

class Game:
    def __init__(self, rooms):
        self.rooms = rooms
        self.current_room = rooms[0]
        self.play()

    def play(self):
        selection = input("Enter direction, q to exit")
        while selection != "q":
            if selection in {"left", "right", "forward", "back"}:
                if self.current_room.doors[selection] != "wall":
                    self.current_room = self.current_room.doors[selection]
                    print(f"Moved to {self.current_room.name}")
                else:
                    print("Cannot go that way")
            else:
                print("Unknown direction")
            selection = input("Enter direction, q to exit")

# rooms
kitchen = Room("Kitchen")
hall = Room("Hall")
living_room = Room("Living Room")
basement = Room("Basement")

# connect rooms into map
kitchen.add_door("right", hall)
living_room.add_door("left", hall)
basement.add_door("back", hall)
hall.add_door("left", kitchen)
hall.add_door("right", living_room)
hall.add_door("forward", basement)

# create and start
game1 = Game([kitchen, hall, living_room, basement])