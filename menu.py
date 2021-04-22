import py_functions
import translation
import os
import sys

mode = "Python"

def switch_mode():
    global mode
    if mode == "Python":
        mode = "C"
        menu(mode)
    elif mode == "C":
        mode = "Python"
        menu(mode)
    
def ask_for_index():
    if len(images) == 0:
        print("No images have been loaded. No image can be selected.")
        menu(mode)
    else:
        while True:
            try:
               image_num1 = int(input("What is the index of the image you would like to select? "))
            except ValueError:
                print("That is not a valid integer.") #testing if input 1 is valid
                continue
            else:
                if int(image_num1) not in range(1,len(images) + 1):
                    print("The index should be between {} and {}.".format(1, len(images)))
                    continue
                else:
                    break
        while True:
            try:
                image_num2 = int(input("What is the index of the image you would like to select? "))
            except ValueError:
                print("That is not a valid integer.") #testing if input 2 is valid
                continue
            else:
                if int(image_num2) not in range(len(images) + 1):
                    print("The index should be between {} and {}.".format(1, len(images)))
                    continue
                else:
                    break
        image_index1 = "Image " + str(image_num1)
        image_index2 = "Image " + str(image_num2)
        if images[image_index1][1] != images[image_index2][1]:
            print("Images are not the same length; cannot compute PSNR between them.")
            menu(mode)
        else:
            return (image_index1, image_index2)


def ask_for_input():
    command = input()
    std_command = command.lower().replace(" ", "")
    print(std_command)
    if std_command == "help":
        help()
    elif std_command == "mode":
        switch_mode()
    elif std_command == "quit":
        quit()
    elif std_command == "load":
        load()
    elif std_command == "show":
        show()
    elif std_command == "psnr-r":
        image_index1, image_index2 = ask_for_index()
        if (images[image_index1][2] != "colour") or (images[image_index2][2] != "colour"):
            print("One of those images is not in colour; cannot compute red PSNR.")
            menu(mode)
        else:
            if mode == "Python":
                image1 = images[image_index1][0]
                image2 = images[image_index2][0]
                print(image1, image2)
                py_functions.py_r_psnr(image1, image2)
                menu(mode)
            else:
                image1 = images[image_index1]
                if image1[2] == "colour":
                    image1[2] = 1
                else:
                    image1[2] = 0
                image2 = images[image_index2]
                if image2[2] == "colour":
                    image2[2] = 1
                else:
                    image1[2] = 0
                print(image1, image2)
                #translation.call_c_r_psnr(image1, image2)
                menu(mode)
    elif std_command == "psnr-g":
        image_index1, image_index2 = ask_for_index()
        if (images[image_index1][2] != "colour") or (images[image_index2][2] != "colour"):
            print("One of those images is not in colour; cannot compute green PSNR.")
            menu(mode)
        else:
            image1 = images[image_index1][0]
            image2 = images[image_index2][0]
            print(image1, image2)
            if mode == "Python":
                py_functions.py_g_psnr(image1, image2)
                menu(mode)
            else:
                menu(mode)
    elif std_command == "psnr-b":
        image_index1, image_index2 = ask_for_index()
        if (images[image_index1][2] != "colour") or (images[image_index2][2] != "colour"):
            print("One of those images is not in colour; cannot compute blue PSNR.")
            menu(mode)
        else:
            image1 = images[image_index1][0]
            image2 = images[image_index2][0]
            print(image1, image2)
            if mode == "Python":
                py_functions.py_b_psnr(image1, image2)
                menu(mode)
            else:
                menu(mode)
    elif std_command == "psnr":
        image_index1, image_index2 = ask_for_index()
        if images[image_index1][2] != images[image_index2][2]:
            print("Images are not the same type; cannot compute PSNR between them.")
            menu(mode)
        else:
            image1 = images[image_index1][0]
            image2 = images[image_index2][0]
            print(image1, image2)
            if mode == "Python":
                py_functions.py_total_psnr(image1, image2)
                menu(mode)
            else:
                menu(mode)
    else:
        print("Invalid command.")
        ask_for_input()

def menu(mode):
    print("""
    ---PSNR Image Menu---

    Mode: {}
    Type 'help' to see all commands
    """.format(mode))
    ask_for_input()

images = {} #empty dictionary that contains loaded images
def load():
    colour = ""
    try:
        file_name = input("Enter the filename you want to load: ") #asks for file name input
        if os.stat(file_name).st_size == 0: #error case when file is empty
            print("Error: File is empty.")
            menu(mode)
        f = open(file_name, "r")
        lines = [line.split() for line in f] #breaking file into individual pixels and putting them in a list
        result = [] #creating an empty list that will contain the processed data
        for line in lines:
            result.append(line[0].split(",")) #getting rid of the commas
        for i in result: #iterating to each line
            if len(i) == 1:
                try:
                    i[0] = int(i[0])
                except ValueError:
                    print("Error: Non-integer value found in image file.") #error case when pixels contains non-integer
                    menu(mode)
                if (i[0] not in range(256)):
                        print("Error: Number outside the range of 0 to 255 found in image file.") #error case when integer value is outside the range
                        menu(mode)
                colour = "monochrome"
            elif len(i) == 3:
                for j in range(3): #iterating to each number
                    try:
                        i[j] = int(i[j]) #turning string from file into integer
                    except ValueError:
                        print("Error: Non-integer value found in image file.") #error case when pixels contains non-integer
                        menu(mode)
                    if (i[j] not in range(256)):
                        print("Error: Number outside the range of 0 to 255 found in image file.") #error case when integer value is outside the range
                        menu(mode)
                colour = "colour"
            else:
                print("Error: Image does not appear in RGB or monochrome format.") #error case when file is not correctly formatted
                menu(mode)
           
        image_index = "Image " + str(len(images) + 1)
        length = len(result)
        images[image_index] = [result, length, colour] #loads correctly formatted image into program memory
        print(images)
        f.close()
        menu(mode)
    except FileNotFoundError: 
        print("Error: File does not exist.") #error case when file does not exist
        menu(mode)

def show():
    for image_index in images:
        print("{}, Length {}, {}.".format(image_index, images[image_index][1], images[image_index][2]))
    menu(mode)

def help():

    print("""
    Commands:
    load: Load a single image into the program for use
    show: Display all images currently loaded
    psnr-r: Calculate the PSNR between the red values for two colour images
    psnr-g: Calculate the PSNR between the green values for two colour images
    psnr-b: Calculate the PSNR between the blue values for two colour images
    psnr: Calculate the PSNR between all values for two images
    mode: Toggle mode between C and Python
    help: Print out this command list
    quit: Exit the PSNR Image Menu
    """)

    ask_for_input()

print("Welcome to the PSNR image menu!")
menu(mode)