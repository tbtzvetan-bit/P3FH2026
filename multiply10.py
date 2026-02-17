import streamlit as st
import random

st.title("Математическа игра")

# This creates a "memory" so the numbers don't change every time you type
if 'z1' not in st.session_state:
    st.session_state.z1 = random.randint(1, 10)
    st.session_state.z2 = random.randint(1, 10)

z1 = st.session_state.z1
z2 = st.session_state.z2

st.write(f"### Колко е {z1} * {z2}?")

# Use number_input instead of input()
tipp = st.number_input("Твоят отговор:", value=0, step=1)

if st.button("Провери"):
    if tipp == (z1 * z2):
        st.success("Правилно! 🎉")
        # Change numbers for the next round
        st.session_state.z1 = random.randint(1, 10)
        st.session_state.z2 = random.randint(1, 10)
        st.rerun() # Refresh to show new numbers
    else:
        st.error("Грешка! Опитай пак! ❌")
