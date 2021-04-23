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
    int red = *(image1->pd.colour_pixels.red);
    printf("%d\n", red);
    int red2 = *(image2->pd.colour_pixels.red);
    printf("%d\n", red2);
    return 0;
}

float c_g_psnr(struct Image* image1, struct Image* image2) {
    //TODO
    return 0;
}

float c_b_psnr(struct Image* image1, struct Image* image2) {
    //TODO
    return 0;
}

float c_total_psnr(struct Image* image1, struct Image* image2) {
    //TODO
    return 0;
}