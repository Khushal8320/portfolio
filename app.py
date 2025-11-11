import streamlit as st
from streamlit_lottie import st_lottie
import requests
from streamlit_extras.colored_header import colored_header
from streamlit_extras.let_it_rain import rain

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Khushal Patel | Portfolio",
    page_icon="💼",
    layout="wide"
)

# ------------------ LOTTIE ANIMATION LOADER ------------------
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ✅ Use reliable Lottie URLs
lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_cg3ev5f1.json")
lottie_ai = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_tll0j4bb.json")

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        scroll-behavior: smooth;
    }
    .stApp {
        background: linear-gradient(135deg, #0f172a, #1e1b4b, #3b0764);
        color: #F1F5F9;
    }
    .title {
        text-align: center;
        font-size: 2.8rem;
        font-weight: 700;
        color: #F9FAFB;
        margin-bottom: 10px;
    }
    .subtitle {
        text-align: center;
        font-size: 1.2rem;
        opacity: 0.85;
        margin-bottom: 40px;
    }
    .section {
        padding: 70px 0;
    }
    .skill-bar {
        background-color: #1e293b;
        border-radius: 20px;
        overflow: hidden;
        margin-bottom: 15px;
    }
    .skill-progress {
        height: 18px;
        border-radius: 20px;
        background: linear-gradient(90deg, #9333EA, #A855F7, #C084FC);
        transition: width 1.5s ease;
    }
    .contact-input {
        width: 100%;
        padding: 10px;
        border-radius: 8px;
        border: none;
        margin-bottom: 12px;
    }
    .btn {
        background: linear-gradient(90deg, #9333EA, #A855F7);
        color: white;
        padding: 10px 25px;
        border-radius: 10px;
        border: none;
        font-weight: 600;
        transition: 0.3s;
    }
    .btn:hover {
        transform: scale(1.05);
        background: linear-gradient(90deg, #A855F7, #C084FC);
    }
</style>
""", unsafe_allow_html=True)

# ------------------ HEADER ANIMATION ------------------
rain(emoji="💻", font_size=20, falling_speed=3, animation_length="infinite")

# ------------------ SIDEBAR NAVIGATION ------------------
st.sidebar.title("📂 Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "👤 About", "💻 Projects", "🧠 Skills", "📬 Contact"])

# ------------------ HOME SECTION ------------------
if page == "🏠 Home":
    st.markdown("<div class='section' id='home'>", unsafe_allow_html=True)
    st.markdown("<h1 class='title'>Hi, I'm Khushal Patel 👋</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Full Stack Developer | Data Scientist | AI Enthusiast</p>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        if lottie_coding:
            st_lottie(lottie_coding, height=320, key="coding")
        else:
            st.image("https://cdn-icons-png.flaticon.com/512/1055/1055646.png", width=250)
    with col2:
        st.write("""
        I specialize in **Data Science, Full Stack Development, and Artificial Intelligence**.  
        I'm passionate about building intelligent digital experiences that combine **creativity, data, and automation**.  
        """)
        st.markdown("[🌐 View my GitHub](https://github.com/KhushalPatel)")

# ------------------ ABOUT SECTION ------------------
elif page == "👤 About":
    st.markdown("<div class='section' id='about'>", unsafe_allow_html=True)
    colored_header(label="About Me", description=None, color_name="violet-70")
    st.write("""
    I’m currently pursuing **Integrated Artificial Intelligence** at **SAIT, Calgary (Canada)**.  
    Previously, I graduated in **Information Technology** from **Gujarat Technological University**  
    and have **1 year of experience** in software development.  

    My goal is to use AI and data-driven solutions to make technology smarter, more ethical, and more human-centered.
    """)

# ------------------ PROJECTS SECTION ------------------
elif page == "💻 Projects":
    st.markdown("<div class='section' id='projects'>", unsafe_allow_html=True)
    colored_header(label="Projects", description=None, color_name="violet-60")

    tab1, tab2 = st.tabs(["🏠 Ames Housing (Data Science)", "💻 Project Management System (Full Stack)"])

    with tab1:
        if lottie_ai:
            st_lottie(lottie_ai, height=200, key="ai")
        st.write("""
        **Ames Housing Price Prediction**
        - Built ML model to predict housing prices using advanced regression  
        - Feature engineering + Data visualization using Matplotlib and Seaborn  
        - Tools: Python, Pandas, Scikit-Learn  
        """)

    with tab2:
        st.write("""
        **Project Management System**
        - Full stack web app for task tracking and collaboration  
        - Built using **Ruby on Rails (backend)** and **React.js (frontend)**  
        - Integrated PostgreSQL and responsive UI components  
        """)

# ------------------ SKILLS SECTION ------------------
elif page == "🧠 Skills":
    st.markdown("<div class='section' id='skills'>", unsafe_allow_html=True)
    colored_header(label="Skills", description=None, color_name="violet-50")

    skills = {
        "Python": 95,
        "React.js": 85,
        "Ruby on Rails": 80,
        "Machine Learning": 90,
        "Data Visualization": 88,
        "AI / Deep Learning": 84,
    }

    for skill, level in skills.items():
        st.markdown(f"**{skill}**")
        st.markdown(f"<div class='skill-bar'><div class='skill-progress' style='width:{level}%;'></div></div>", unsafe_allow_html=True)

# ------------------ CONTACT SECTION ------------------
elif page == "📬 Contact":
    st.markdown("<div class='section' id='contact'>", unsafe_allow_html=True)
    colored_header(label="Contact Me", description=None, color_name="violet-40")

    contact_form = """
    <form action="https://formsubmit.co/YOUR_EMAIL_HERE" method="POST">
        <input type="text" name="name" placeholder="Your Name" required class="contact-input">
        <input type="email" name="email" placeholder="Your Email" required class="contact-input">
        <textarea name="message" placeholder="Your Message" required class="contact-input" style="height:120px"></textarea>
        <button type="submit" class="btn">Send Message</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

# ------------------ FOOTER ------------------
st.markdown("""
<hr style="border: 1px solid #6B21A8;">
<div style="text-align:center; font-size:0.9rem;">
    <p>© 2025 Khushal Patel | Built with ❤️ using Streamlit</p>
</div>
""", unsafe_allow_html=True)
