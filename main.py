# The game is a game of ball and bars where the player has to avoid hitting the bars
# and the bars go up continuously while the ball can be moved at all four directions.
# The speed at which the bar go up increases and the score is the amount of time spent
# by the player in the game


# imports all the required modules and libs
import sys
try:
    import tkinter
    from time import sleep, time 
    from random import choice   
    from tkinter import messagebox, PhotoImage
except ImportError:
    print("Unresolved libraries!")

    # Exists the program in CPython but in Ipython, it shuts off the kernel
    sys.exit()


class game:
    def __init__(self,):
        '''The class is a game that uses tkinter-canvas'''

        self.window_height = 800
        self.window_width = 800
        
        self.time = time()
        
        # creates a window
        self.window = tkinter.Tk()
        self.window['height'] = self.window_height
        self.window['width'] = self.window_width
        
        # creates a canvas object sets the background to black and packs it
        self.canvas = tkinter.Canvas(self.window, height=self.window_height, width=self.window_width)

        
        self.canvas.configure(bg='black') 
        
        self.canvas.pack(fill="both",)
    
        self.score = None
        self.ball_pos = [375, 175, 425, 225]
        self.ball_speed = 1
    
        self.bars_x = [x*200 for x in range(3, 5000)]

        self.bars = []
        self.bars_speed = -2

        # creates a score board for the game. The socre is the total time in seconds
        # passed in the game, it starts with 0

        self.score_board = self.canvas.create_text(100,50, text="Score : 0", fill="white", font=('Calibri'))

    def left(self, event):
        '''Event callback that will move the ball towards left'''
        self.canvas.move(self.ball, -50, 0)
    
    def right(self, event):
        '''Event callback that will move the ball towards right''' 
        self.canvas.move(self.ball, 50, 0)
    
    def up(self, event):
        '''Event callback that will move the ball upwards'''
        self.canvas.move(self.ball, 0, -50)
    
    def down(self, event):
        '''Event callback that will move the ball downwards'''
        self.canvas.move(self.ball, 0, 50)
    
    
    def collision_detection(self):
        '''The function determines the collision between the ball and the bar provided
            to the function'''
        
        ball = self.canvas.bbox(self.ball)
        # The following code checks if the co-ordinates of the ball overlaps with other elements
        # using the inbuilt canvas.find_overlapping method
        collision = self.canvas.find_overlapping(ball[0], ball[1], ball[2], ball[3])
        collision = [x for x in collision]
        collision = [obj for obj in collision if obj!=self.ball]

        # returns true if any element is found 
        if(len(collision) > 0):return True
        return False


    def gameloop(self):
        ''' This is main game loop of the game which does most of the tasks like
            moving the ball, moving bars and determining the collision'''
        
        self.ball = self.canvas.create_oval(self.ball_pos, fill='white', outline='gray', width=4)
        
        # loops through the list of numbers on self.bars_x and create bars with the distance between them being 200
        for i in range(0, len(self.bars_x)):
            if(i == 0):y = 0
            elif(i%2==0): y=choice([100,200,300,400])
            else:y=choice([300,400,500,600])

        
            self.bars.append(self.canvas.create_rectangle(y, self.bars_x[i],  y+200, self.bars_x[i]+25, fill="white"))
            
            
            # the following piece of code binds the arrow keys to the canvas
            self.canvas.focus_set()
            self.canvas.bind('<Up>', self.up)
            self.canvas.bind('<Down>', self.down)
            self.canvas.bind('<Left>', self.left)
            self.canvas.bind('<Right>', self.right)

        # this variable will be set to False when the game is lost by the player
        lose = False
        tick = time()
        # this is the main loop which continues till the user loses the game
        while not lose:
            # moves the ball with the desired speed
            self.canvas.move(self.ball, 0, self.ball_speed)
            
            # loops through the bars created by the instance and moves them with the pre defined speed
            for x,i in enumerate(self.bars):
                self.canvas.move(i, 0, self.bars_speed)

            if(self.collision_detection() == True):
                    messagebox.showinfo("Oops", "Sorry, you lost the game")
                    lose = True
 
            # to prevent from running out of bars,  a new bar is added at each iteration
            self.window.update()
 
            self.score = int(time() - tick)
            self.canvas.itemconfig(self.score_board, text="Score : "+str(self.score))

            # The speed of the game increases every 10 seconds
            if(int(time() - self.time) > 15):
                self.bars_speed -= 2
                self.time = time()

    
# Runs the file if it is being run as a script
if __name__ == "__main__":
    # creates a new instance
    newGame = game()
    # runs the mainloop of the game
    newGame.gameloop()