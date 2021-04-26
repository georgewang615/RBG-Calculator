import math

def py_r_psnr(image1, image2):
    MSE = 0

    for i in range(len(image1)): #iterating through each line of pixels
        MSE += (image1[i][0]-image2[i][0]) ** 2 #adding each squared difference to MSE
    MSE /= len(image1) #dividing MSE by image length

    try:
        PSNR = 10 * math.log10((255**2)/MSE)

    except ZeroDivisionError: #prevents zero division where images are identical
        PSNR = float(0)
    
    return PSNR
    


def py_g_psnr(image1, image2):
    MSE = 0

    for i in range(len(image1)): 
        MSE += (image1[i][1]-image2[i][1]) ** 2 
    MSE /= len(image1) 

    try:
        PSNR = 10 * math.log10((255**2)/MSE)

    except ZeroDivisionError: 
        PSNR = float(0)

    return PSNR
    


def py_b_psnr(image1, image2):
    MSE = 0

    for i in range(len(image1)): 
        MSE += (image1[i][2]-image2[i][2]) ** 2 
    MSE /= len(image1) 

    try:
        PSNR = 10 * math.log10((255**2)/MSE)

    except ZeroDivisionError: 
        PSNR = 0

    return PSNR


def py_total_psnr(image1, image2):
    MSE = 0

    if len(image1[0]) == 1: #case where images are monochrome

        for i in range(len(image1)):
            MSE += (image1[i][0]-image2[i][0]) ** 2
        MSE /= len(image1)

        try:
            PSNR = 10 * math.log10((255**2)/MSE)

        except ZeroDivisionError:
            PSNR = float(0)
    else: #case where images are coloured
    
        for i in range(len(image1)):

            for j in range(3):
                MSE += (image1[i][j] - image2[i][j]) ** 2

        MSE /= (3* len(image1))

        try:
            PSNR = 10 * math.log10((255**2)/MSE)

        except ZeroDivisionError:
            PSNR = float(0)

    return PSNR
