import streamlit as st

with st.sidebar:

    st.write("This code will be printed to side")
    if st.button("hola"):
        st.write("hola")




st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.write('hola')

x = 10

st.write(f"Mi numero es {x}")

####################################################
####################################################
####################################################
# repaso 2

#if st.button("Hola"):
    #st.write('has pinchado "Hola"')        # imprimimosdo algo...
    #calcular()                             # o llamamos a una funcion etc.

