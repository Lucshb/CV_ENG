from pathlib import Path

import streamlit as st
#import my_custom_theme
from PIL import Image
from streamlit_extras.app_logo import add_logo
from streamlit_lottie import st_lottie
import base64
import requests

import time

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital Resume | Lucas Henrique de Barros"
PAGE_ICON = ":wave:"
NAME = "Lucas Henrique de Barros"
DESCRIPTION = """
❤️ Passionate about technology and business, I have experience in both the private and public sectors, always engaging with clients, patrons, and users in general.

🎓 I hold a Bachelor's degree in Law (UNIMEP), with a specialization in LGPD, and I am currently pursuing a degree in Data Science.

🥼 Throughout my undergraduate and specialization studies, I gained knowledge and hands-on experience in implementing LGPD in Brazil, Excel spreadsheet management, database maintenance, and an introduction to the world of data.

🎲 I currently work as a Business Intelligence Analyst at Transportadora Garbuio, dealing with data extraction, manipulation, and visualization. Each day brings new challenges, insights, and learning experiences.

💻 I am proficient in Excel, SQL, MySQL, PostgreSQL, and Power BI/Qlik View for data analysis and visualization. Currently, I am deepening my knowledge in Python.
"""
EMAIL = "barroslucash@gmail.com"
SOCIAL_MEDIA = {
    "💻 LinkedIn": "https://www.linkedin.com/in/lucas-h-barros/",
}


st.set_page_config(layout= 'wide', page_title=PAGE_TITLE ,page_icon=":wave:")

#my_custom_theme.apply_custom_theme()

add_logo("logo.png")

def load_lottierur1(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_hello = load_lottierur1("https://lottie.host/0c84e0de-6029-46f0-a582-b6429cfc97c4/e5VWao3q69.json")



def mensagem_sucesso():
    sucesso = st.success('Arquivo baixado com sucesso!', icon = "✅")
    #time.sleep(1)
    sucesso.empty()

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("logo.png")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://wallpapercave.com/wp/dMCG3T2.jpg");
background-size: 600px 400px;
background-position: bottom right;
background-repeat: no-repeat;
background-attachment: local;
image-rendering: pixelated;
image-rendering: -webkit-optimize-contrast;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

#st.markdown(page_bg_img, unsafe_allow_html=True)


resume_file = "Lucas Henrique de Barros.pdf"
css_file = "styles/main.css"
profile_pic = "logo.png"


st.markdown(
    """
    <style>
    body {
        background-color: #3e36b5; /* Cor de fundo desejada */
    }
    </style>
    """,
    unsafe_allow_html=True,
)


with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
#profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---

col1, col2= st.columns(2, gap="medium")
with col1:
    #add_logo('logo.png')
    st.title(NAME)
    st.write('\n')
    st.write(DESCRIPTION)
    st.write('\n')
with col2:
    imagem_local = Image.open("Picture4.png")
    st.image(imagem_local, width= None)
with col1:
    st.download_button(
        label=" 📄 Resume Download",
        data=PDFbyte,
        file_name=resume_file,
        mime="application/octet-stream",
        on_click=mensagem_sucesso
    )

with col1:
    st.write('\n')
    for linkedin, link in SOCIAL_MEDIA.items():
        st.write(f"[{linkedin}]({link})")
    st.write("📫", "barroslucash@gmail.com") 
    st.write("📞", "(19) 99263-0596")

st.write('\n')

st.write("---")
st.subheader("Soft Skills")
st.write(
    """
- ✔️ Diligent and quick learner with technologies
- ✔️ Efficient work, managing resources effectively and solving problems efficiently
- ✔️ Passionate about the world of data and always eager to learn
- ✔️ Excellence in teamwork and analytical profile for assigned tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 📊 Data Visualization: Power BI, Qlik Sense, Google Looker, Python (Streamlit, Plotly, Matplotlib)
- 👩‍💻 Programming: Python (Numpy, Pandas), R Language, HTML, and CSS.
- 🗄️ Databases: SQL, MySQL, PostgreSQL.
"""
)


# --- WORK HISTORY ---
st.write('\n')

st.write("---")
st.subheader("Experiências: ")

st.write('\n')
st.write('\n')

col1, col2 = st.columns(2)

# --- JOB 1
with col1:
    st.write("📈", "**BI Analyst  | Transportadora Garbuio**")
    st.write("05/2023 - Present")
    st.write(
    """
- BI (Data View):
\n
- * BI Project Management
- * Development of medium/high complexity dashboards with strategic indicators for generating insights
- * Responsible for liaising with managers to understand business rules and validate data.
- * Metrics in M and Dax languages for data analysis.
- * HTML/CSS for creating animations usable in dashboards
- * Maintenance of operational dashboards in the company.
- * Management and release of accesses via Sharepoint
- * Generate specific reports in Excel
- * Workspace management, deployment, and update
- * Dataset management
\n
- Data Engineering:
\n
- * Queries and manipulation in SQL Server, MySQL, and PostgreSQL databases
- * Configuration and management of the gateway
- * Creation, maintenance, and management of data flows.
- * Automation of data flow with Power Automate
- * Extraction of information via the database and validation of Totvs/Protheus
"""
)

# --- JOB 2
with col1:
    st.write('\n')
    st.write("📈", "**BI Assistant | Transportadora Garbuio**")
    st.write("02/2023 - 04/2023")
    st.write(
    """
- Development of dashboards with strategic indicators for generating insights
- Maintenance of operational dashboards in the company
- Queries and manipulation in SQL Server databases
- Extraction of information via the database and validation of Totvs/Protheus
"""
)

# --- JOB 2.5
with col1:
    st.write('\n')
    st.write("📈", "**Free Lancer**")
    st.write("07/2021 - Atual")
    st.write(
    """
- Data Project Management
- Consultation on Business Intelligence solutions
- Creation of strategic and customized dashboards
- Problem-solving in data management (DW, ERP suggestions, Database optimization)
- Maintenance of ongoing dashboards
"""
)



# --- JOB 3
with col2:
    st.write('\n')
    st.write("👨🏽‍💼", "**Public Defender's Assistant | Defensoria Pública do Estado de São Paulo**")
    st.write("04/2022 - 02/2023")
    st.write(
    """
- Numerous in-person and online consultations
- Legal-administrative routine
- Analysis and explanation of complex situations
- Document collection
- Data entry in spreadsheets and other administrative activities
- Control of internal deadlines and compliance with them
- Preparation and creation of reports
"""
)


# --- JOB 4
with col2:
    st.write('\n')
    st.write("👨🏽‍💼", "**Legal Intern | Regional Labor Court 15th Region - Campinas/SP**")
    st.write("06/2019 - 06/2021")
    st.write(
    """
- Numerous in-person and online consultations
- Legal-administrative routine
- Analysis and explanation of complex situations
- Document collection
- Data entry in spreadsheets and other administrative activities
- Control of internal deadlines and compliance with them
- Preparation and creation of reports

"""
)
    
# --- JOB 5
with col2:
    st.write('\n')
    st.write("👨🏽‍💼", "**Legal Assistant | Dr. Vinicius Tomé & Advogados**")
    st.write("09/2018 - 04/2019")
    st.write(
    """
- Legal-administrative routine
- In-person and online customer service
- Document collection
- Discount of titles
- Negotiation with clients and partners
- Drafting, negotiation, and review of contracts
- Fast typing of files and information
- Formulation and monitoring of Excel spreadsheets on clients, deadlines, and finances
- Information consultation and handling
- File organization

"""
)



# --- Projects & Accomplishments ---


PROJECTS_PY = {
"📈 Análise de Equipe de Vendas": "https://sales-project.onrender.com",
"📈 Análise dos preços de gasolina": "https://gaspriceapp.onrender.com",
"📈 Análise Simples de receita da empresa": "https://projeto-dashvendas-python.streamlit.app",
"📈 Análise de Dados da Fifa": "https://fifaproject.streamlit.app"
}


PROJECTS_BI = {
"📈 Dashboard Simples de Faturamento (Google Looker/Data Studio)": "https://lookerstudio.google.com/reporting/3959707c-c28d-4946-b667-d1567753ebc0",
"📈 Dashboard Simples de Perfomance de Campanha (Google Looker/Data Studio)": "https://lookerstudio.google.com/reporting/4157f723-d529-49c9-9baa-732865224df2",
"📈 Dashboard de Vendas (Power BI) ": "https://app.powerbi.com/view?r=eyJrIjoiYzQ5YTgzYWMtYjJkZi00N2U3LWIwNTYtNGYwOWI4NzIxYWY1IiwidCI6ImNjMmE5NWVhLTMzNWMtNDQzYi04NDQzLWU5YWQzM2ZmOWUwNCJ9 "
}

st.write('\n')
st.write("---")
st.subheader("Portfolio Projects")
st.write('\n')

st.write("Python Projects (Web Apps):")

for projeto_py, linker in PROJECTS_PY.items():
    st.write(f"[{projeto_py}]({linker})")

st.write('\n')
st.write("BI Projects:")
st.write('\n')

for projeto_bi, linked in PROJECTS_BI.items():
    st.write(f"[{projeto_bi}]({linked})")
