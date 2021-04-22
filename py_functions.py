import math

def py_r_psnr(image1, image2):
    MSE = 0
    for i in range(len(image1)):
        squared_difference = (image1[i][0]-image2[i][0]) ** 2
        MSE += squared_difference
    MSE /= len(image1)
    try:
        PSNR = 10 * math.log10((255**2)/MSE)
    except ZeroDivisionError:
        PSNR = 0
    print("Red PSNR: {}".format(PSNR))

def py_g_psnr(image1, image2):
    MSE = 0
    for i in range(len(image1)):
        squared_difference = (image1[i][0]-image2[i][0]) ** 2
        MSE += squared_difference
    MSE /= len(image1)
    try:
        PSNR = 10 * math.log10((255**2)/MSE)
    except ZeroDivisionError:
        PSNR = 0
    print("Green PSNR: {}".format(PSNR))

def py_b_psnr(image1, image2):
    MSE = 0
    for i in range(len(image1)):
        squared_difference = (image1[i][0]-image2[i][0]) ** 2
        MSE += squared_difference
    MSE /= len(image1)
    try:
        PSNR = 10 * math.log10((255**2)/MSE)
    except ZeroDivisionError:
        PSNR = 0
    print("Blue PSNR: {}".format(PSNR))

def py_total_psnr(image1, image2):
    if len(image1[0]) == 1:
        MSE = 0
        for i in range(len(image1)):
            squared_difference = (image1[i]-image2[i]) ** 2
            MSE += squared_difference
        MSE /= len(image1)
        try:
            PSNR = 10 * math.log10((255**2)/MSE)
        except ZeroDivisionError:
            PSNR = 0
    else:
        MSE = 0
        for i in range(len(image1)):
            for j in range(3):
                squared_difference = (image1[i][j] - image2[i][j]) ** 2
                MSE += squared_difference
        MSE /= (3* len(image1))
        try:
            PSNR = 10 * math.log10((255**2)/MSE)
        except ZeroDivisionError:
            PSNR = 0
    print("PSNR of images: {}".format(PSNR))
