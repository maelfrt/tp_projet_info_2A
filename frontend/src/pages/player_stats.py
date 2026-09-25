"""
Streamlit page displaying a player's stats.

Endpoints used:
    GET /player/{id_player}
"""

import streamlit as st

from utils.api_client import api_client
from utils.auth_guard import check_authentification
from utils.log_init import get_page_logger

st.title("Player stats")
logger = get_page_logger("player_stats")

check_authentification()

id_player = st.query_params.get("id_player")

if id_player is None:
    st.error("No player specified")
    st.stop()

response = api_client.get(f"/player/{id_player}")

if response["status_code"] != 200:
    st.error("Error loading player")
    st.stop()

player_data = response["data"]

st.subheader(player_data["username"])

col1, col2 = st.columns(2)

with col1:
    st.metric("Elo", player_data["elo"])

with col2:
    st.write(f"📧 {player_data['email']}")
    st.checkbox(
        "Pokemon fan",
        value=player_data.get("is_pokemon_fan", False),
        disabled=True,
    )