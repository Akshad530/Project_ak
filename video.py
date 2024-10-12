import streamlit as st
st.balloons()
st.title("#Python and it's project with code ")
st.markdown(":pencil:")
st.write("#Please fill out the form below to submit your entry.")
st.write("Here is code to ShutDown / Restart / Restart Time / Logout code")
st.write("Example:")
st.code("""for i in range(1,5,1):
from tkinter import *
import os
st=Tk()
st.title("Shutdown app")
st.geometry("500x500")
st.config(bg="Blue")
def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def logout():
    os.system("shutdown -l")
def shutdown():
    os.system("shutdown r /t /1")
r_button=Button(st,text="Restart",font=("Times New Roman",20,"bold"),relief=RAISED,cursor="hand2",command=restart)
r_button.place(x=150,y=60,height=50,width=200)
rt_button=Button(st,text="Restart time",font=("Times New Roman",20,"bold"),relief=RAISED,cursor="hand2",command=restart_time)
rt_button.place(x=150,y=170,height=50,width=200)
lg_button=Button(st,text="Log-Out",font=("Times New Roman",20,"bold"),relief=RAISED,cursor="hand2",command=logout)
lg_button.place(x=150,y=270,height=50,width=200)
st_button=Button(st,text="Shutdown",font=("Times New Roman",20,"bold"),relief=RAISED,cursor="hand2",command=shutdown)
st_button.place(x=150,y=370,height=50,width=200)
st.mainloop()
")
        """)

st.image("images.png",width=400,caption="What is Python")
st.write("Displaying Audio........")
audio=open("Python.mp3","rb")
audio_bytes= audio.read()
st.audio(audio_bytes,format="audio/ogg")
st.video("https://www.youtube.com/watch?v=Y8Tko2YC5hA&t=2s")
# Display a message
st.write("Python is a popular programming language. It was created by Guido van Rossum and released in 1991.")

# Display a list of what Python can be used for
st.write("It is used for:")
uses = [
    "Web development (server-side)",
    "Software development",
    "Mathematics",
    "System scripting"
]
for use in uses:
    st.write(f"- {use}")

# Display what Python can do
st.write("What can Python do?")
st.write("Python can be used on a server to create web applications.")
st.write("Python can be used alongside software to create workflows.")
name = st.text_input("Enter your name:")
fname = st.text_input("Enter your father's name:")
adr = st.text_area("Enter your address:")
mb = st.text_input("Enter mobile number:")
st.radio("Enter your gender:",["Male","Female","TransGender"])
st.selectbox("Enter your course: ",["Python","Java","C++"])
classdata=st.selectbox("Enter your class:",(1,2,3,4,5,6,7,8,9,10))
button = st.button("Done")

st.markdown(f"""
    Name={name}
    FatherName:{fname}
    Address:{adr}
    MobileNumber:{mb}
    Class:{classdata}""")

st.info("Information on user")
st.success("Congragulation! You Have Learn't What is Python?")