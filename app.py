from pathlib import Path

import streamlit as st
from PIL import Image
import base64


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
profile_pic = current_dir / "assets" / "profile-pic.png"
picture = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Shania Canoy | Portfolio"
PAGE_ICON = "🌸"
NAME = "Shania Canoy"
DESCRIPTION = """
Senior Data Analyst, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "canoy.shania@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://youtube.com/c/codingisfun",
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
    "Twitter": "https://twitter.com",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
st.write("---")
col1, col2 = st.columns([2, 2], gap="large")
with col1:
    st.image("assets/Me.svg", width=420)
with col2:
    st.image("assets/Hello.svg", width=380)

#-- SOCIALS --
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
assets_dir = current_dir / "assets"

def load_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

icons = {
    "GitHub": load_base64_image(assets_dir / "github-hover.svg"),
    "LinkedIn": load_base64_image(assets_dir / "linkedin-hover.svg"),
    "Behance": load_base64_image(assets_dir / "behance-hover.svg"),
    "Facebook": load_base64_image(assets_dir / "facebook-hover.svg"),
}

software_icons = {
    "Figma": load_base64_image(assets_dir / "figma.svg"),
    "Adobe Illustrator": load_base64_image(assets_dir / "illustrator.svg"),
    "Adobe Photoshop": load_base64_image(assets_dir / "photoshop.svg"),
    "Canva": load_base64_image(assets_dir / "canva.svg"),
    "Email": load_base64_image(assets_dir / "email.svg"),
}

st.write("---")
# Social media links
social_media_links = {
    "GitHub": "https://github.com/shaniacc",
    "LinkedIn": "https://linkedin.com/in/shaniacanoy",
    "Behance": "https://www.behance.net/shanbright",
    "Facebook": "https://facebook.com/shania.cachin",
}

cols = st.columns(4)

for index, (platform, link) in enumerate(social_media_links.items()):
    encoded_string = icons[platform]
    cols[index].markdown(
        f"""
        <div style="text-align:center;">
            <a href="{link}" style="text-decoration:none;">
                <img src="data:image/svg+xml;base64,{encoded_string}" alt="{platform} Icon" style="width:16px; vertical-align:middle; margin-right:10px;">
                <span style="vertical-align:middle;">{platform}</span>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write('\n')
st.write('\n')
st.write("---")

# --- ABOUT ME ---
col1, col2 = st.columns([3, 2], gap="small")
with col1:
    st.markdown(
        """
        <h2><b>All About <span style="color:#FDBFD5">Me ⋆˚✿˖°</span></b></h2>
        <p>Hi! I'm <span style="color:#FDBFD5">Shania</span>, an aspiring graphic and UI/UX designer based in the Philippines.  I’m currently studying in 
        <span style="color:#FDBFD5">Cebu Institute of Technology-University</span>, and I strive to create impactful and visually stunning publications by having perfect balance between aesthetics and functionality in my designs.<p>
        <p>
        With an open mind and a determination to excel, I am dedicated to honing my skills and making a lasting impact in the world of visual communication and Information Technology.
        🫧</p>
        """,
        unsafe_allow_html=True
    )
with col2:
    st.write('\n')
    st.write('\n')
    st.image("assets/Me2.svg", width=300)

# --- CORE SKILLS ---
st.write('\n')
st.write('\n')

col1, col2, col3 = st.columns([2,2,2.5], gap="small")

with col1:
    container = st.container(border=True)
    container.write(
        """
        🎨 Graphic Design
        """,
        unsafe_allow_html=True
    )
with col2:
    container = st.container(border=True)
    container.write(
        """
        ✨ UI/UX Design
        """,
        unsafe_allow_html=True
    )
with col3:
    container = st.container(border=True)
    container.write(
        """
        🖥️ Frontend Development
        """,
        unsafe_allow_html=True
    )

# --- EXPERIENCE ---
st.write('\n')
st.write("---")
st.markdown(
    """
    <h3><b><span style="color:#FDBFD5">Experience</span> ⋆⭒˚｡⋆</b></h3>
    """,
    unsafe_allow_html=True
)
col1, col2= st.columns([2,2], gap="small")

# Experience 1
with col1:
    container = st.container(border=True)
    container.write(
        """
        <p style="font-size:16px">SY 2021 - 2022 (First Semester)</p>
        <p style="color:#FDBFD5; font-size:18px"><b>Media and Publications Committee Staff in Computer Students Society</b></p>
        <p style="font-size:16px">Cebu Institute of Technology - University</>
        """,
        unsafe_allow_html=True
    )
# Experience 2
with col2:
    container = st.container(border=True)
    container.write(
       """
        <p style="font-size:16px">SY 2023 - present</p>
        <p style="color:#FDBFD5; font-size:18px"><b>Graphic Designer in Google
Developer Student Clubs CIT-U Chapter</b></p>
        <p style="font-size:16px">Cebu Institute of Technology - University</>
        """,
        unsafe_allow_html=True
    )

st.write('\n')
st.write("---")

# Function to render software icons and progress bars
def render_skill(icon_key, skill_name, progress_value):
    coll1, coll2 = st.columns([0.5, 3], gap="small")
    with coll1:
        st.markdown(
            f"""
            <div>
                <img src="data:image/svg+xml;base64,{software_icons[icon_key]}" alt="{skill_name} Icon" style="width:34px; vertical-align:middle; margin-right:10px;">
            </div>
            """, 
            unsafe_allow_html=True
        )
    with coll2:
        st.progress(progress_value, text=skill_name)

# --- Software Skills ---
st.markdown(
    """
    <h3><b><span style="color:#FDBFD5">Software Skills</span> ⋆⭒˚｡⋆</b></h3>
    """,
    unsafe_allow_html=True
)

container = st.container(border=True)

# Add two columns inside the container
with container:
    st.write('\n')
    col1, col2, col3, col4 = st.columns([0.2,2,2,0.2], gap="small")

    # Figma and Illustrator Column
    with col2:
        render_skill('Figma', 'Figma', 80)
        render_skill('Adobe Illustrator', 'Adobe Illustrator', 70)

    # Photoshop and Canva Column
    with col3:
        render_skill('Adobe Photoshop', 'Adobe Photoshop', 70)
        render_skill('Canva', 'Canva', 90)
    st.write('\n')

#--- My Projects ---
st.markdown(
    """
    <h3><b>My <span style="color:#FDBFD5">Works⋆˚✿˖°</span> </b></h3>
    """,
    unsafe_allow_html=True
)

tab1, tab2, tab3, tab4, = st.tabs(["Publication Material", "Brochure", "Logo", "Mobile Design"])

with tab1:
    st.image("assets/Work1.svg")
with tab2:
    st.image("assets/Work2.svg")
with tab3:
    st.image("assets/Work3.svg")
with tab4:
    st.image("assets/Work4.svg")

# --- FOOTER ---
st.write('\n')
st.write('---')
col1, col2 = st.columns([2, 2])
with col1:
    st.write('\n')
    st.write('\n')
    st.image("assets/ty.svg", width=300)
    st.write('\n')
    st.markdown(
        f"""
        <div style="text-align:center;">
            <a href="mailto:canoy.shania@gmail.com" style="text-decoration:none;">
                <img src="data:image/svg+xml;base64,{software_icons['Email']}" alt="{"email"} Icon" style="width:32px; vertical-align:middle; margin-right:10px;">
                <span style="vertical-align:middle; font-weight:100">{EMAIL}</span>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write('\n')
    st.write('\n')
    # Custom button with specified width using HTML and CSS
    st.markdown(
        """
        <style>
        .custom-button {
            display: inline-block;
            padding: 10px 20px;
            font-size: 16px;
            color: white;
            background-color: #1D1D1D;
            text-align: center;
            text-decoration: none;
            border-radius: 40px;
            width: 330px;  /* Adjust the width as needed */
            border: 1px solid #fff;
            font-weight: 100;
        }
        </style>
        <div style="text-align:center;">   
        <a href="https://www.figma.com/design/ZwoviibdNPR8CPrX5uQAnF/Designs-Archives?node-id=0-1&t=zjQBs6DnIehtcphq-1" class="custom-button">Visit My Design Archives</a>
        </div>
        """,
        unsafe_allow_html=True
    )
with col2:
    st.image("assets/footer-me.svg", width=350)

st.write('\n')
st.write('\n')
st.write('\n')
st.write('---')

#--- Footer ---
st.markdown(
    f"""
    <div style="text-align:center;">   
        <p style="font-size:12px; color: #A7A7A7">Copyright © 2024 Shania Canoy. All rights reserved.</p>
        </div>
    """,
    unsafe_allow_html=True
    )

# --- EXTRA EXTRA HI SIR ----
st.snow()

