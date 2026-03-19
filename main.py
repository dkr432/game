import streamlit as st
import random
import time

st.title("🎮 Game Recommender")

st.write("좋아하는 게임을 입력하세요 (선택, 쉼표로 구분)")
user_input = st.text_input("Example: minecraft, valorant")

# 추천 데이터
game_recommendations = {
    "minecraft": ["Terraria", "Roblox", "Stardew Valley", "Valheim"],
    "valorant": ["CS2", "Overwatch 2", "Rainbow Six Siege", "Apex Legends"],
    "league of legends": ["Dota 2", "Smite", "Heroes of the Storm"],
    "genshin impact": ["Honkai Star Rail", "Tower of Fantasy"],
    "stardew valley": ["Harvest Moon", "Slime Rancher"]
}

# 게임 이미지 데이터
game_images = {
    "Terraria": "https://cdn.cloudflare.steamstatic.com/steam/apps/105600/header.jpg",
    "Roblox": "https://tr.rbxcdn.com/180DAY-9b9c8c9d5a2c0f0d1c0c0f0d1c0c0f0d/768/432/Image/Webp/noFilter",
    "Stardew Valley": "https://cdn.cloudflare.steamstatic.com/steam/apps/413150/header.jpg",
    "Valheim": "https://cdn.cloudflare.steamstatic.com/steam/apps/892970/header.jpg",
    "CS2": "https://cdn.cloudflare.steamstatic.com/steam/apps/730/header.jpg",
    "Overwatch 2": "https://static.playoverwatch.com/img/share/overwatch2.jpg",
    "Rainbow Six Siege": "https://cdn.cloudflare.steamstatic.com/steam/apps/359550/header.jpg",
    "Apex Legends": "https://cdn.cloudflare.steamstatic.com/steam/apps/1172470/header.jpg",
    "Dota 2": "https://cdn.cloudflare.steamstatic.com/steam/apps/570/header.jpg",
    "Smite": "https://cdn.cloudflare.steamstatic.com/steam/apps/386360/header.jpg",
    "Heroes of the Storm": "https://blz-contentstack-images.akamaized.net/v3/assets/blt2477dcaf4ebd440c/blt6a3c32b678f85b45/5d02a2e4c9e77c2d94d0f6d1/share.jpg",
    "Honkai Star Rail": "https://upload-os-bbs.hoyolab.com/upload/2023/04/26/1e9a9c5f7c1d0e7c3b0b8a7c8d9a.jpg",
    "Tower of Fantasy": "https://cdn.cloudflare.steamstatic.com/steam/apps/2064650/header.jpg",
    "Harvest Moon": "https://upload.wikimedia.org/wikipedia/en/5/5a/Harvest_Moon_cover.jpg",
    "Slime Rancher": "https://cdn.cloudflare.steamstatic.com/steam/apps/433340/header.jpg"
}

# 전체 게임 목록
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

    if not results:
        results = all_games

    game = random.choice(results)

    # 타이핑 애니메이션
    placeholder = st.empty()
    text = ""
    for char in game:
        text += char
        placeholder.markdown(f"## 🎮 추천 게임: {text}")
        time.sleep(0.04)

    # 이미지 표시
    if game in game_images:
        st.image(game_images[game], caption=game)
