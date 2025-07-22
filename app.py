import streamlit as st
from main import download_corpus, read_corpus, generate_script
from fpdf import FPDF
import base64

# Theme styling
st.set_page_config(page_title="Sitcom Script Generator", page_icon="🎬", layout="centered")
# Easter egg scenes
EASTER_EGGS = {
    "The One with the Unplugged Wi-Fi": "Write a scene where we have six characters (John, Doe, Callistus,Collins,Ian,Kate) are panicking because the Wi-Fi is down and none of them knows how to fix it.",
    "The One with the Espresso Machine": "Callistus buys a fancy espresso machine that no one knows how to use, but they’re all pretending they do.",
    "The One with the Midnight Burrito": "Collins and Ian sneak into the kitchen at midnight and get caught fighting over the last burrito."
}

def enhance_prompt(user_input, character_pair, season):
    refined_prompt = f"Write a 15-line witty sitcom scene between {character_pair}."

    if season:
        refined_prompt += f" Make it feel inspired by {season}."
    
    refined_prompt += f" The scene involves: {user_input}. Use clever banter, visual beats and actions, build comedic tension, and end on a punchline."
    
    return refined_prompt

# Download corpus once
@st.cache_resource
def load_data():
    download_corpus()
    return read_corpus()

corpus_text = load_data()

# App layout
st.title("Sitcom Script Generator")
st.write("Generate Friends-style sitcom scenes with custom prompts!")

# Easter egg dropdown
easter_choice = st.selectbox("🌟 Try a Sample Prompt? (Optional)", ["None"] + list(EASTER_EGGS.keys()))
# # Character dropdown
# # Character input mode
# char_mode = st.radio("🎭 Choose Character Mode", ["Single Character", "Character Pair", "All Six"])

# if char_mode == "Single Character":
#     selected_character = st.selectbox("🧍 Select Character", [
#         "Joey", "Chandler", "Ross", "Rachel", "Phoebe", "Monica"
#     ])
#     characters_selected = selected_character

# elif char_mode == "Character Pair":
#     selected_pair = st.selectbox("👫 Choose Character Pair", [
#         "Joey & Chandler", "Ross & Rachel", "Phoebe & Monica",
#         "Monica & Chandler", "Joey & Rachel"
#     ])
#     characters_selected = selected_pair

# else:
#    characters_selected = "All Six (Joey, Chandler, Ross, Rachel, Phoebe, Monica)"
characters_selected = "the Friends characters"


# Optional season/episode input
season = st.text_input("📺 (Optional) Season or Episode Reference", placeholder="e.g., Season 3, Episode 5")

# Prompt input
# scene_prompt = st.text_area(" Describe Your Scene", placeholder="e.g., They’re stuck in an elevator during a blackout.")



scene_prompt = ""
if easter_choice != "None":
    scene_prompt = EASTER_EGGS[easter_choice]
    st.info(f"✨ Easter Egg Prompt Loaded: {scene_prompt}")
else:
    scene_prompt = st.text_area("Describe Your Scene", placeholder="e.g., They’re stuck in an elevator during a blackout.")
optimize = st.checkbox("✨ Optimize my prompt for better results")

def create_pdf(text, filename="sitcom_script.pdf"):
    font_path = "C:\\Users\\Kate Naisylian\Desktop\\Sitcom gf\\dejavu-fonts-ttf-2.37\\ttf\\DejaVuSans.ttf"
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font("DejaVu", "", font_path, uni=True)
    pdf.set_font("DejaVu", "", 12)
    
    # Break lines to avoid overflow
    for line in text.split("\n"):
        pdf.multi_cell(0, 10, line)
    
    pdf.output(filename)
    return filename

# Generate script
if st.button("🎬 Generate Script"):
    if optimize:
        prompt = enhance_prompt(scene_prompt, characters_selected, season)
    else:
        prompt = f"Write a 20 or more-line witty sitcom script between {characters_selected}."
        if season:
            prompt += f" It should feel like it’s inspired by {season}."
        prompt += f" Scene prompt: {scene_prompt}"

    result = generate_script(prompt)
    st.subheader("📝 Your Generated Script")
    st.write(result)


 # PDF export
    pdf_path = create_pdf(result)
    with open(pdf_path, "rb") as f:
         pdf_data = f.read()
         b64 = base64.b64encode(pdf_data).decode("utf-8")
         href = f'<a href="data:application/pdf;base64,{b64}" download="sitcom_script.pdf">📄 Download Script as PDF</a>'
         st.markdown(href, unsafe_allow_html=True)