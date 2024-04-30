from tkinter import*
from PIL import Image,ImageTk
from random import randint


root = Tk()
root.title("rock paper scissors")
root.configure(background="pink")


#picture
rock_img = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissor.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("comp_rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("comp_paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("comp_scissor.png"))


#insert image
user_label1 = Label(root,image=scissor_img,bg='pink')
user_label1.grid(row=1,column=4)
comp_label1 = Label(root,image=scissor_img_comp,bg='pink')
comp_label1.grid(row=1,column=0)


playerScore = Label(root, text=0, font=100, bg="pink", fg="black")
computerScore = Label(root, text=0, font=100, bg="pink", fg="black")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1,column=3)


user_indicator = Label(root, font=50, text="USER", bg="#9b59b6", fg="white")
comp_indicator = Label(root, font=50, text="COMPUTER", bg="#9b59b6", fg="white")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0,column=1)


#messages
msg = Label(root,font=50,bg='pink',fg ='white')
msg.grid(row=3,column=2)


def updateMessage(x):
    msg['text'] = x
def updateUserScore():
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
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    else:
        pass


choices = ["rock", "paper", "scissor"]


def updateChoice(x):
    compChoice = choices [randint(0, 2)]
    if compChoice == "rock":
        comp_label1.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label1.configure(image=paper_img_comp)
    else:
        comp_label1.configure(image=scissor_img_comp)

    if x == "rock":
        user_label1.configure(image=rock_img)
    elif x == "paper":
        user_label1.configure(image=paper_img)
    else:
        user_label1.configure(image=scissor_img)
    checkWinner(x,compChoice)


#buttons
rock = Button(root, width=20, height=2, text="ROCK",bg="#FF3E4D", fg="white",command = lambda:updateChoice("rock")).grid(row=2, column=1)
paper = Button(root, width=20, height=2, text="PAPER",bg="#FAD02E", fg="white",command = lambda:updateChoice("paper")).grid(row=2, column=2)
scissor = Button(root, width=20, height=2, text="SCISSOR", bg="#0ABDE3",fg="white",command = lambda:updateChoice("scissor")).grid(row=2,column=3)


root.mainloop()