import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image
import os

# Global variables
directory = r'DIRECTORY WITH IMAGES'
images = []
img_counter = 0

# Formating variables
btn_color = 'white'
color_fondo = 'lightblue'


class w(tk.Tk):
    def __init__(self, dir_imgs, img_ext):
        tk.Tk.__init__(self)
        self.title('Image viewer')
        self.config(bg=color_fondo)

        # Get names of files in directory.
        self.get_files_names(dir_imgs, img_ext)

        btn_font = tkFont.Font(family = "Lucida console", size=10, weight=tkFont.BOLD)

        # Widget creation:
        self.main_frame = tk.Frame(self, bg= color_fondo)
        self.img = ImageTk.PhotoImage(Image.open(dir_imgs+'\\'+images[0]), master=self)
        self.img_lbl = tk.Label(self.main_frame, image=self.img)
        prev_nav_btn = tk.Button(self.main_frame, bg=btn_color, font=btn_font, text='<<', height=2, width=20, command=lambda : self.navigation(dir_imgs, 'prev'))
        next_nav_btn = tk.Button(self.main_frame, bg=btn_color, font=btn_font, text='>>', height=2, width=20, command=lambda : self.navigation(dir_imgs,'next'))
        
        # Widget placing:
        self.main_frame.pack()
        self.img_lbl.grid(row=0, column=0, columnspan=2)
        prev_nav_btn.grid(row=1, column=0, pady=10)
        next_nav_btn.grid(row=1, column=1, pady=10)
        self.mainloop()


    def get_files_names(self, directory, extension):
        """
        This function returns a list with the names of the files with a determined extension.
        Parameters:
            -directory: Directory to be opened.
            -extension: Extension of the files to be displayed.
        """
        global images
        try:
            files = os.listdir(directory)
            images = [x for x in files if extension in x]
            return images
        except FileNotFoundError:
            raise Exception("Please, use an appropiate directory.")


    def navigation(self, directory, direction):
        """
        This function modifies the value of the global variable img_counter by 1,
        depending on the direction of the direction parameter. Additionaly, shows the
        corresponding image in the corresponding widget.
        Parameters:
            -directory: Directory to be opened.
            -direction: Takes the strings "prev" or "next" to increment or decrease
                        the img_counter by 1, respectively.
        """
        global img_counter, images
        if direction == 'prev' and img_counter !=0:
            img_counter -= 1
        elif direction == 'next' and img_counter != len(images)-1:
            img_counter += 1
        self.img_lbl.grid_forget()
        self.img = ImageTk.PhotoImage(Image.open(directory+'\\'+images[img_counter]), master=self)
        self.img_lbl.config(image=self.img)
        self.img_lbl.grid(row=0, column=0, columnspan=2)


if __name__ == "__main__":
    w1 = w(directory, '.jpg')
