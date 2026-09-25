import streamlit as st

from utils.api_client import api_client
from utils.auth_guard import check_authentification
from utils.log_init import get_page_logger

# Protection de la page
check_authentification()

st.title("Player's stats")
logger = get_page_logger("player_stats")

def get_player_data(player_id):
    """Appelle l'API via l'api_client pour récupérer les données du joueur."""
    try:
        # The endpoint /player/{player_id} matches the sequence diagram in backend/README.md
        response = api_client.get(f"/player/{player_id}")
        
        if hasattr(response, 'raise_for_status'):
            response.raise_for_status()
            return response.json()
        
        return response
        
    except Exception as err:
        logger.error(f"Erreur lors de la récupération des données du joueur {player_id}: {err}")
        return None

# --- LOGIQUE PRINCIPALE ---

# 1. Récupérer l'ID via st.query_params
player_id = st.query_params.get("player_id")

if player_id:
    # Appel de l'API
    player_data = get_player_data(player_id)

    if player_data:
        # --- AFFICHAGE DES INFORMATIONS DU JOUEUR ---
        
        # A. Username dans un st.subheader
        username = player_data.get("username", "Inconnu")
        st.subheader(f"👤 {username}")

        # B. Utilisation de st.columns pour créer 2 colonnes
        col1, col2 = st.columns(2)

        with col1:
            # col1: elo dans un st.metric
            elo = player_data.get("elo", "N/A")
            st.metric(label="Elo Rating", value=elo)

        with col2:
            # col2: email avec st.write et checkbox pour Pokemon fan
            email = player_data.get("email", "Non renseigné")
            
            # FIX: Changed 'is_pokemon_fan' to 'pokemon_fan' to match backend/src/business_object/player.py
            is_pokemon_fan = player_data.get("pokemon_fan", False)
            
            st.write(f"**Email :** {email}")
            
            # Affichage de la checkbox (désactivée car c'est de l'affichage de stats)
            st.checkbox("Pokémon Fan ⚡", value=is_pokemon_fan, disabled=True)
            
    else:
        st.error("Impossible de récupérer les données du joueur. Vérifiez l'ID.")
else:
    st.warning("Aucun ID de joueur trouvé dans l'URL. Utilisez `?player_id=...`")