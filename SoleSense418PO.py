# Sole Sense GUI (c)2016
# Stacie Zaroban, Peter Oxley
# April 2016
#
# Built for Sole Sense Engineering Project
# by Erik Anderson and Alexis Fesenbek


# Imports
# from tkinter import *
import Tkinter as tk
from time import sleep
from PIL import ImageTk, Image
from tkFileDialog import askopenfilename
import math
import os
import csv


#############################################
# Function: _crate_circle()
# Parameters: object, x-coord, y-coord, radius, other arguments)
# Returns: circle object on canvas
# Description: draws a circle based on center-point instead of corner
# By: Oxley
#############################################
def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle


#############################################
# Function: getColor()
# Parameters: objectID, sensor value (0-1023)
# Returns: new color
# Description: recolor an object
# By: Oxley
#############################################
def getColor(v):
    c = '#' + format(int(((math.ceil(float(v)/float(23)))-(15*(math.floor(float(v)/346))))*(math.pow(16,(math.floor(float(v)/346))))), '03X')
    # print c,
    return c
    #sensorArray.itemconfig(id, fill=c)
    #sensorArray.itemconfig(s, fill='blue')
    #sensorArray.itemconfig(s, fill='blue')


#############################################
# Function: openLeftFile(), openRightFile()
# Parameters: none
# Returns: sensor data in array
# Description: import sensor data into arrays
# By: Oxley
#############################################
left_array = []
def openLeftFile():
    global left_array
    left_array = []
    leftFileText.delete("1.0", tk.END)
    filename = askopenfilename(parent=root,title='Choose a file')
    leftFileText.insert(1.0, os.path.basename(filename))
    left_array = list(csv.reader(open(filename, 'r'), delimiter = ' '))
    #printLeft()

right_array = []
def openRightFile():
    global right_array
    right_array = []
    rightFileText.delete("1.0", tk.END)
    filename = askopenfilename(parent=root,title='Choose a file')
    rightFileText.insert(1.0, os.path.basename(filename))
    right_array = list(csv.reader(open(filename, 'r'), delimiter = ' '))

##def printLeft():
##    for i in range(0,10):#len(left_array)):
##        for j in range(0,10):
##            print left_array[i][j],
##        print ""
##    print "DONE"


#############################################
# flagStop()
# Parameters: none
# Returns: flag
# Description: sets a flag to halt playback
# By: Oxley
#############################################
stop = 0
def stopFlag():
    global stop
    stop = 1    


#############################################
# Function: paintSensors()
# Parameters: none
# Returns: updated color
# Description: writes new sensor color to sensor item
# By: Oxley
#############################################
def paintSensors():
    global stop
    stop = 0
    if(len(left_array) > 0 and len(right_array) > 0):
        lim = ((min(len(left_array), len(right_array))))
    elif(len(left_array) == 0):
        lim = len(right_array)
    elif(len(right_array) == 0):
        lim = len(left_array)
    else:
        return
    for i in range(lim):
        # print str(i),
        if(stop == 0):
            if(len(left_array) > 0):
                sensorArray.itemconfig(L1, fill=getColor(left_array[i][0]))
                sensorArray.itemconfig(L2, fill=getColor(left_array[i][1]))
                sensorArray.itemconfig(L3, fill=getColor(left_array[i][2]))
                sensorArray.itemconfig(L4, fill=getColor(left_array[i][3]))
                sensorArray.itemconfig(L5, fill=getColor(left_array[i][4]))
                sensorArray.itemconfig(L6, fill=getColor(left_array[i][5]))
                sensorArray.itemconfig(L7, fill=getColor(left_array[i][6]))
                sensorArray.itemconfig(L8, fill=getColor(left_array[i][7]))
                sensorArray.itemconfig(L9, fill=getColor(left_array[i][8]))
                sensorArray.itemconfig(L10, fill=getColor(left_array[i][9]))
            if(len(right_array) > 0):
                sensorArray.itemconfig(R1, fill=getColor(right_array[i][0]))
                sensorArray.itemconfig(R2, fill=getColor(right_array[i][1]))
                sensorArray.itemconfig(R3, fill=getColor(right_array[i][2]))
                sensorArray.itemconfig(R4, fill=getColor(right_array[i][3]))
                sensorArray.itemconfig(R5, fill=getColor(right_array[i][4]))
                sensorArray.itemconfig(R6, fill=getColor(right_array[i][5]))
                sensorArray.itemconfig(R7, fill=getColor(right_array[i][6]))
                sensorArray.itemconfig(R8, fill=getColor(right_array[i][7]))
                sensorArray.itemconfig(R9, fill=getColor(right_array[i][8]))
                sensorArray.itemconfig(R10, fill=getColor(right_array[i][9]))
            sensorArray.update_idletasks()
            sleep(.055)


#############################################
# Function: Window and Canvas Setup
# Parameters: none
# Returns: none
# Description: Setup
# By: Zaroban, Oxley
#############################################
    # Window Setup
root = tk.Tk()                                   
root.wm_title("Sole Sense")                      # Window title
root.iconbitmap('icon.ico')
#root.resizable(width=FALSE, height=FALSE)       # Makes the window non-resizable
root.resizable(width=0, height=0)                # false=0 -> 2.7

    # Sole Frame
feet = ImageTk.PhotoImage(file = "PCB_Soles.png")
sensorArray = tk.Canvas(root, width=350, height=500, borderwidth=0, highlightthickness=0, bg="white")
sensorArray.create_image(175, 250, image = feet)
sensorArray.grid()
    # Control frame
controlFrame = tk.Canvas(root, width=600, height=600) #tk -> 2.7
controlFrame.grid(row=0, column=1200, padx=10, pady=2)


#############################################
# Function: Sensor Array Layout
# Parameters: none
# Returns: none
# Description: Place sensors on soles
# By: Oxley
#############################################
L1 = sensorArray.create_circle(125, 169, 12, fill="black", outline="white", width=2)
L2 = sensorArray.create_circle(131, 69, 12, fill="black", outline="white", width=2)
L3 = sensorArray.create_circle(66, 69, 12, fill="black", outline="white", width=2)
L4 = sensorArray.create_circle(89, 141, 12, fill="black", outline="white", width=2)
L5 = sensorArray.create_circle(99, 263, 12, fill="black", outline="white", width=2)
L6 = sensorArray.create_circle(44, 156, 12, fill="black", outline="white", width=2)
L7 = sensorArray.create_circle(56, 227, 12, fill="black", outline="white", width=2)
L8 = sensorArray.create_circle(51, 327, 12, fill="black", outline="white", width=2)
L9 = sensorArray.create_circle(72, 446, 12, fill="black", outline="white", width=2)
L10 = sensorArray.create_circle(101, 402, 12, fill="black", outline="white", width=2)

R1 = sensorArray.create_circle(223, 169, 12, fill="black", outline="white", width=2)
R2 = sensorArray.create_circle(217, 69, 12, fill="black", outline="white", width=2)
R3 = sensorArray.create_circle(282, 69, 12, fill="black", outline="white", width=2)
R4 = sensorArray.create_circle(259, 141, 12, fill="black", outline="white", width=2)
R5 = sensorArray.create_circle(248, 263, 12, fill="black", outline="white", width=2)
R6 = sensorArray.create_circle(305, 156, 12, fill="black", outline="white", width=2)
R7 = sensorArray.create_circle(292, 227, 12, fill="black", outline="white", width=2)
R8 = sensorArray.create_circle(297, 327, 12, fill="black", outline="white", width=2)
R9 = sensorArray.create_circle(275, 446, 12, fill="black", outline="white", width=2)
R10 = sensorArray.create_circle(247, 402, 12, fill="black", outline="white", width=2)


#############################################
# Function: Control Frame Layout
# Parameters: none
# Returns: none
# Description: Place controls in frame
# By: Zaroban
#############################################
logo = Image.open("logo.gif")
logoimage = ImageTk.PhotoImage(logo)
logolabel = tk.Label(controlFrame, image=logoimage)
logolabel.grid(row=1, column=80, columnspan=200, padx=10, pady=2)

newLabel = tk.Label(controlFrame, text="")
newLabel.grid(row=2, column=80, columnspan=200, padx=10, pady=2)

openLeftButton = tk.Button(controlFrame, text="Open Left Foot File", command=openLeftFile)  # tk. -> 2.7 # A command can be added for a click event
openLeftButton.grid(row=3, column=150, padx=10, pady=2)

openRightButton = tk.Button(controlFrame, text="Open Right Foot File", command=openRightFile)  # tk. -> 2.7
openRightButton.grid(row=3, column=200, padx=10, pady=2)

startButton = tk.Button(controlFrame, text="Start", command=paintSensors) # tk. -> 2.7
startButton.grid(row=200, column=175, padx=10, pady=2)
#startButton.grid(row=200, column=150, padx=10, pady=2)

# stopButton = tk.Button(controlFrame, text="Stop") # tk. -> 2.7
# stopButton.grid(row=200, column=175, padx=10, pady=2)

# resetButton = tk.Button(controlFrame, text="Reset") # tk. -> 2.7
# resetButton.grid(row=200, column=200, padx=10, pady=2)

    # Text boxes to confirm user file choice
leftFileText = tk.Text(controlFrame, width=15, height=1, takefocus=0) # tk. -> 2.7
leftFileText.grid(row=7, column=150, padx=10, pady=2)

rightFileText = tk.Text(controlFrame, width=15, height=1, takefocus=0) # tk. -> 2.7
rightFileText.grid(row=7, column=200, padx=10, pady=2)

contributorsLabel = tk.Label(controlFrame, text="\n\n\n\nEngineers: Erik Anderson, Alexis Fesenbek\nGUI Programmers: Peter Oxley, Stacie Zaroban")
contributorsLabel.grid(row=300, column=80, columnspan=200, padx=10, pady=2)



root.mainloop()         # !!Nothing below this runs!!
