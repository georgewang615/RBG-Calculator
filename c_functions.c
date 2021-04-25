#include "c_functions.h"
#include <stdio.h>

void make_coloured_image(int* red, int* green, int* blue, int len, struct ColouredPixels* cp, union PixelData* pd, struct Image* im) {
    cp->red = red;
    cp->green = green;
    cp->blue = blue;
    pd->colour_pixels = *cp;
    im->pd = *pd;
    im->length = len;
    im->is_coloured = 1;
}

void make_monochrome_image(int* grey, int len, union PixelData* pd, struct Image* im) {
    pd->grey_pixels = grey;
    im->pd = *pd;
    im->length = len;
    im->is_coloured = 0;
}

float c_r_psnr_wrapper(int* red1, int* green1, int* blue1, int* red2, int* green2, int* blue2, int len) {
    struct ColouredPixels cp1;
    struct ColouredPixels cp2;

    union PixelData pd1;
    union PixelData pd2;

    struct Image image1;
    struct Image image2;

    make_coloured_image(red1, green1, blue1, len, &cp1, &pd1, &image1);
    make_coloured_image(red2, green2, blue2, len, &cp2, &pd2, &image2);
    
    return c_r_psnr(&image1, &image2);
}

float c_g_psnr_wrapper(int* red1, int* green1, int* blue1, int* red2, int* green2, int* blue2, int len) {
    struct ColouredPixels cp1;
    struct ColouredPixels cp2;

    union PixelData pd1;
    union PixelData pd2;

    struct Image image1;
    struct Image image2;

    make_coloured_image(red1, green1, blue1, len, &cp1, &pd1, &image1);
    make_coloured_image(red2, green2, blue2, len, &cp2, &pd2, &image2);
    
    return c_g_psnr(&image1, &image2);
}

float c_b_psnr_wrapper(int* red1, int* green1, int* blue1, int* red2, int* green2, int* blue2, int len) {
    struct ColouredPixels cp1;
    struct ColouredPixels cp2;

    union PixelData pd1;
    union PixelData pd2;

    struct Image image1;
    struct Image image2;

    make_coloured_image(red1, green1, blue1, len, &cp1, &pd1, &image1);
    make_coloured_image(red2, green2, blue2, len, &cp2, &pd2, &image2);
    
    return c_b_psnr(&image1, &image2);
}

float c_total_psnr_wrapper(int* red1, int* green1, int* blue1, int* red2, int* green2, int* blue2, int len, int is_coloured) {
    struct ColouredPixels cp1;
    struct ColouredPixels cp2;

    union PixelData pd1;
    union PixelData pd2;

    struct Image image1;
    struct Image image2;

    if (is_coloured) {
        make_coloured_image(red1, green1, blue1, len, &cp1, &pd1, &image1);
        make_coloured_image(red2, green2, blue2, len, &cp2, &pd2, &image2);
    } else {
        make_monochrome_image(red1, len, &pd1, &image1);
        make_monochrome_image(red2, len, &pd2, &image2);
    }

    float f = c_total_psnr(&image1, &image2);
    return f;
}

float c_r_psnr(struct Image* image1, struct Image* image2) {
    float MSE = 0;

    for (int i = 0; i < image1->length; i++){ //iterating through each line of pixels
        int red1 = *(image1->pd.colour_pixels.red + i); //accessing the address of the pixel and dereferencing it, and adding i moves on to the next line
        int red2 = *(image2->pd.colour_pixels.red + i);
        MSE += pow((red1-red2), 2); //adding each squared error to MSE
    }
    MSE /= image1->length; //diving MSE by the image length

    if (MSE == 0){
        return 0; //to prevent zero division with identical images
    }

    else{
        float PSNR = 10 * log10((255 * 255) / MSE); //calculates PSNR as a float
        return PSNR;
    }
}

float c_g_psnr(struct Image* image1, struct Image* image2) {
    float MSE = 0;
    for (int i = 0; i < image1->length; i++){
        int green1 = *(image1->pd.colour_pixels.green + i);
        int green2 = *(image2->pd.colour_pixels.green + i);
        MSE += pow((green1-green2), 2);
    }
    MSE /= image1->length;
    if (MSE == 0){
        return 0;
    }
    else{
        float PSNR = 10 * log10((255 * 255) / MSE);
        return PSNR;
    }
}

float c_b_psnr(struct Image* image1, struct Image* image2) {
    float MSE = 0;
    for (int i = 0; i < image1->length; i++){
        int blue1 = *(image1->pd.colour_pixels.blue + i);
        int blue2 = *(image2->pd.colour_pixels.blue + i);
        MSE += pow((blue1-blue2), 2);
    }
    MSE /= image1->length;
    if (MSE == 0){
        return 0;
    }
    else{
        float PSNR = 10 * log10((255 * 255) / MSE);
        return PSNR;
    }
}

float c_total_psnr(struct Image* image1, struct Image* image2) {
    float MSE = 0;
    if (image1->is_coloured == 0){
        for (int i = 0; i < image1->length; i++){
            int grey1 = *(image1->pd.grey_pixels + i);
            int grey2 = *(image2->pd.grey_pixels + i);
            int difference = pow((grey1-grey2), 2);
            MSE += difference;
        }
        MSE /= image1->length;
        if (MSE == 0){
            return 0;
        }
        else{
            float PSNR = 10 * log10((255 * 255) / MSE);
            return PSNR;
        }
    }
    else {
        for (int i = 0; i < image1->length; i++){
            int red1 = *(image1->pd.colour_pixels.red + i);
            int red2 = *(image2->pd.colour_pixels.red + i);

            int green1 = *(image1->pd.colour_pixels.green + i);
            int green2 = *(image2->pd.colour_pixels.green + i);

            int blue1 = *(image1->pd.colour_pixels.blue + i);
            int blue2 = *(image2->pd.colour_pixels.blue + i);

            MSE += pow((red1-red2), 2);
            MSE += pow((green1-green2), 2);
            MSE += pow((blue1-blue2), 2);
        }
        MSE /= 3 * image1->length;
        if (MSE == 0){
            return 0;
        }
        else{
            float PSNR = 10 * log10((255 * 255) / MSE);
            return PSNR;
        }
    }
}