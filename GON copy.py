import random
import streamlit as st

# --- Interface ---
st.set_page_config(page_title="Gon Freecs 🤖", page_icon="💬")

# --- Title ---
st.title(" 💜 Bienvenue au jeu Pierre, Feuille, Ciseau ! ")
st.write("Choisis une option ci dessous, puis clique sur 'Jouer'.")
st.divider()
# --- Option possibles ---
options = ["Pierre", "Feuille", "Ciseaux"]

# Initialiser des scores dans session_state ---
if "score_joueur" not in st.session_state:
    st.session_state.score_joueur = 0
if "score_Gon" not in st.session_state:
    st.session_state.score_Gon = 0
if "egalites" not in st.session_state:
    st.session_state.egalites = 0

# Le joueur choisit
joueur = st.selectbox("Fais ton choix:", options)

# --- Bouton pour jouer ---
if st.button("Jouer"):
    
    # L'ordinateur choisit aléatoirement
    Gon  = random.choice(options)
    st.write(f"Gon a choisi : **{Gon}**")
    #Comparer les choix 
    if joueur == Gon:
        st.write(" 🤝 Égalité ! ")
        st.image("https://www.icegif.com/wp-content/uploads/2022/09/icegif-70.gif", width=300) #Gif egalites
        st.session_state.egalites += 1
    elif (joueur == "Pierre" and Gon == "Ciseaux") or \
         (joueur == "Feuille" and Gon == "Pierre") or \
         (joueur == "Ciseaux" and Gon == "Feuille"):
        st.write("🎉 Tu gagnes ! ")
        st.image("https://www.icegif.com/wp-content/uploads/2022/09/icegif-69.gif", width=300)  # GIF victoire joueur
        st.session_state.score_joueur += 1
    else:
        st.write("💻 Gon gagne hahahahaha 💚 ! ")
        st.image("https://www.icegif.com/wp-content/uploads/icegif-4878.gif", width=300) # GIF victoire Gon
        st.session_state.score_Gon += 1
    
    # --- Affichage des scores ---
st.divider()
st.subheader("📊 Score actuel")
st.write(f"👤 Joueur : {st.session_state.score_joueur}")
st.write(f"💻 Gon : {st.session_state.score_Gon}")
st.write(f"⚖️ Égalités : {st.session_state.egalites}")
