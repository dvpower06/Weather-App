from tkinter import *
from PIL import Image, ImageTk
from Script import Weather

class Menu_Interface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Weather App")
        self.logo = PhotoImage(file='Images/cloudy.png')
        self.city_label = Label(self.window,
                                text="City",
                                font=("Segoe UI", 20, "bold"),
                                fg="#000000",
                                bg=None,
                                padx=30,
                                pady=20 
                                )
        self.city = Entry(self.window, width=30, font=("Segoe UI", 16))
        self.submit_button = Button(self.window,
                                    text="Get Weather",
                                    bg="#18ad45",
                                    fg="white", 
                                    activebackground="#0b7a2c",
                                    activeforeground="white",
                                    command=self.submit
                                    )
        self.noCityFound_label = None
        self.cityWeather_label= None
        self.background_image = Image.open("Images/background.jpg")
        self.bg = ImageTk.PhotoImage(self.background_image)
        self.background = Label(self.window, image=self.bg)
         
    def center_window(self, window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width//2) - (width//2)
        y = (screen_height//2) - (height//2)
        window.geometry(f"{width}x{height}+{x}+{y}")

    def submit(self):
            
            city_name = self.city.get()
            self.wp = Weather(city_name)

            #Clear existing text
            if self.cityWeather_label:
                 self.cityWeather_label.destroy()
                 self.cityWeather_label = None

            if self.noCityFound_label:
                 self.noCityFound_label.destroy()
                 self.noCityFound_label = None
            

            if not self.wp.cityExists():
                self.noCityFound_label = Label(self.window,
                                               text = "No city found!",
                                                fg="#000000",
                                                bg="#E7D9D9",
                                                font=("Segoe UI", 12, "bold")
                                                  )
                self.noCityFound_label.pack()
            else:
                self.wp.getWeather()

                text = f"Weather in {city_name}:\n{self.wp.temperature}\n{self.wp.description}"

                self.cityWeather_label = Label(self.window,
                                                text=text,
                                                fg="#000000",
                                                bg="#E7D9D9",
                                                font=("Segoe UI", 12, "bold")
                                                )
                self.cityWeather_label.pack(pady=20)
      
    def run(self):
        self.background.place(x=0, y=0, relwidth=1, relheight=1)
        self.background.lower()
        self.city_label.pack(pady=20)
        self.city.pack(pady=20)
        self.submit_button.pack(pady=20)
         
        self.center_window(self.window, 600, 400)
        self.window.iconphoto(True, self.logo)
        self.window.resizable(False, False)
        self.window.mainloop()




if __name__ == "__main__":
    mi = Menu_Interface()
    mi.run()

