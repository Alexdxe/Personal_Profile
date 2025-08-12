#Import necessary libraries
import streamlit as st
from PIL import Image

st.header("Personal Interests/Hobbies")

#Anime
st.subheader("Anime")
st.markdown("Ever since watching Pokemon as a child, I have been fascinated with everything anime. Whether it's the unique art styles, incredible soundtracks, or jaw-dropping story telling, anime has always been a big part of my adolescence. From 2020-2023, it was all I did as a past time. Watch the hottest shows of the anime season, play Japanese Gacha games, and discuss the following topics with friends. While I don't nearly watch as much anime as I do before, it has made a large impact on my music taste, hobbies, and even fashion.")
st.image("C:/Users/alexd/Downloads/Projects/Personal_Profile/images/Screenshot Capture - 2025-08-09 - 16-42-14.png")
st.link_button("MyAnimeList Page!", "https://myanimelist.net/profile/H0ly_Water", type = "secondary")
st.write("")

#Music
st.subheader("Music")
st.markdown("Music is one of my favorite hobbies for so many reasons:")
st.markdown("1) Music is such a powerful form of expression, allowing artists to write and compose their raw emotions into an art for the world to hear.")
st.markdown("2) Music so sentimental, as it can act like a time machine. When a certain song appears, I am reminded of a moment in my life. Whether the moment was walking home to beautful sunset, or a pre-exam review session, music has always been there for me.")
st.markdown("3) Music is one of my favorite conversation starters. I enjoy meeting new people and hearing what their favorite songs and artists are, because in a way, sharing your music taste is sharing a piece of yourself. It's oddly personal, and when you find out that someone enjoys the same music, or even thought the song you reccommended was enjoyable, it's oddly satisfying.")
st.image("C:/Users/alexd/Downloads/Projects/Personal_Profile/images/Screenshot 2025-08-09 171435.png")
st.link_button("My Spotify Page", "https://open.spotify.com/user/alexdxe64")
st.write("")

#Consumer Electronics:
st.subheader("Consumer Electronics")
st.markdown("I am a massive fan of both Mechanical Keyboards and In-Ear Monitors. The aesthetics, sound(produced by the switches and drivers), and experience each give me is why I always comeback to each hobby. Because both niches are so expensive, I try to put as much thought possible into each purcahse spending hours researching on each component(keyboard) and sound profile(IEMs). For now, I have stopped purchasing new keyboards, but have considered a new IEM at a discounted price.")
photos = {
"Keyboards": { 
    "image": Image.open("C:/Users/alexd/Downloads/Projects/Personal_Profile/images/20250811_141426.jpg"),
    "caption": "My current keyboard collection. Keyboards from top to bottom: Neo70(Holy Pandas, off-brand Bocchi the Rock keycaps), Mod008(Oil Kings/Tealios V2, Mizu clones), Blade60(HMX Sonja). Switches from top to bottom: Gateron Melodics, Gateron Type R, TKC Kiwis."
    },
"IEMs": { 
    "image": Image.open("C:/Users/alexd/Downloads/Projects/Personal_Profile/images/20250811_142614.jpg"),
    "caption": "My current IEM collection. IEMs from top left to bottom right: Tangzu Wan'er, Softears Volume, Moondrop Dusk, Moondrop Variations, Thieaudio Oracle, Unique Melody MEST."
    
}
}

choice = st.selectbox("Images:", list(photos.keys()))
st.image(
    photos[choice]["image"],
    caption = photos[choice]["caption"],
    use_container_width=True
)
st.write("")
#Photography

st.subheader("Photography")
st.markdown("As a huge nature enjoyer, I always found myself taking photos of the unique scenary and wildlife at each location I visited. Naturally, this les me to eventually take up photograhpy when I bought my first camera, the Sony A6000. Since then, I have been taking photos of anything I found unique or interesting, and have even upgraded camera lenses. This summer, I have made it my goal to visit a large list of places within the Bay Area, taking as many photos I can of every location I stop by.")
photos = {

    "California Street": {
        "image": Image.open("C:/Users/alexd/Downloads/Projects/Personal_Profile/images/DSC03269.jpg")
    },
    "Chinatown": {
        "image": Image.open("C:/Users/alexd/Downloads/Projects/Personal_Profile/images/DSC03071.jpg")
    },    
    "Coit Tower":{
        "image": Image.open("C:/Users/alexd/Downloads/Projects/Personal_Profile/images/DSC03126.jpg")
    },
    "Fisherman's Wharf": {
        "image": Image.open("C:/Users/alexd/Downloads/Projects/Personal_Profile/images/DSC03764.jpg")
    },
     "Golden Gate Bridge": {
        "image": Image.open("C:/Users/alexd/Downloads/Projects/Personal_Profile/images/DSC03445.jpg")
    },
    "Golden Gate Park": {
        "image": Image.open("C:/Users/alexd/Downloads/Projects/Personal_Profile/images/DSC09083.jpg")    
    },
     "Japantown": {
        "image": Image.open("C:/Users/alexd/Downloads/Projects/Personal_Profile/images/DSC02691.jpg")
    },
    "Japanese Tea Garden": {
        "image": Image.open("C:/Users/alexd/Downloads/Projects/Personal_Profile/images/DSC09109.jpg")
    },
    "Land's End": { 
        "image": Image.open("C:/Users/alexd/Downloads/Projects/Personal_Profile/images/20231126_164406.jpg")
    },
    "Lombard Street": {
        "image": Image.open("C:/Users/alexd/Downloads/Projects/Personal_Profile/images/DSC03845.jpg")
    },
    "Lyon Street Steps": {
        "image": Image.open("C:/Users/alexd/Downloads/Projects/Personal_Profile/images/DSC02751.jpg")
    },
    "McLaren Park":{
        "image": Image.open("C:/Users/alexd/Downloads/Projects/Personal_Profile/images/DSC03401.jpg")
    },
    "Ocean Beach": {
        "image": Image.open("C:/Users/alexd/Downloads/Projects/Personal_Profile/images/DSC09139.jpg")
    },
    "Presidio": {
        "image": Image.open("C:/Users/alexd/Downloads/Projects/Personal_Profile/images/DSC02478.jpg")
    },
    "San Bruno Mountain Park": {
        "image": Image.open("C:/Users/alexd/Downloads/Projects/Personal_Profile/images/DSC01770.jpg")
    },
    "Twin Peaks": {
        "image": Image.open("C:/Users/alexd/Downloads/Projects/Personal_Profile/images/20230912_144329.jpg")
    },
    "UC Davis": {
        "image": Image.open("C:/Users/alexd/Downloads/Projects/Personal_Profile/images/DSC08764.jpg")
    }
}

choice = st.selectbox("Images:", list(photos.keys()))
st.image(
    photos[choice]["image"],
    use_container_width=True
)
st.link_button("My Photographby Account", "https://www.instagram.com/fluid_photoss/")
    