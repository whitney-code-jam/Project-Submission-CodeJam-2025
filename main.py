import tkinter as tk
from tkinter import ttk

from google import genai

KEY = "AIzaSyBqdPE6YEwUc1kfVjrAVBjmLfR8OUBFu2o"

root = tk.Tk()
root.title("Psyched In")
root.state("zoomed")
img = tk.PhotoImage(file="psychedin_logo.png")
root.iconphoto(False, img)


# chat frame
chat_frame = ttk.Frame(root, padding="10")
chat_frame.pack(fill=tk.BOTH, expand=True)

chat_history = tk.Text(chat_frame, state="disabled", wrap="word", bg="lightgrey")  # text stuff printed here
chat_history.pack(fill=tk.BOTH, expand=True)

input_frame = ttk.Frame(root, padding="10")
input_frame.pack(fill=tk.X, side=tk.BOTTOM)


user_input = ttk.Entry(input_frame, width=80)
user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))

send_button = ttk.Button(input_frame, text="Send")
send_button.pack(side=tk.RIGHT)

chatbot_options = ["General", "Workout Routines", "Recipes", "Motivation"]
selected_chatbot = tk.StringVar(value=chatbot_options[0])
chatbot_menu = ttk.OptionMenu(input_frame, selected_chatbot, "General", *chatbot_options)
chatbot_menu.pack(side=tk.LEFT, padx=(0, 10))

sidebar = tk.Frame(root, width=200, bg="black")
sidebar.pack(side=tk.LEFT, fill=tk.Y)


# alter egos for the ai
def send_message(event=None):
    message = user_input.get()
    user_input.delete(0, tk.END)
    match selected_chatbot.get():
        case "General":
            prompt = "You are a health and wellness assistant. Respond to the following prompt with a general response.\n"
        case "Workout Routines":
            prompt = "You are a health and wellness assistant. Respond to the following prompt with a workout routine.\n"
        case "Recipes":
            prompt = "You are a health and wellness assistant. Respond to the following prompt with a recipe.\n"
        case "Motivation":
            prompt = "You are a health and wellness assistant. Respond to the following prompt with a motivational quote.\n"
    if message:
        client = genai.Client(api_key=KEY)

        response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt + message)
        response = response.text.replace("**", "")

        chat_history.config(state="normal")
        chat_history.insert(tk.END, "You: " + message + "\n")
        chat_history.insert(tk.END, "Bot: " + response + "\n")
        chat_history.config(state="disabled")


send_button.config(command=send_message)
root.bind("<Return>", send_message)

root.mainloop()
