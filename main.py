import tkinter as tk
import random
import time

# 간단한 추천 데이터
game_recommendations = {
    "minecraft": ["Terraria", "Roblox", "Stardew Valley"],
    "league of legends": ["Dota 2", "Smite", "Heroes of the Storm"],
    "valorant": ["CS:GO", "Overwatch 2", "Rainbow Six Siege"],
    "genshin impact": ["Honkai Star Rail", "Zelda Breath of the Wild", "Tower of Fantasy"],
    "fortnite": ["Apex Legends", "PUBG", "Call of Duty Warzone"]
}

def recommend():
    user_games = entry.get().lower().split(",")

    results = []
    for game in user_games:
        game = game.strip()
        if game in game_recommendations:
            results += game_recommendations[game]

    if not results:
        results = ["No data 😢 Try popular games!"]

    show_animation(random.choice(results))

def show_animation(text):
    result_label.config(text="")
    
    for i in range(len(text)+1):
        result_label.config(text=text[:i])
        root.update()
        time.sleep(0.05)

# GUI
root = tk.Tk()
root.title("🎮 Game Recommender")
root.geometry("500x300")

title = tk.Label(root, text="Enter games you like (comma separated)", font=("Arial", 14))
title.pack(pady=20)

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

btn = tk.Button(root, text="Recommend Game", command=recommend)
btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 16), fg="blue")
result_label.pack(pady=30)

root.mainloop()
