import streamlit as st
# import pyperclip
import pint
u = pint.UnitRegistry()


# st.title('Akel Units')


def converter(f, t):
    return f.to(t).magnitude


f = u(st.text_input('From'))
t = u(st.text_input('To'))

if t and f:
    if t.magnitude != 1:
        st.error(f'"To" cannot have magnitude')

    elif f.dimensionality != t.dimensionality:
        st.error('Dimensionality mismatch')
    else:
        c = converter(f, t)
        full = f'From ({f:P~}) to ({t:P~})\n\n{c}'
        st.markdown(full)



#         st.components.v1.html('''
# <button class="button" onclick="myFunction()">Copy Conversion</button>


# <script>
# function myFunction() {
# navigator.clipboard.writeText("'''+ str(c) +'''");
# }
# </script>

# <style>
# .button {
#   display: inline-block;
#   padding: 15px 25px;
#   font-size: 24px;
#   cursor: pointer;
#   text-align: center;
#   text-decoration: none;
#   outline: none;
#   color: #fff;
#   background-color: #4CAF50;
#   border: none;
#   border-radius: 15px;
#   box-shadow: 0 9px #999;
# }

# .button:hover {background-color: #3e8e41}

# .button:active {
#   background-color: #3e8e41;
#   box-shadow: 0 5px #666;
#   transform: translateY(4px);
# }
# </style>

#         ''')



