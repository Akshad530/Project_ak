import streamlit as st

def main():
    """Main function to run the Streamlit app"""
st.title("Welcome to My Website")
st.header("Main")
st.markdown("I love python")
st.code("""for i in range(1,5,1):
                print("Hello")
        """)
name = st.text_input("Enter your name:")
fname = st.text_input("Enter your father's name:")
adr = st.text_area("Enter your Text:")
classdata=st.selectbox("Enter your class:",(1,2,3,4,5,6,7,8,9,10))
button = st.button("Done")
if button:
    st.markdown(f"""
    Name={name}
    FatherName:{fname}
    Address:{adr}
    Class:{classdata}""")
