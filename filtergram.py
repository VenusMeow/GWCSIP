#import my filters file
import filters

#main function
def main():
    filename = input("Enter the name of the file you want to edit: ")

    #load image using filename
    img = filters.load_img(filename)

    #change the filter of the Image
    #newim = filters.grayscale(img)
    newim2 = filters.obamicon(img)
    
    #saves final image
    filters.save_img(newim2, "obamicat.jpeg")



#DONT TOUCH
if __name__ == "__main__":
    main()
