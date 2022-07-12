import streamlit as st
import pandas

data= {
"Series_1": [1, 2, 3, 4],
"Series_2": [52, 36, 72, 85] 
}
df= pandas.DataFrame(data)

st.title("Our First Streamlit App")
st.subheader("Introducing Streamlit in Automate Everything in Python")
st.write("""This is our first Web App.
Enjoy it!         
""")
st.write(df)
st.line_chart(df)
st.area_chart(df)

myslider= st.slider("Celsius")
st.write(myslider, "in Frenheit is", myslider *9/5 + 32)