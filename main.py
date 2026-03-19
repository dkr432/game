import streamlit as st
import random

st.title("🎮 Game Recommender")

user_input = st.text_input("좋아하는 게임 입력 (선택)")

game_recommendations = {
"minecraft": ["Terraria","Stardew Valley","Valheim"],
"valorant": ["CS2","Apex Legends","Overwatch 2"],
"league of legends": ["Dota 2","Smite"]
}

game_images = {

"Terraria":"https://upload.wikimedia.org/wikipedia/en/1/1b/Terraria_Steam_artwork.jpg",

"Stardew Valley":"https://upload.wikimedia.org/wikipedia/en/f/fd/Stardew_Valley.png",

"Valheim":"https://upload.wikimedia.org/wikipedia/en/5/5d/Valheim_cover_art.jpg",

"CS2":"https://upload.wikimedia.org/wikipedia/en/6/6e/Counter-Strike_2.jpg",

"Apex Legends":"https://upload.wikimedia.org/wikipedia/en/d/db/Apex_legends_cover.jpg",

"Overwatch 2":"https://upload.wikimedia.org/wikipedia/en/8/8c/Overwatch_2_Steam_artwork.jpg",

"Dota 2":"https://upload.wikimedia.org/wikipedia/en/3/31/Dota_2_Steam_artwork.jpg",

"Smite":"https://upload.wikimedia.org/wikipedia/en/8/88/Smite_cover.jpg"
}

all_games = list(game_images.keys())

if st.button("🎲 추천 받기"):

    results = []

    if user_input:
        user_games = user_input.lower().split(",")

        for game in user_games:
            game = game.strip()
            if game in game_recommendations:
                results += game_recommendations[game]

    if not results:
        results = all_games

    game = random.choice(results)

    st.header(f"🎮 추천 게임: {game}")

    if game in game_images:
        st.image(game_images[game])
