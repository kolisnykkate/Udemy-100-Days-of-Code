import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
BLACK = "#36454F"
WHITE = "#FFF5EE"

# My way, according to Codex, is correct and better than Angela's way
# try:
#     data = pd.read_csv("data/words_to_learn.csv")
# except FileNotFoundError:
#     data = pd.read_csv("data/english_slang_words_corrected.csv")
# data_list = data.to_dict(orient="records")

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/english_slang_words_corrected.csv")
    data_list = original_data.to_dict(orient="records")
else:
    data_list = data.to_dict(orient="records")

new_word = {}
def random_word():
    global new_word, flip_timer
    window.after_cancel(flip_timer)
    # new_word = data_list[random.randint(0, len(data_list))]["English"]
    new_word = random.choice(data_list)
    # canvas.itemconfig(word_to_learn, text = new_word)
    canvas.itemconfig(card_title, text="English", fill=BLACK)
    canvas.itemconfig(word_to_learn, text=new_word["English"], fill=BLACK)
    canvas.itemconfig(canvas_img, image=card_front_img)
    flip_timer =window.after(1000, flip_card)

def flip_card():
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(card_title, text="Ukrainian", fill = WHITE)
    canvas.itemconfig(word_to_learn,
                      text=new_word["Ukrainian"],
                      fill=WHITE,
                      font=(FONT_NAME, 40, "bold"),
                      width=600,
                      justify="center")

# def learned_word():
#     data_list.remove(new_word)
#     words_to_learn = pd.DataFrame(data_list)
#     words_to_learn.to_csv("data/words_to_learn.csv", index=False)
#
# def rnd_word_learned():
#     random_word()
#     learned_word()

def rnd_word_learned():
    data_list.remove(new_word)
    words_to_learn = pd.DataFrame(data_list)
    words_to_learn.to_csv("data/words_to_learn.csv", index=False)
    random_word()
# UI
window = tk.Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(1000, flip_card)

canvas = tk.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = tk.PhotoImage(file="images/card_front.png")
card_back_img = tk.PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row = 0, column = 0, columnspan = 2)
card_title = canvas.create_text(400, 150, text = "Title", fill = BLACK, font=(FONT_NAME, 40, "italic"))
word_to_learn = canvas.create_text(400, 263, text = "Word", fill = BLACK, font=(FONT_NAME, 40, "bold"))

right_img = tk.PhotoImage(file="images/right.png")
right_btn = tk.Button(image=right_img, highlightthickness=0, bd=0, command = rnd_word_learned)
right_btn.grid(row = 1 , column = 1)

wrong_img = tk.PhotoImage(file="images/wrong.png")
wrong_btn = tk.Button(image=wrong_img, highlightthickness=0, bd=0, command = random_word)
wrong_btn.grid(row = 1 , column = 0)

random_word()


window.mainloop()