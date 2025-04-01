import streamlit as st

from forms.contact import contact_form


@st.experimental_dialog("Contact Me")
def show_contact_form():
    contact_form()


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/IMG.png", width=230)

with col2:
    st.title("Abhiraj Gupta", anchor=False)
    st.write(
        "Student Coordinator @Training and Placement Cell MMMMUT | B.tech EE'26"
    )
    if st.button("✉️ Contact Me"):
        show_contact_form()




# --- SKILLS ---
st.write("\n")
st.subheader("Skills", anchor=False)
st.write(
    """
- Technical: C, C++, HTML, CSS, Bootstrap, JavaScript, MATLAB, Microsoft Office, Adobe Photoshop, Canva.
- Non-Technical: Problem solving, Adaptability, Teamwork, Time Management, Critical Thinking, Creativity, Active
Listening.
- Curriculum: Power System, Power Electronics, MATLAB-Simulink, Electrical Machines.
- Interests: Data Structures & Algorithm, Problem Solving, Web development (MERN).
    """
)
