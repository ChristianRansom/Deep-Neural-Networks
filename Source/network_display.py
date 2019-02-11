from tkinter import *
from tkinter import ttk
import network_tester

class GUI: 
    
    def __init__(self):
        
        self.root = Tk()
        style = ttk.Style()
        style.configure("BW.TLabel", background="grey", forground="blue")
        self.root.geometry("600x400")
        #self.root.title("Feet to Meters")
        self.root.config(background='grey')

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        self.draw_frame = ttk.Frame(self.root, padding="10 10 10 10", style = "BW.TLabel")
        self.draw_frame.pack(side="top", fill='both', expand=1)
        
        self.draw_frame['borderwidth'] = 5
        self.draw_frame['relief'] = 'raised'        
        self.canvas = Canvas(self.draw_frame)
        self.canvas.pack(fill=BOTH,  expand=1)
        
        button_frame = ttk.Frame(self.root, padding="3 3 3 3").pack(fill='both')
        
        restart_button = ttk.Button(button_frame, text="Start", command=self.start).pack(side="left", fill='both', expand=1)
        quit_button = ttk.Button(button_frame, text="Quit", command=self.quit_game).pack(side="right", fill='both', expand=1)
        

        self.root.focus_force()
        
        
        self.root.bind('<Return>', self.start)
        
        
        
        self.root.mainloop()

        
    #need args* paramater because its passed by tk for the input types of frames
    def start(self, *args):
        
        self.canvas.update()
        #self.canvas.itemconfigure(self.canvas_frame, width=width, height=event.height)
        h = self.canvas.winfo_height()
        w = self.canvas.winfo_width()
        mid_point = [w / 2, h / 2]
        node_size = h / 10
        
        print(str(self.canvas.winfo_height()))
        print(str(self.canvas.winfo_width()))
        #self.canvas.create_rectangle(0, 0, w, h, 
        #    outline="#f11", fill="#1f1", width=2)
        
        self.canvas.create_oval(mid_point[0] - node_size / 2, mid_point[1] - node_size / 2, 
                                mid_point[0] + node_size / 2, mid_point[1] + node_size / 2, 
                                outline="blue", 
                                fill="blue", width=2)  
        
        network_tester.test()
        
    def quit_game(self):
        sys.exit(0)


class Window(Frame):    
  
    def __init__(self, master=None):
        super().__init__(master)   
         
        self.initUI()
        
        
    def initUI(self):
        
        self['borderwidth'] = 2
        self['relief'] = 'sunken'
        self.pack(fill=BOTH, expand=1)


        canvas = Canvas(self) #create a canvas with the parent being this window class
        print(str(self.winfo_reqheight()))
        canvas.create_rectangle(0, 0, self.winfo_reqheight(), self.winfo_reqwidth(), 
            outline="#f11", fill="#1f1", width=2)          
        
        canvas.create_oval(10, 10, 80, 80, outline="#f11", 
            fill="#1f1", width=2)
        canvas.create_oval(110, 10, 210, 80, outline="#f11", 
            fill="#1f1", width=2)
        canvas.create_rectangle(230, 10, 290, 60, 
            outline="#f11", fill="#1f1", width=2)
        canvas.create_arc(30, 200, 90, 100, start=0, 
            extent=210, outline="#f11", fill="#1f1", width=2)
            
        points = [150, 100, 200, 120, 240, 180, 210, 
            200, 150, 150, 100, 200]
        canvas.create_polygon(points, outline='#f11', 
            fill='#1f1', width=2)
        
        canvas.pack(fill=BOTH, expand=1)

if __name__ == '__main__':
    GUI()        
     
    