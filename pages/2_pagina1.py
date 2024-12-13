import streamlit as st

st.title("Pagina 1")
st.write("pagina 1")


st.page_link("pages/1_pagina2.py", label="Ir a pagina 2")


number1 = st.number_input("Insert number 1")

number2 = st.number_input("Insert number 2")

if st.button("sumar"):
    #st.write(f"tengo tu numero y es: {number1}")
    #st.write(f"tengo tu otro numero y es: {number2}")
    sol = int(number1) + int(number2)
    st.write (f"tu numero {sol}")


######################
# metemos funcion 'lambda'

res = (lambda x, y: x+y) (number1, number2)

if res:
    st.write(res)