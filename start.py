import customtkinter

def button_callback():
    app.destroy()
    import black
    black.main()

def button_callback2():
    app.destroy()
    import white
    white.main()

app = customtkinter.CTk()
app.geometry("1200x700")

button = customtkinter.CTkButton(app,width=500,height=100, text="Dark", font=("Arial", 80), command=button_callback,fg_color="#B010F7",hover_color="#660192",text_color="#242424",corner_radius=100)
button.place(x=50 , y = 300)
 
button2 = customtkinter.CTkButton(app,width=500,height=100, text="light",font=("Arial",80), command=button_callback2,fg_color="#B010F7",hover_color="#660192",text_color="#242424",corner_radius=100)
button2.place(x = 670 , y = 300)

app.mainloop()