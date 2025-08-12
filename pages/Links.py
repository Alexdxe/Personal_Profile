#Import necessary libraries
import streamlit as st
from PIL import Image

st.header("Links")

#LinkedIn
st.subheader("LinkedIn")
st.image("C:/Users/alexd/Downloads/Projects/Personal_Profile/images/LinkedIn-Logo.wine.png", width = 500)
st.markdown("Feel free to connect with me on LinkedIn!")
st.link_button("My LinkedIn Profile", "https://www.linkedin.com/in/alexander-cai-8b1694365/", type="primary")
st.write("")

#GitHub
st.subheader("GitHub")
st.image("C:/Users/alexd/Downloads/Projects/Personal_Profile/images/maxresdefault.jpg", width = 500)
st.markdown("Visit my GitHub to see all of the code for my projects.")
st.link_button("My LinkedIn Profile", "https://github.com/Alexdxe", type="primary")
st.write("")

#Photography Account
st.subheader("Photography")
st.image("C:/Users/alexd/Downloads/Projects/Personal_Profile/images/Instagram_icon.png",  width = 250)
st.markdown("Check out my photography account on Instagram. Feel free to message me if you ever need photos.")
st.link_button("My Photography Account", "https://www.instagram.com/fluid_photoss/", type="primary")
st.write("")