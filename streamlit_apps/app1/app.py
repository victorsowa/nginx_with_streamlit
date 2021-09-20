import random

import streamlit as st

from_value = st.number_input('From value', 1, 10)
to_value = st.number_input('To value', 11, 20)
give_random_number_button = st.button('Give me a number')
random_integer = random.randint(from_value, to_value)

if give_random_number_button:
    st.write(random_integer)
