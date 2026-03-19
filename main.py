import streamlit as st
import random
import time

st.title("🎮 Game Recommender")
st.write("좋아하는 게임을 쉼표로 구분해서 입력하세요")

user_input = st.text_input("Example: minecraft, valorant")

game_recommendations = {

"minecraft": [
"Terraria","Roblox","Stardew Valley","No Man's Sky","Valheim","Subnautica"
],

"valorant": [
"CS2","Overwatch 2","Rainbow Six Siege","Apex Legends","Call of Duty Warzone"
],

"league of legends": [
"Dota 2","Smite","Heroes of the Storm","Mobile Legends","Arena of Valor"
],

"genshin impact": [
"Honkai Star Rail","Tower of Fantasy","Zelda Breath of the Wild","Ni no Kuni","Blue Protocol"
],

"fortnite": [
"Apex Legends","PUBG","Call of Duty Warzone","Splitgate","Hyperscape"
],

"stardew valley": [
"Harvest Moon","Animal Crossing","Slime Rancher","My Time at Portia"
],

"elden ring": [
"Dark Souls 3","Bloodborne","Sekiro","Lies of P","Monster Hunter World"
],

"zelda breath of the wild": [
"Genshin Impact","Immortals Fenyx Rising","Skyrim","Horizon Zero Dawn"
],

"skyrim": [
"Witcher 3","Dragon Age Inquisition","Elden Ring","Kingdom Come Deliverance"
]
}

if st.button("🎲 추천 받기"):

    user_games = user_input.lower().split(",")
    results = []

    for game in user_games:
        game = game.strip()
        if game in game_recommendations:
            results += game_recommendations[game]

    if not results:
        st.error("추천 데이터가 부족합니다 😢 다른 게임도 입력해 보세요!")
    else:
        game = random.choice(results)

        placeholder = st.empty()

        text = ""
        for char in game:
            text += char
            placeholder.markdown(f"## ✨ 추천 게임: {text}")
            time.sleep(0.04)
