        # rooms                             #floors                 #buildings
rooms = [[[False for r in range(20)] for f in range(15)] for b in range(3)]
 
#The first index (0 through 2) selects one of the buildings; the second (0 through 14) selects the floor, the third (0 through 19) selects the room number. All rooms are initially free.


#Now you can book a room for two newlyweds: in the second building, on the tenth floor, room 14:
rooms[1][9][13] = True

#and release the second room on the fifth floor located in the first building:
rooms[0][4][1] = False

vacancy = 0
 
for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1