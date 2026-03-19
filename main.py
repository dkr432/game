import streamlit as st
import random
import time

st.title("🎮 Game Recommender")

st.write("좋아하는 게임을 입력하세요 (쉼표로 구분)")

user_input = st.text_input("Example: minecraft, valorant")

game_recommendations = {
    "minecraft": ["Terraria", "Roblox", "Stardew Valley"],
    "league of legends": ["Dota 2", "Smite", "Heroes of the Storm"],
    "valorant": ["CS:GO", "Overwatch 2", "Rainbow Six Siege"],
    "genshin impact": ["Honkai Star Rail", "Zelda Breath of the Wild", "Tower of Fantasy"],
    "fortnite": ["Apex Legends", "PUBG", "Call of Duty Warzone"]
}

if st.button("🎲 추천 받기"):
    user_games = user_input.lower().split(",")

    results = []

    for game in user_games:
        game = game.strip()
        if game in game_recommendations:
            results += game_recommendations[game]

    if not results:
        st.error("추천 데이터를 찾지 못했어요 😢")
    else:
        game = random.choice(results)

        placeholder = st.empty()

        # 타이핑 애니메이션 효과
        text = ""
        for char in game:
            text += char
            placeholder.markdown(f"## ✨ 추천 게임: {text}")
            time.sleep(0.05)
