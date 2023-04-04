from tkinter import *
from PIL import *
from PIL import ImageTk, Image
import random

root = Tk()

root.geometry("1000x1000")
root.title("Endless Pokemon Game")
root.configure(background="yellow2")

img_btn = ImageTk.PhotoImage(Image.open("button.jpg"))


text = [
    "Abra","Bulbasour","Charmender","Iyvasour","Jigglypuff","Kadabra","Meowth","Nidoking","Paras","Persion","Pikachu","Ratata","Squirtle"
]

PokemonCards = {
    "Abra": ImageTk.PhotoImage(Image.open("abra.jpg")),
    "Bulbasour": ImageTk.PhotoImage(Image.open("bulbasour.jpg")),
    "Charmender": ImageTk.PhotoImage(Image.open("charmender.jpg")),
    "Iyvasour": ImageTk.PhotoImage(Image.open("Iyvasour.jpg")),
    "Jigglypuff": ImageTk.PhotoImage(Image.open("jigglypuff.jpg")),
    "Kadabra": ImageTk.PhotoImage(Image.open("kadabra.jpg")),
    "Meowth":  ImageTk.PhotoImage(Image.open("meowth.jpg")),
    "Nidoking": ImageTk.PhotoImage(Image.open("meowth.jpg")),
    "Paras": ImageTk.PhotoImage(Image.open("paras.jpg")),
    "Persion": ImageTk.PhotoImage(Image.open("persion.jpg")),
    "Pikachu": ImageTk.PhotoImage(Image.open("pikachu.jpg")),
    "Ratata": ImageTk.PhotoImage(Image.open("ratata.jpg")),
    "Squirtle": ImageTk.PhotoImage(Image.open("squirtle.jpg"))
}

dict_cards_val = {
    "Abra":"30",
    "Bulbasour":"60",
    "Charmender":"50",
    "Iyvasour":"100",
    "Jigglypuff":"70",
    "Kadabra":"70",
    "Meowth":"60",
    "Nidoking":"90",
    "Paras":"40",
    "Persion":"70",
    "Pikachu":"200",
    "Ratata":"40",
    "Squirtle":"50"
}

label_player1_title = Label(root, text="Player 1", bg="royal blue", fg="white")
label_player1_title.place(relx=0.2, rely=0.3, anchor=CENTER)

label_player2_title = Label(root, text="Player 2", bg="royal blue", fg="white")
label_player2_title.place(relx=0.8, rely=0.3, anchor=CENTER)

label_player1_score = Label(root, bg="royal blue", fg="white")
label_player1_score.place(relx=0.2, rely=0.4, anchor=CENTER)

label_player2_score = Label(root, bg="royal blue", fg="white")
label_player2_score.place(relx=0.8, rely=0.4, anchor=CENTER)

label_players_time_score = Label(root, bg="chocolate1", fg="white")
label_players_time_score.place(relx=0.5, rely=0.5, anchor=CENTER)

player1_score = 0

def player1():
    global player1_score
    random1 = random.randint(0, 11)
    text1 = text[random1]
    label_players_time_score["image"] = PokemonCards[text1]
    score = dict_cards_val[text1]
    player1_score += int(score)
    label_player1_score["text"] = str(player1_score)

player2_score = 0

def player2():
    global player2_score
    random2 = random.randint(0, 11)
    text2 = text[random2]
    label_players_time_score["image"] = PokemonCards[text2]
    score1 = dict_cards_val[text2]
    player2_score += int(score1)
    label_player2_score["text"] = str(player2_score)

btn_player1 = Button(root, image=img_btn, command=player1)
btn_player1.place(relx=0.1, rely=0.6)

btn_player2 = Button(root, image=img_btn, command=player2)
btn_player2.place(relx=0.8, rely=0.6)

root.mainloop()