import streamlit as st
st.title('Classify text')
a, b = 1, 0


option = st.sidebar.selectbox('What type of event?', ['flood', 'drought'])
if option == 'drought':
  "You selected drought, but it's not available"
input_text = st.sidebar.text_input('Enter some text')

'text is:', input_text