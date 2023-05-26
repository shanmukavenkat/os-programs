from random import randrange


def linked_list_allocate(disk, start, length, file_no):
    flag = 0
    free_slots = 0
    for i in range(len(disk)):
        if disk[i][0] == 0:
            free_slots += 1
    if length <= free_slots and disk[start][0] == 0:
        count = 0
        temp = 0
        # random_slot = 0
        while count < length:
            if count > 0:
                random_slot = int(randrange(0, (len(disk))))
            else:
                random_slot = start
                temp = random_slot
            if disk[random_slot][0] == 0:
                if count > 0:
                    disk[temp][1] = random_slot
                    temp = random_slot
                count += 1
                disk[random_slot][0] = file_no
    else:
        flag = 1
    free_slots = 0
    for i in range(len(disk)):
        if disk[i][0] == 0:
            free_slots += 1
    print("Free Slots : {}\n".format(free_slots))
    return flag


if __name__ == "__main__":
    disk_size = int(input("Enter disk size : "))
    ll_disk = [[0, -1]] * disk_size
    # print(len(ll_disk))
    go = "y"

    while go == "y":
        file_number = int(input("Enter file number : "))
        start_point = int(input("Enter the starting point : "))
        length_of_file = int(input("Enter the file size : "))
        if length_of_file > disk_size:
            length_of_file = int(input("please enter valid size : "))
        check = linked_list_allocate(ll_disk, start_point, length_of_file, file_number)
        if check == 1:
            print("File Not Allocated to the Disk: \n")
            go = input("Do you want to enter more files(y/n) : \n")
        else:
            flag = 0
            temp = start_point
            for i in range(start_point, start_point + length_of_file):
                if flag == 0:
                    print("Slot No : {} :: Fill Flag(File No) : {} :: Next Slot(Next File) : {}\n".format(temp, ll_disk[temp][0], ll_disk[temp][1]))
                    temp = ll_disk[temp][1]
                    flag = 1
                else:
                    print("Slot No : {} :: Fill Flag(File No) : {} :: Next Slot(Next File) : {}\n".format( temp, ll_disk[temp][0], ll_disk[temp][1]))
                    temp = ll_disk[temp][1]
            print("The File is Allocated to the Disk  \n")
            file_number += 1
            go = input("Do you want to enter more files : \n")
