def seq_allocate(disk, start, length, file_no):
    flag = 0
    free_slots = 0

    for i in range(start, start + length):
        if disk[i] != 0:
            flag = 1

    if flag != 1:
        for i in range(start, start+length):
            disk[i] = file_no

    for i in disk:
        if i == 0:
            free_slots += 1

    print("Free Slots : ", free_slots)
    print()
    return flag


if __name__ == "__main__":
    disk_size = int(input("Enter disk size : "))
    seq_disk = [0]*disk_size
    go = "y"

    while go == "y":
        file_number = int(input("Enter file number : "))
        start_point = int(input("Enter the starting point : "))
        length_of_file = int(input("Enter the file size : "))

        if length_of_file > disk_size:
            length_of_file = int(input("please enter valid size : "))
        check = seq_allocate(seq_disk, start_point, length_of_file, file_number)

        if check == 1:
            print("File Not Allocated to the Disk: \n")
            print()
            go = input("Do you want to enter more files(y/n) : \n")

        else:
            for i in range(start_point, start_point + length_of_file):
                print("Slot No : {} :: Fill Flag(File No) : {}\n".format(i, seq_disk[i]))
            print("The File is Allocated to the Disk : \n")
            file_number += 1
            print()
            go = input("Do you want to enter more files(y/n) : \n")
