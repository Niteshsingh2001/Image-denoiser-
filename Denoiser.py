import cv2 as cv
import random as ran
from rich import print as rprint
from rich.progress import track

def resize_frame(frame,scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimesnion = (width,height)
    return cv.resize(frame,dimesnion,interpolation=cv.INTER_AREA)


def both(image,scale_val,d,sigma_color,sigma_space):
    resize_img = resize_frame(image,scale_val)
    return denoiser(resize_img,d,sigma_color,sigma_space)

def denoiser(image,d,sigma_color,sigma_space):
    b,g,r = cv.split(image)

    blue = cv.bilateralFilter(b,d,sigma_color,sigma_space)
    Green = cv.bilateralFilter(g,d,sigma_color,sigma_space)
    Red = cv.bilateralFilter(r,d,sigma_color,sigma_space)
    return cv.merge([blue,Green,Red])



if __name__ == "__main__":

    rprint("---------------- Image Works -------------------------")

    rprint("1. Upscale Image\n2. Denoise Image\n3. Upscale and Denoise")
    
    user_choice = int(input("Enter Your Choice : "))
    
    img_loc = input("Enter Image Location : ")
    
    reading_image = cv.imread(img_loc)

    if user_choice == 1:
        scale_val = float(input("Enter Scale Value : "))
        for _ in track(range(100), description='[green]Please Wait'):
            img_res = resize_frame(reading_image,scale_val)
        cv.imwrite(f"cv_upscale{ran.randrange(0,999999999)}.png",img_res)
        rprint("Done")
    elif user_choice == 2:
        val = int(input("Enter Strength Value :"))
        color = int(input("Enter Color Value :"))
        space = int(input("Enter Space Value :"))

        for _ in track(range(100), description='[green]Please Wait'):
            img_de = denoiser(reading_image,val,color,space)
        
        cv.imwrite(f"cv_denoise{ran.randrange(0,999999999)}.png",img_de)
        cv.imshow("Preview",resize_frame(img_de,0.5))
        rprint("Done")
        cv.waitKey(0)
        

    elif user_choice == 3:
        scale_val = float(input("Enter Scale Value : "))
        val = int(input("Enter Strength Value :"))
        color = int(input("Enter Color Value :"))
        space = int(input("Enter Space Value :"))
        for _ in track(range(100), description='[green]Please Wait'):
            img = both(reading_image,scale_val,val,color,space)
        cv.imwrite(f"cv_upscale_and_denoise{ran.randrange(0,999999999)}.png",img)
        rprint("Done")
    
    else:
        rprint("[Error!] Enter Valid Choice")
    
