import streamlit as st
import random
import time

st.title("Math Quiz 🧮")

# Initialize session state to keep track of questions and score
if 'zahl1' not in st.session_state:
    st.session_state.zahl1 = random.randint(1, 10)
    st.session_state.zahl2 = random.randint(1, 10)
    st.session_state.start_time = time.time()

z1 = st.session_state.zahl1
z2 = st.session_state.zahl2

st.write(f"What is {z1} * {z2}?")

# Use Streamlit's input widget
tipp = st.number_input("Your answer:", step=1, value=0)

if st.button("Check Answer"):
    ergebniss = z1 * z2
    if tipp == ergebniss:
        st.success("Правилно! 🎉")
        # Generate new numbers for next time
        st.session_state.zahl1 = random.randint(1, 10)
        st.session_state.zahl2 = random.randint(1, 10)
        st.button("Next Question")
    else:
        st.error("Грешка! Опитай пак! ❌")

end = int(time.time() - st.session_state.start_time)
st.info(f"Time passed: {end} seconds")
