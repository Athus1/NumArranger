
Num_List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(Num_List)
direction = input("forward or backward?: ")
if direction == "forward":
    steps = input("how many steps forward?: ")
    while int(steps) > 0:
        x = len(Num_List)
        a = Num_List.pop(x - 1)
        Num_List.insert(0, int(a))
        print(Num_List)
        steps = int(steps) - 1

elif direction == "backward":
    steps = input("how many steps backward?: ")
    while int(steps) > 0:
        x = len(Num_List)
        a = Num_List.pop(0)
        Num_List.insert(x-1, int(a))
        text = str(Num_List)
        print(Num_List)

        steps = int(steps) - 1
