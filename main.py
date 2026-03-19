import streamlit as st
import random
import time

st.title("🎮 Game Recommender")

st.write("좋아하는 게임을 입력하세요 (선택 사항, 쉼표로 구분)")

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
"Honkai Star Rail","Tower of Fantasy","Zelda Breath of the Wild","Ni no Kuni"
],

"fortnite": [
"Apex Legends","PUBG","Call of Duty Warzone","Splitgate"
],

"stardew valley": [
"Harvest Moon","Animal Crossing","Slime Rancher","My Time at Portia"
],

"elden ring": [
"Dark Souls 3","Bloodborne","Sekiro","Lies of P","Monster Hunter World"
]
}

# 전체 게임 목록 생성
all_games = []
for games in game_recommendations.values():
    all_games.extend(games)

if st.button("🎲 추천 받기"):

    results = []

    if user_input:
        user_games = user_input.lower().split(",")

        for game in user_games:
            game = game.strip()
            if game in game_recommendations:
                results += game_recommendations[game]

    # 입력 없거나 매칭 없으면 랜덤 추천
    if not results:
        results = all_games

    game = random.choice(results)

    placeholder = st.empty()

    text = ""
    for char in game:
        text += char
        placeholder.markdown(f"## ✨ 추천 게임: {text}")
        time.sleep(0.04)
