import streamlit as st
import random

st.set_page_config(page_title="Game Recommender", layout="wide")

st.title("🎮 AI Game Recommender")

st.write("좋아하는 게임을 입력하세요 (선택)")

user_input = st.text_input("Example: minecraft, valorant")

# 게임 데이터
games = {

"Minecraft":{
"genre":"sandbox",
"image":"https://upload.wikimedia.org/wikipedia/en/5/51/Minecraft_cover.png"
},

"Terraria":{
"genre":"sandbox",
"image":"https://upload.wikimedia.org/wikipedia/en/1/1b/Terraria_Steam_artwork.jpg"
},

"Stardew Valley":{
"genre":"simulation",
"image":"https://upload.wikimedia.org/wikipedia/en/f/fd/Stardew_Valley.png"
},

"Valheim":{
"genre":"sandbox",
"image":"https://upload.wikimedia.org/wikipedia/en/5/5d/Valheim_cover_art.jpg"
},

"Valorant":{
"genre":"fps",
"image":"https://upload.wikimedia.org/wikipedia/en/b/ba/Valorant_cover.jpg"
},

"CS2":{
"genre":"fps",
"image":"https://upload.wikimedia.org/wikipedia/en/6/6e/Counter-Strike_2.jpg"
},

"Apex Legends":{
"genre":"fps",
"image":"https://upload.wikimedia.org/wikipedia/en/d/db/Apex_legends_cover.jpg"
},

"Overwatch 2":{
"genre":"fps",
"image":"https://upload.wikimedia.org/wikipedia/en/8/8c/Overwatch_2_Steam_artwork.jpg"
},

"League of Legends":{
"genre":"moba",
"image":"https://upload.wikimedia.org/wikipedia/en/7/77/League_of_Legends_logo.png"
},

"Dota 2":{
"genre":"moba",
"image":"https://upload.wikimedia.org/wikipedia/en/3/31/Dota_2_Steam_artwork.jpg"
}

}

game_names = list(games.keys())

def recommend_games(user_games):

    genres = []

    for g in user_games:
        g = g.strip().lower()

        for name in games:
            if name.lower() == g:
                genres.append(games[name]["genre"])

    results = []

    for name,data in games.items():

        if not genres:
            results.append(name)

        elif data["genre"] in genres:
            results.append(name)

    return random.sample(results, min(3,len(results)))

if st.button("🎲 추천 받기"):

    if user_input:
        user_games = user_input.split(",")
    else:
        user_games = []

    recs = recommend_games(user_games)

    cols = st.columns(len(recs))

    for i,game in enumerate(recs):

        with cols[i]:
            st.image(games[game]["image"])
            st.subheader(game)
