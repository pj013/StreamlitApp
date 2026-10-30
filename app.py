import os
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Eufronio A. Aaron III | Portfolio",
    page_icon="👋",
    layout="wide",
)
with open("style.css", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------- Session state ----------
if "feedback_count" not in st.session_state:
    st.session_state.feedback_count = 0

# ---------- Sidebar ----------
with st.sidebar:
    st.header("Eufronio A. Aaron III")
    st.caption("BSIT | 4th Year | G01")
    page_view = st.radio("View mode", ["Full portfolio", "Projects only"])
    show_skills = st.checkbox("Show skills section", value=True)
    st.divider()
    st.write("Messages sent this session:", st.session_state.feedback_count)

# ---------- Header ----------
st.title("Eufronio A. Aaron III")
st.markdown("**BSIT | 4th Year**")

# ---------- About ----------
if page_view == "Full portfolio":
    st.header("About Me")
    col1, col2 = st.columns([1, 3],)
    with col1:
        st.write("")
        st.write("")
        if os.path.exists("profile.jpg"):
            st.image("profile.jpg", caption="Eufronio A. Aaron III", use_container_width="stretch")
        else:
            st.info("📷 Photo placeholder (add profile.jpg next to app.py)")
    with col2:
        st.write("")
        st.write("")
        st.write("I am a 25-year-old 4th-year BSIT student from Minglanilla passionate about software development and tech innovation—notably serving on the St. Cecilia's College weather balloon flight team. In my free time, I enjoy playing pickleball, cooking, watching *Spider-Man*, and playing *The Witcher 3*.")
        m1, m2 = st.columns(2)
        m1.metric("Projects", 3)
        m2.metric("Skills listed", 5)

    # ---------- Autobiography ----------
    st.header("Autobiography")
    tab1, tab2, tab3 = st.tabs(["Background", "Education", "Interests"])
    with tab1:
        st.write(
            """
            Born in Laray, Inayawan, Cebu City in 2001, I later moved to Lipata, Minglanilla in 2011, which has been my home ever since. 
            Growing up in a large, closely-knit family instilled in me strong family values and a solid support system. 
            Above all, what has truly shaped me into who I am today is my constant drive and willingness to self-improve, adapt, and learn from every challenge I face.
            """
        )
        st.write(
            """
            In 8th grade, I became active in school for the first time. My friends and I joined the Science Club, where we spent the year working on and studying our weather balloon project. Thankfully, the school supported us financially, making the experience possible. It was fun and memorable. We were even featured on TV and invited for a radio interview. Those were good times, and I still look back on them fondly.

            Right now, I’m working on myself to get back to that version of me—the one who was active, motivated, and always willing to try new things. This time, I want to become even better than I was before. I know I can’t bring back those exact moments, but I can bring back the mindset and drive I had then and continue growing from there.
            """
        )
    with tab2:
        st.write(
            """
        ### 🎓 Educational Attainment
        
        * **College (Present):** Bachelor of Science in Information Technology (BSIT - 4th Year) | *Cebu Institute of Technology – University*
        * **Senior High School:** *Cebu Institute of Technology – University*
        * **Junior High School:** *St. Cecilia's College – Cebu*
        * **Elementary School:** *Lipata Central Elementary School*
        
        ---
        
        ### 🚀 Key Accomplishments
        * **Weather Balloon Flight Team Member:** Participated in the high-altitude weather balloon launch at *St. Cecilia's College*, gaining hands-on experience with telemetry, tracking systems, and atmospheric data collection.
        """
        )
    with tab3:
        st.write(
            """
        ### 🏀 Hobbies & Activities
        * **Pickleball:** Staying active and enjoying friendly competitive matches on the court.
        * **Cooking:** Experimenting with new recipes and preparing meals.
        * **Video Games:** Immersing myself in open-world storytelling and challenging game mechanics.
        * **Movies & Cinema:** Unwinding with action-packed and story-driven films.

        ---

        ### ⭐ Personal Favorites
        * **Favorite Video Game:** *The Witcher 3: Wild Hunt*
        * **Favorite Movie:** *Spider-Man*
        """
        )

    st.subheader("Milestones")
    milestones = pd.DataFrame(
        {
            "Year": [2016, 2023, 2025],
            "Milestone": [
                "St. Cecilia's College Weather Balloon Launch Team", 
                "Working on Real IT Industry Project",
                "Joined my first 2 Hackathons"]
        }
    )
    st.table(milestones)

    # ---------- Skills ----------
    if show_skills:
        st.header("Skills")
        skills = pd.DataFrame(
            {
                "Skill": ["Python", "Communication", "Teamwork", "SQL", "Design"],
                "Level (1-10)": [7, 8, 9, 5, 6],  
            }
        )
        c1, c2 = st.columns(2)
        with c1:
            st.dataframe(skills, use_container_width=True, hide_index=True)
        with c2:
            st.bar_chart(skills.set_index("Skill"))

        chosen = st.multiselect(
            "Pick skills to highlight", skills["Skill"], default=["Python"]
        )
        min_level = st.slider("Minimum level", 1, 10, 5)
        filtered = skills[
            skills["Skill"].isin(chosen) & (skills["Level (1-10)"] >= min_level)
        ]
        st.write("Matching skills:", ", ".join(filtered["Skill"]) or "None")

# ---------- Projects ----------
st.header("Projects")
projects = {
    "Online Gambling App":{"role": "Frontend Developer", "tools": "React, Java, HTML, CSS", "outcome": "I cant give the link because it is a private project"},
    "InternTrack App": {"role": "Frontend Developer, Backend Developer", "tools": "HTML, Python", "outcome": "https://github.com/aceuda/CSIT327-G2-InternTrack.git"},
    "Modular-Monolith-Integration-with-a-React-Frontend": {"role": "Frontend Developer, Backend Developer", "tools": "React, Java, HTML, CSS", "outcome": "https://github.com/pj013/Modular-Monolith-Integration-with-a-React-Frontend.git"},
}
selected = st.selectbox("Choose a project", list(projects.keys()))
p = projects[selected]
st.subheader(selected)
st.write(f"**Role:** {p['role']}")
st.write(f"**Tools used:** {p['tools']}")
st.write(f"**Outcome / link:** {p['outcome']}")

with st.expander("See all projects at a glance"):
    st.table(pd.DataFrame(projects).T)

# ---------- Contact / feedback ----------
st.header("Contact / Feedback")
st.link_button("Visit my GitHub profile", "https://github.com/pj013")
with st.form("contact_form", clear_on_submit=True):
    name = st.text_input("Your name")
    message = st.text_area("Your message")
    submitted = st.form_submit_button("Send")

if submitted:
    if name and message:
        st.session_state.feedback_count += 1
        st.success(f"Thanks, {name}! Your message was received.")
        st.balloons()
    else:
        st.warning("Please fill in both your name and message.")

# ---------- Download ----------
st.download_button(
    "Download my bio (.txt)",
    data="Eufronio A. Aaron III\nBSIT, 4\nI am a 25-year-old 4th-year BSIT student from Minglanilla passionate about software development and tech innovation—notably serving on the St. Cecilia's College weather balloon flight team. In my free time, I enjoy playing pickleball, cooking, watching *Spider-Man*, and playing *The Witcher 3*",
    file_name="bio.txt",
)

st.divider()
st.caption("Eufronio A. Aaron III | G01")