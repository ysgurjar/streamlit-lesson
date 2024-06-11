import streamlit as st

st.title(":blue[Calculator app]")
st.write('---')

# Create three col layout
col1,col2,col3 = st.columns(3)

with col1.container():
    first = st.number_input(":grey[Enter first integer]", key="first_number")
    

with col2.container():
    second = st.number_input(":grey[Enter first integer]", key="second_number")

with col3.container():
    option = st.selectbox(
    ":grey[Select operation]",
    ("Add", "Subtract", "Multiply","Divide"))


def execute():
    st.write("hey the function executed")
    


st.button("Calculate", type="secondary", on_click=execute)
