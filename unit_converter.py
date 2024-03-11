# A Standard Unit Converter Program
from tkinter import*


myWindow = Tk()
myWindow.title("Unit Conversion")
myWindow.geometry("500x430+250+250")
myWindow.resizable(0,0)
myWindow.configure(bg="#999900")

def myArea():
    area_window = Toplevel()
    area_window.title("Area Conversion")
    area_window.geometry("400x400")
    area_window.resizable(0,0)
    area_window.configure(bg="#16a085")

    area_Label = Label(area_window , text="Convert Area", width=15, fg="black", bg="#e8f6f3", padx=30, pady=15, font=("arial black",16))
    area_Label.place(x=50, y=20)

    # Entry widget
    number = StringVar()
    number = Entry(area_window, width=15, border=5, font=("arial", 16))
    number.place(x=100, y=100)

    #output label
    output_label = Label(area_window ,width=1, padx=120, pady=10, font=("arial black",11), relief="solid", borderwidth=2)
    output_label.place(x=75, y=250)

    # dropdown menu
    area_options = [
        "Sq. Millimiter",
        "Sq. Centimeter", 
        "Sq. Metre", 
        "Sq. Kilometer", 
        "Sq. Mile", 
        "Sq. Foot",
        "Hectare",
        "Acre"
    ]

    converted_area = {
        "Sq. Millimiter" : 0.000001,  
        "Sq. Centimeter" : 0.0001,  
        "Sq. Metre" : 1.0,
        "Sq. Kilometer" : 1000000.0,
        "Sq. Mile" : 2590000.0,  
        "Sq. Foot" : 0.0929,
        "Hectare" : 10000.0,  
        "Acre" : 4046.856,
    }
    
    # Options Menu to Convert from
    options1 = StringVar()
    options1.set("Convert from")
    drop1 = OptionMenu(area_window, options1,*area_options)
    drop1.place(x=65, y=165, width=120)

    # Options Menu to Convert To
    options2 = StringVar()
    options2.set("Convert to")
    drop2 = OptionMenu(area_window, options2, *area_options)
    drop2.place(x=220, y=165, width=120)
   
    def pop_answer():

        #comparing the dropdown menus
        drop1 = options1.get()
        drop2 = options2.get()
               
        try:
            num = float(number.get())
            answer = num    
            if drop1 in area_options != drop2 in area_options:
                answer = num * converted_area[drop1]/converted_area[drop2]
                output_label.config(text = answer)

            else:
                output_label.config(text="Error!! Check Units")

        except ValueError:
            output_label.config(text="Invalid Input!!")
    

    def cancel():
        # Clear the input and output field
        number.delete(0,END)
        output_label.config(text="")

        #Reset the menu options
        options1.set("Convert from")
        options2.set("Convert to")
    
    # Answer and Close Buttons
    answer_button =Button(area_window, text="Answer", padx=10, command=pop_answer)
    answer_button.place(x=100, y=340)
    close_button =Button(area_window, text="Cancel", padx= 15, command=cancel)
    close_button.place(x=250, y=340)
    

#######################################################################################################################################################################
#######################################################################################################################################################################

def myDistance():
    distance_window = Toplevel()
    distance_window .title("Distance Conversion")
    distance_window .geometry("400x400")
    distance_window .resizable(0,0)
    distance_window .configure(bg="#ff33ff")

    distance_Label = Label(distance_window , text="Convert Distance", width=15,fg="black",bg="#e8f6f3", padx=30, pady=15, font=("arial black",16))
    distance_Label.place(x=50, y=20) # bg="#e8f6f3"


    # Entry widget
    number = StringVar()
    number = Entry(distance_window, width=15, border=5, font=("arial", 16))
    number.place(x=100, y=100)

    #output label
    output_label = Label(distance_window, width=1, padx=120, pady=10, font=("arial black",11), relief="solid", borderwidth=2)
    output_label.place(x=75, y=250)

    # dropdown menu
    distance_options = [
        "Millimeter", 
        "Centimeter", 
        "Metre", 
        "Kilometer", 
        "Miles", 
        "Yards"
    ]

    converted_distance = {
       "Millimeter": 0.001, 
        "Centimeter": 0.01, 
        "Metre": 1.0, 
        "Kilometer": 1000.0, 
        "Miles": 1609.344, 
        "Yards": 0.9144
    }

    # Convert from
    options1 = StringVar()
    options1.set("Convert from")
    drop1 = OptionMenu(distance_window, options1, *distance_options)
    drop1.place(x=65, y=165, width=120)

    # Convert To
    options2 = StringVar()
    options2.set("Convert To")
    drop2 = OptionMenu(distance_window, options2, *distance_options)
    drop2.place(x=220, y=165, width=120)

    def pop_answer():       
        #comparing the dropdown menus
        drop1 = options1.get()
        drop2 = options2.get()

        try:
            # capturing the value entered || en(try widget
            num = float(number.get())
            answer = num    
            if drop1 in distance_options != drop2 in distance_options:
                answer = num * converted_distance[drop1]/converted_distance[drop2]
                output_label.config(text = answer)

            else:
                output_label.config(text="Error!! Check Units")

        except ValueError:
            output_label.config(text="Invalid Input")

    def cancel():
        # Clear the input and output field
        number.delete(0,END)
        output_label.config(text="")

        #Reset the menu options
        options1.set("Convert from")
        options2.set("Convert to")

    # Answer and Close Buttons
    answer_button =Button(distance_window, text="Answer", padx=10, command=pop_answer)
    answer_button.place(x=100, y=340)
    close_button =Button(distance_window , text="Cancel", padx= 15, command=cancel)
    close_button.place(x=250, y=340)

#######################################################################################################################################################################
#######################################################################################################################################################################

def myWeight():
    weight_window = Toplevel()
    weight_window.title("Weight Conversion")
    weight_window.geometry("400x400")
    weight_window.resizable(0,0)
    weight_window.configure(bg="#7f00ff")

    weight_Label = Label(weight_window , text="Convert Weight", width=15, fg="black", bg="#e8f6f3", padx=30, pady=15, font=("arial black",16))
    weight_Label.place(x=50, y=20)


    # Entry widget
    number = StringVar()
    number = Entry(weight_window, width=15, border=5, font=("arial", 16))
    number.place(x=100, y=100)

    #output label
    output_label = Label(weight_window, width=1, padx=120, pady=10, font=("arial black",11), relief="solid", borderwidth=2)
    output_label.place(x=75, y=250)

    # dropdown menu
    weight_options = [
        "Milligram",
        "Gram", 
        "Kilogram",  
        "Pound", 
        "Ton",
        "Ounce"    
    ]

    converted_weight = {
        "Milligram": 0.001,
        "Gram": 1.0, 
        "Kilogram": 1000.0, 
        "Pound": 453.592, 
        "Ton" : 1000000.0,
        "Ounce": 28.3495
    }

    # Convert from
    options1 = StringVar()
    options1.set("Convert from")
    drop1 = OptionMenu(weight_window, options1, *weight_options)
    drop1.place(x=65, y=165, width=120)

    # Convert To
    options2 = StringVar()
    options2.set("Convert To")
    drop2 = OptionMenu(weight_window, options2,*weight_options)
    drop2.place(x=220, y=165, width=120)
    

    def pop_answer():
        # capturing values selected in the drop down menu || convertions
        drop1 = options1.get()
        drop2 = options2.get()

        try:
            # capturing the value entered || entry widget
            num = float(number.get())
            answer = num

            if drop1 in weight_options != drop2 in weight_options:
                answer = num * converted_weight[drop1]/converted_weight[drop2]
                output_label.config(text = answer)

            else:
                output_label.config(text="Error!! Check Units")

        except ValueError:
            output_label.config(text="Invalid Input")


    def cancel():
        # Clear the input and output field
        number.delete(0,END)
        output_label.config(text="")

        #Reset the menu options
        options1.set("Convert from")
        options2.set("Convert to")

    # Answer and Close Buttons
    answer_button =Button(weight_window, text="Answer", padx=10, command=pop_answer)
    answer_button.place(x=100, y=340)
    close_button =Button(weight_window, text="Cancel", padx= 15, command=cancel)
    close_button.place(x=250, y=340)


#####################################################################################################################################################################
#######################################################################################################################################################################

def myVolume():
    volume_window = Toplevel()
    volume_window.title("Volume Conversion")
    volume_window.geometry("400x400")
    volume_window.resizable(0,0)
    volume_window.configure(bg="#606060")

    volume_Label = Label(volume_window, text="Convert Volume", width=15, fg="black", bg="#e8f6f3", padx=30, pady=15, font=("arial black",16))
    volume_Label.place(x=50, y=20)

    # Entry widget
    number = StringVar()
    number = Entry(volume_window, width=15, border=5, font=("arial", 16))
    number.place(x=100, y=100)

    # Output Label
    output_label = Label(volume_window, width=1, padx=120, pady=10, font=("arial black", 11), relief="solid", borderwidth=2)
    output_label.place(x=75, y=250)

    # dropdown menu
    volume_options = [
        "Litre", 
        "Milliliter", 
        "Cubic Metre", 
        "Cubic Centimeter", 
        "Gallon"
    ]

    converted_volume = {
        "Litre": 1.0, 
        "Milliliter": 0.001, 
        "Cubic Metre": 1000.0, 
        "Cubic Centimeter": 0.001, 
        "Gallon": 3.785
    }

    # Convert from
    options1 = StringVar()
    options1.set("Convert from")
    drop1 = OptionMenu(volume_window, options1, *volume_options)
    drop1.place(x=65, y=165, width=120)

    # Convert To
    options2 = StringVar()
    options2.set("Convert To")
    drop2 = OptionMenu(volume_window, options2, *volume_options)
    drop2.place(x=220, y=165, width=120)

    def pop_answer():
        # capturing values selected in the drop down menu || convertions
        drop1 = options1.get()
        drop2 = options2.get()

        try:
            # capturing the value entered || entry widget
            num = float(number.get())
            answer = num

            if drop1 in volume_options != drop2 in volume_options:
                answer = num * converted_volume[drop1]/converted_volume[drop2]
                output_label.config(text = answer)

            else:
                output_label.config(text="Error!! Check Units")

        except ValueError:
            output_label.config(text="Invalid Input")

    def cancel():
        # Clear the input and output field
        number.delete(0,END)
        output_label.config(text="")

        #Reset the menu options
        options1.set("Convert from")
        options2.set("Convert to")

    # Answer and Close Buttons
    answer_button =Button(volume_window, text="Answer", padx=10, command=pop_answer)
    answer_button.place(x=100, y=340)
    close_button =Button(volume_window, text="Cancel", padx= 15, command=cancel)
    close_button.place(x=250, y=340)


#####################################################################################################################################################################
#######################################################################################################################################################################

def myTime():
    time_window = Toplevel()
    time_window.title("Time Conversion")
    time_window.geometry("400x400")
    time_window.resizable(0,0)
    time_window.configure(bg="#006600")

    time_Label = Label(time_window, text="Convert Time", width=15, fg="black", bg="#e8f6f3", padx=30, pady=15, font=("arial black",16))
    time_Label.place(x=50, y=20)

    # Entry widget
    number = StringVar()
    number = Entry(time_window, width=15, border=5, font=("arial", 16))
    number.place(x=100, y=100)

    # Output Label
    output_label = Label(time_window, width=1, padx=120, pady=10, font=("arial black", 11), relief="solid", borderwidth=2)
    output_label.place(x=75, y=250)

    # dropdown menu
    time_options = [
        "Milliseconds",
        "Seconds",
        "Minutes",
        "Hours",
        "Days",
        "Weeks",
        "Months",
        "Years"
    ]

    converted_time = {
        "Milliseconds": 0.001,
        "Seconds": 1.0,
        "Minutes": 60.0,
        "Hours": 3600.0,
        "Days": 86400.0,
        "Weeks": 604800.0,
        "Months": 2628002.88,
        "Years": 31536000.0
    }

    # Convert from
    options1 = StringVar()
    options1.set("Convert from")
    drop1 = OptionMenu(time_window, options1, *time_options)
    drop1.place(x=65, y=165, width=120)

    # Convert To
    options2 = StringVar()
    options2.set("Convert To")
    drop2 = OptionMenu(time_window, options2, *time_options)
    drop2.place(x=220, y=165, width=120)

    def pop_answer():
        # capturing values selected in the drop down menu || convertions
        drop1 = options1.get()
        drop2 = options2.get()

        try:
            # capturing the value entered || entry widget
            num = float(number.get())
            answer = num

            if drop1 in time_options != drop2 in time_options:
                answer = num * converted_time[drop1]/converted_time[drop2]
                output_label.config(text = answer)

            else:
                output_label.config(text="Error!! Check Units")

        except ValueError:
            output_label.config(text="Invalid Input")

    def cancel():
        # Clear the input and output field
        number.delete(0,END)
        output_label.config(text="")

        #Reset the menu options
        options1.set("Convert from")
        options2.set("Convert to")

    # Answer and Close Buttons
    answer_button =Button(time_window, text="Answer", padx=10, command=pop_answer)
    answer_button.place(x=100, y=340)
    close_button =Button(time_window, text="Cancel", padx= 15, command=cancel)
    close_button.place(x=250, y=340)


#####################################################################################################################################################################
#######################################################################################################################################################################

def myTemperature():
    temperature_window = Toplevel()
    temperature_window.title("Temperature Conversion")
    temperature_window.geometry("400x400")
    temperature_window.resizable(0,0)
    temperature_window.configure(bg="#ff6666")

    temperature_Label = Label(temperature_window, text="Convert Temperature", width=15, fg="black", bg="#e8f6f3", padx=30, pady=15, font=("arial black",16))
    temperature_Label.place(x=50, y=20)

    # Entry widget
    number = StringVar()
    number = Entry(temperature_window, width=15, border=5, font=("arial", 16))
    number.place(x=100, y=100)

    # Output Label
    output_label = Label(temperature_window, width=1, padx=120, pady=10, font=("arial black", 11), relief="solid", borderwidth=2)
    output_label.place(x=75, y=250)

    # dropdown menu
    temperature_options = [
        "Celsius",
        "Fahrenheit",
        "Kelvin"
    ]

    converted_temperature = {
        "Celsius": 1.0,
        "Fahrenheit": 33.8,
        "Kelvin": 274.15
    }

    # Convert from
    options1 = StringVar()
    options1.set("Convert from")
    drop1 = OptionMenu(temperature_window, options1, *temperature_options)
    drop1.place(x=65, y=165, width=120)

    # Convert To
    options2 = StringVar()
    options2.set("Convert To")
    drop2 = OptionMenu(temperature_window, options2, *temperature_options)
    drop2.place(x=220, y=165, width=120)

    def pop_answer():
        # capturing values selected in the drop down menu || convertions
        drop1 = options1.get()
        drop2 = options2.get()
 
        try:
            # capturing the value entered || entry widget
            num = float(number.get())
            answer = num

            if drop1 in temperature_options != drop2 in temperature_options:
                answer = num * converted_temperature[drop1]/converted_temperature[drop2]
                output_label.config(text = answer)

            else:
                output_label.config(text="Error!! Check Units")

        except ValueError:
            output_label.config(text="Invalid Input")

    def cancel():
        # Clear the input and output field
        number.delete(0,END)
        output_label.config(text="")

        #Reset the menu options
        options1.set("Convert from")
        options2.set("Convert to")

    # Answer and Close Buttons
    answer_button =Button(temperature_window, text="Answer", padx=10, command=pop_answer)
    answer_button.place(x=100, y=340)
    close_button =Button(temperature_window, text="Cancel", padx= 15, command=cancel)
    close_button.place(x=250, y=340)


#####################################################################################################################################################################
#######################################################################################################################################################################

# Creating a main window label
myLabel = Label(myWindow, text="Standard Unit Converter",fg="black", bg="#e8f6f3", padx=50, pady=20, font=("arial black",16))
myLabel.place(x=60, y=20)

myButton1 = Button(myWindow, text="Area", pady=5, padx=38, command=myArea)
myButton1.place(x=80, y=150)
myButton2 = Button(myWindow, text="Distance", pady=5, padx=28, command=myDistance)
myButton2.place(x=300, y=150)
myButton3 = Button(myWindow, text="Weight", pady=5, padx=30, command=myWeight)
myButton3.place(x=80, y=220)
myButton4 = Button(myWindow, text="Volume", pady=5, padx=30, command=myVolume)
myButton4.place(x=300, y=220)
myButton5 = Button(myWindow, text="Time", pady=5, padx=30, command=myTime)
myButton5.place(x=80, y=290)
myButton6 = Button(myWindow, text="Temperature", pady=5, padx=18, command=myTemperature)
myButton6.place(x=300, y=290)

myWindow.mainloop()