from random import randint


def indexed_allocate(disk, start, length, file_no, index_slot):
    if index_slot == start:
        return 1
    flag = 0
    free_slots = 0
    for i in range(len(disk)):
        if disk[i][1] == 0:
            free_slots += 1
    if length <= free_slots and disk[start][1] == 0 and disk[index_slot][1] == 0:
        count = 0
        random_slot = 0
        disk[index_slot][0] = 1  # As it's an index slot
        disk[index_slot][1] = file_no
        index_slot_idx = 2
        block_no = 1
        while count < length:
            if count > 0:
                random_slot = randint(0, (len(disk)))
            else:
                random_slot = start
            if disk[random_slot][1] == 0:
                disk[random_slot][1] = file_no
                disk[random_slot][2] = block_no
                disk[index_slot][index_slot_idx] = random_slot
                index_slot_idx += 1
                block_no += 1
                count += 1
    else:
        flag = 1
    free_slots = 0
    for i in range(len(disk)):
        if disk[i][1] == 0:
            free_slots += 1
    print("Free Slots : ", free_slots)
    print()
    return flag



if __name__ == "__main__":
    disk_size = int(input("Enter disk size : "))
    ind_disk = [[0, 0]] * disk_size
    go = "y"

    while go == "y":
        file_number = int(input("Enter file number : "))
        start_point = int(input("Enter the starting point : "))
        length_of_file = 1  # int(input("Enter the file size : "))
        if length_of_file > disk_size:
            length_of_file = int(input("please enter valid size : "))
        print("Enter the block/slot for the index : ")
        index = int(input())
        check = indexed_allocate(ind_disk, start_point, length_of_file, file_number, index)

        if check == 1:
            print("File Not Allocated to the Disk \n")
            print("Do you want to enter more files(y/n) : \n")
            go = input()
        else:
            flag = 0
            temp = start_point
            print("The Index is : \n")
            for i in range(length_of_file):
                print("Block_No : {} :: Indexed at : {} \n".format(i + 1, ind_disk[index][i + 2]))
                if flag == 0:
                    print("Slot No : {} :: Fill Flag(File No) : {} :: Block_No : {] \n".format(temp, ind_disk[temp][1], ind_disk[temp][2]))
                    flag = 1
                else:
                    temp = ind_disk[index][2 + i]
                    print("Slot No : {} :: Fill Flag(File No) : {} :: Block_No : {} \n".format(temp, ind_disk[temp][1], ind_disk[temp][2]))
                    temp = ind_disk[temp][1]
            print("The File is Allocated to the Disk : \n")
            file_number += 1
            print("Do you want to enter more files(y/n) : \n")
            go = input()
