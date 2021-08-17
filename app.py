from tkinter import *
from main import get_response

FONT = "ComicSans 12"
FONT_BOLD = "ComicSans 14 bold"
splash_root = Tk()

# Adjust size
splash_root.geometry("470x491")

# Set Label
photo=PhotoImage(file='2.png')
splash_label = Label(splash_root, text="Splash Screen", font=18,image=photo)
splash_label.pack()

def main():
    # destory splash window
    splash_root.destroy()

# Set Interval
splash_root.after(5000, main)

# Execute tkinter
mainloop()

class ChatApplication:

    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("~Metis")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=550, bg="#17202A")

        #headlabel
        head_label = Label(self.window, bg="gray20", fg="lawn green", text="Virtual Chat Assistant", font=FONT, pady=10)
        head_label.place(relwidth=1)

        #tiny divider
        line = Label(self.window, width=450, bg="gray95")
        line.place(rely=0.07, relheight=0.012)

        #text widget
        self.text_widget= Text(self.window, width= 20, height=2, bg="grey11", fg="lawn green", font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)#0.745
        self.text_widget.configure(cursor="arrow",state=DISABLED)

        #scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.993, width=7, height =1)
        scrollbar.configure(command=self.text_widget.yview)

        #bottom label
        bottom_label = Label(self.window, bg="grey20", height= 80)
        bottom_label.place(relwidth=1, rely=0.825)

        #message entry box
        self.msg_entry = Entry(bottom_label, bg="gray12", fg="lawn green", font=FONT)#bg for entry box bg and fg for text inside it
        self.msg_entry.place(relwidth=.74, relheight=0.04, rely=0.0185, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        #send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=25, bg="grey11",fg= "lawn green", command= lambda: self._on_enter_pressed(None))
        send_button.place(relx=.77, rely=0.0185, relheight=0.04, relwidth= 0.22)

    def _on_enter_pressed(self, event):
        msg= self.msg_entry.get()#this gets the input text as a string
        self._insert_message(msg, "You")

    def _insert_message(self, msg, sender):
        if not msg:
            return
        self.msg_entry.delete(0,END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        msg2 = f"Metis: {get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)

if __name__ == "__main__":
    app = ChatApplication()
    app.run()
    
