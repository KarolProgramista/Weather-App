import requests
from tkinter import font
import tkinter as tk
from PIL import Image, ImageTk

HEIGHT = 700
WIDTH = 800


def test_function(entry):
    print("This is the entry ", entry)

# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
# 31935f74dc38428a0dbb629f55a8e63a


def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s \nConditions: %s \nTemperature (°C): %s' % (name, desc, temp)
    except:
        final_str = "There was a problem"

    return final_str


def get_weather(city):
    weather_key = '31935f74dc38428a0dbb629f55a8e63a'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    print(response.json())
    weather = response.json()

    icon_name = weather['weather'][0]['icon']
    print(icon_name)

    label['text'] = format_response(weather)
    open_image(icon_name)

def open_image(icon):
    size = int(lower_frame.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='./img/landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

label = tk.Label(lower_frame, font=('Courier', 28))
label.place(relwidth=1, relheight=1)


weather_icon = tk.Canvas(label, bd=0, highlightthickness=0)
weather_icon.place(relx=0.8, rely=0, relwidth=0.198, relheight=0.3)


root.mainloop()
