#Import necessary libraries
import streamlit as st
from PIL import Image

#Title and header for the profile page
st.markdown("<h1 style='text-align: center;'>Alexander Cai</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center;'>Welcome to my profile page!</h5>", unsafe_allow_html=True)


#Profile Photo:
photo = Image.open("images/DSC03059.jpg")

#Centering: 
left, center, right = st.columns([1, 2, 1])
with center:
    st.image(photo, width=350)

st.header("About Me")
st.subheader("Education")
st.write("I am currently a 3rd year student at the University of California Davis, pursuing a Bachelor's degree in Data Science, with a minor in Data and Society. My hope is to one day work in a company that values meaningful change to society, bettering the world through data analytics and storytelling.")
st.subheader("Relevant Course Work")
classes = [ 
    ("STA 035A", "Stat Data Science I"),
    ("MAT 021A", "Calculus"),
    ("ECS 017", "Data Logic and Computation"),
    ("STA 035B", "Stat Data Science II"),
    ("ECS 032A", "Intro to Programming"),
    ("MAT 021B", "Calculus II"),
    ("STA 035C", "Stat Data Science III"),
    ("ECS 032B", "Intro to Data Structures"),
    ("STS 100", "Data & Society"),
    ("MAT 021C", "Calculus III"),
    ("STA 108", "Regression Analysis"),
    ("MAT 022A", "Linear Algebra"),
    ("STA 141A", "Statistical Data Science"),
    ("ECS 116", "Databases for Non-Majors")
]
prefix = {
    "Statistics": "STA",
    "Math": "MAT",
    "Computer Science": "ECS",
    "Science and Technology Studies": "STS"
}

selected_prefixes = st.multiselect(
    "Filter by department:",
    options=list(prefix.keys()),
    default=[]
)

if not selected_prefixes:
    filtered_classes = classes
else:
    selected_prefixes = [prefix[label] for label in selected_prefixes]
    filtered_classes = [
        (code, name) for code, name in classes 
        if any(code.startswith(prefix) for prefix in selected_prefixes)
    ]

st.markdown("#### Classes Taken")
for code, name in filtered_classes:
    st.write(f"- **{code}**: {name}")

st.subheader("What Have I Been Up To?")
st.markdown("**1) Projects:** I have been working on a project recently that involves self-recording and analyzing typing performance of different Keyboard switches. Currently, I am on the Data Analysis phase which has been conducted through Juypter Notebooks. My aim is to see if certain factors (price, weight, sound) affect performance like Words Per Minute or accuracy, while also making models to predict my performance based on these factors.")
st.page_link("pages\Projects.py", label="Go to Project Page", icon="📊")

st.markdown("**2) Internships:** I am the current Data Science Manager for Associated Students of UC Davis Pantry. My role is overseeing all data-related tasks, including data analysis, projects, and collection. Currently, I am exploring the different resources needed for the position and brainstorming ideas for future projects.")
st.image("images/logo-white-transparentbg.png", width = 150)
st.write("")

st.markdown("**3) Independent Learning:** Outside of Data Science, I have been learning and practicing the guitar, Japanese (Duolingo) and photography. While these skills are not related to Data Science, they help me develop other skills like pattern recognition, patience, and persistance, which are all important in the field of Data Science.")
photos = {
"Lighthouse": {
    "image": Image.open("images/DSC03650.jpg"),
    "caption": "A photo of the lighthouse at San Francisco's Fort Point, taken on a Sony A6000"
},
 
"Guitar": { 
    "image": Image.open("images/DSC03680.jpg"),
    "caption": "A photo of my Scheter Demnon-6 guitar, currently I am learning the fingerstyle version of 打上花火 by DAOKO and Kenshi Yonezu."
},
"Duolingo": { 
    "image": Image.open("images/Screenshot_20250807_115706_Duolingo.jpg"),
    "caption": "A screenshot of my current Duolingo streak, I have been learning Japanese consistently for the past 2 months, practicing for about 20 minutes a day."
} 
}
choice = st.selectbox("Images:", list(photos.keys()))
st.image(
    photos[choice]["image"],
    caption = photos[choice]["caption"],
    use_container_width=True)