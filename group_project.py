from tkinter import*  #to generate the graphical user interface
from PIL import Image,ImageTk #to show the image 
from random import randint # to generate random numbers


graphical_interface = Tk() #Used to initialize Tkinter to create a window
graphical_interface.title("rock paper scissors") #Giving the title as Rock Paper Scissor to the GUI
graphical_interface.configure(background="pink") #Changing the background colour of the GUI to pink


#defining the picture of the player choice
rock_img = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissor.png"))
#defining the picture of the computer random choice
rock_img_comp = ImageTk.PhotoImage(Image.open("comp_rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("comp_paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("comp_scissor.png"))


#inserting the initial image as scissors in the GUI
player_label = Label(graphical_interface,image=scissor_img,bg='pink') 
player_label.grid(row=1,column=4)
computer_label = Label(graphical_interface,image=scissor_img_comp,bg='pink')
computer_label.grid(row=1,column=0)


#creating labels to show the scores and setting the initial scores as zero
playerScore = Label(graphical_interface, text=0, font=100, bg="pink", fg="black")
computerScore = Label(graphical_interface, text=0, font=100, bg="pink", fg="black")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1,column=3)


#creating labels to show the computer side and player side on the top
player_indicator = Label(graphical_interface, font=50, text="PLAYER", bg="purple", fg="white")
computer_indicator = Label(graphical_interface, font=50, text="COMPUTER", bg="purple", fg="white")
player_indicator.grid(row=0, column=3)
computer_indicator.grid(row=0,column=1)


#creating a label to show messages of the result(win or loose or tie)
msg = Label(graphical_interface,font=50,bg='pink',fg ='white')
msg.grid(row=3,column=2)


def updateMessage(x):
    msg['text'] = x
def updateplayerScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"]=str(score)
def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"]=str(score)

def checkWinner(player,computer):
    if player == computer:
        updateMessage("It's a tie")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage ("You Win")
            updateplayerScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateplayerScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateplayerScore()
    else:
        pass


choices = ["rock", "paper", "scissor"]


#creating a function to update player choice by taking button input and computer choice by using random number generated
def updateChoice(x):
    computerChoice = choices[randint(0, 2)]
    if computerChoice == "rock":
        computer_label.configure(image=rock_img_comp)
    elif computerChoice == "paper":
        computer_label.configure(image=paper_img_comp)
    else:
        computer_label.configure(image=scissor_img_comp)

    if x == "rock":
        player_label.configure(image=rock_img)
    elif x == "paper":
        player_label.configure(image=paper_img)
    else:
        player_label.configure(image=scissor_img)
    checkWinner(x,computerChoice)


#inserting buttons to take the player choice and commanding to update the player label
rock = Button(graphical_interface, width=20, height=2, text="ROCK",bg="#FF3E4D", fg="white",command = lambda:updateChoice("rock")).grid(row=2, column=1)
paper = Button(graphical_interface, width=20, height=2, text="PAPER",bg="#FAD02E", fg="white",command = lambda:updateChoice("paper")).grid(row=2, column=2)
scissor = Button(graphical_interface, width=20, height=2, text="SCISSOR", bg="#0ABDE3",fg="white",command = lambda:updateChoice("scissor")).grid(row=2,column=3)


graphical_interface.mainloop()
