import streamlit as st
# import pyperclip
import pint
u = pint.UnitRegistry()


# st.title('Akel Units')


def converter(f, t):
    return u(f).to(u(t)).magnitude


f = st.text_input('From')
t = st.text_input('To')

if t and f:
    c = converter(f, t)
    st.markdown(f'From ({f}) to ({t})\n{c}')
    # st.markdown(c)
    # pyperclip.copy(c)

# if st.button("Convert"):
#     st.markdown(f'From {f} to {t}')
#     c = converter(f, t)
#     st.markdown(c)
#     pyperclip.copy(c)

# st.markdown(pint.UnitRegistry())
