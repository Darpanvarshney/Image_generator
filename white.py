import customtkinter as ctk
from PIL import Image
import random

def main():
        
        def draw_rounded_rectangle(canvas, x1, y1, x2, y2, radius=20, **kwargs):
            points = [
                x1 + radius, y1,
                x2 - radius, y1,
                x2, y1,
                x2, y1 + radius,
                x2, y2 - radius,
                x2, y2,
                x2 - radius, y2,
                x1 + radius, y2,
                x1, y2,
                x1, y2 - radius,
                x1, y1 + radius,
                x1, y1
            ]
            return canvas.create_polygon(points, smooth=True, **kwargs)

        def resize_canvas(event=None):
            canvas_width = canvas.winfo_width()
            canvas_height = canvas.winfo_height()
            canvas.delete("all")
            if canvas_width > 0 and canvas_height > 0:
                draw_rounded_rectangle(
                    canvas,
                    0,0, canvas_width, 136, 
                    radius=100,
                    fill="#32383D",
                    outline="#32383D",
                    width=0
                )

        def on_input_change(event=None):
            if prom.get().strip():
                button.configure(state="normal")
            else:
                button.configure(state="disabled")

        def get_text():
            global out_file
            p = prom.get()
            print(p) 
            import image_generator as ig
            pipe =ig.load_model()
            prompt = p
            generated_image_file =ig.generate_image(pipe, prompt, output_file=f"img\{random.randrange(0,99999999)}.png")
            ig.resize_image(generated_image_file, f"img\{random.randrange(0,99999999)}.png", new_width=3840, new_height=2160)
            img_number = random.randrange(0,99999999)
            ig.upscale_image_opencv(generated_image_file,f"img\{img_number}.png", scale=4)
            img = Image.open(f"img\{img_number}.png")
            show_img = ctk.CTkImage(light_image=img,size=(display_frame.winfo_width(),display_frame.winfo_height()))
            display_img.configure(text=" ",bg_color="#2B2B2B")
            display_img.configure(image=show_img)
        
            
        root = ctk.CTk()
        root.geometry("1200x700")


        canvas = ctk.CTkCanvas(root, highlightthickness=0)
        canvas.pack(fill=ctk.BOTH, expand=True)
        canvas.configure(bg="#FFFFFF", border=0)

        image = Image.open("components/logo.png")
        ctk_image = ctk.CTkImage(light_image=image, size=(120, 100))
        logo_var = ctk.CTkLabel(canvas, image=ctk_image,width=100,height=100, text="",fg_color="transparent", bg_color="#32383D",corner_radius=50)
        logo_var.place(x=6,y=6)

        image2 = Image.open("components/title.png")
        ctk_image2 = ctk.CTkImage(light_image=image2, size=(370, 110))
        title_name = ctk.CTkLabel(canvas,width=190, height=40,text="",image=ctk_image2,bg_color="#32383D",fg_color="#32383D",corner_radius=20)
        title_name.pack(pady=0)

        bottom = ctk.CTkCanvas(canvas,highlightthickness=0,)
        bottom.pack(side='bottom',padx=10,)
        bottom.configure(border=0,height=100,bg="#FFFFFF",width=1300)

        prom = ctk.CTkEntry(bottom, placeholder_text="Enter Your Prompt Here",  width=900 ,font=("Inter",24,), height=80,fg_color="#EFEFEF", border_width=0,corner_radius=50)
        prom.pack(side="bottom",pady=10,)


        button_img = Image.open("components/button-2.png")
        ctk_button_image = ctk.CTkImage(light_image=button_img, size=(50, 50))
        button = ctk.CTkButton(bottom, text="",image=ctk_button_image,width=40,height=40,corner_radius=10, 
                                    fg_color="transparent",command=get_text,
                                    text_color="white", bg_color="#EFEFEF",hover=None,state="disabled")
        button.place(relx=0.9, rely=0.2)

        ##################################################### display of image where image will appear after generaton ##################################################################################################################################################################################
        display_canvas = ctk.CTkCanvas(canvas,highlightthickness=0,highlightcolor="#636363")
        display_canvas.pack(pady=10,padx=10,fill=ctk.BOTH,expand=True)
        display_canvas.configure(border=0,height=700,bg="#FFFFFF",)

        display_frame = ctk.CTkFrame(display_canvas,height=600,corner_radius=30,bg_color="#FFFFFF",fg_color="#EFEFEF")
        display_frame.pack(fill = ctk.BOTH,expand = True , padx =20,pady=20)

        display_img = ctk.CTkLabel(display_frame,text="YOUR GENERATED WILL COME HERE",bg_color="#EFEFEF",text_color="#212121",font=("Bold",40))
        display_img.pack(fill = ctk.BOTH,padx = 20,pady=20,expand=True)
        ############################################################################################################################################################################################################################################################################
        root.bind("<Configure>", resize_canvas)
        prom.bind("<KeyRelease>", on_input_change)
        root.update_idletasks()
        resize_canvas()

        root.mainloop()
