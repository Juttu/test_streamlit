
import streamlit as st 

f = open ("students.txt", "a")

f.write("a")

f1 = open ("students.txt", "r")
contents=f1.readlines()
print(contents)


f.close()

st.metric(label="Temperature", value=contents[0], delta="100 °F")

