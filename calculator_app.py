import streamlit as st

num1 = st.number_input("please enter a numner")
num2 = st.number_input("please enter a second number")

import streamlit as st

operation = st.selectbox(
    'Choose the operation',
    ('Add', 'Substract', 'Divide','Multiply'))

if operation == 'Add':
    st.write(num1+num2)
elif operation == 'Substract':
    st.write(num1-num2)
elif operation == 'Multiply':
    st.write(num1*num2)
elif operation == 'Divide':
    st.write(num1/num2)
else:
    st.write('No operation added')