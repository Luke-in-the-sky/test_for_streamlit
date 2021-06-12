import streamlit as st
from pathlib import Path
from fastai.text.all import *
from helpers import download_file_from_google_drive


st.title('Classify text')


option = st.sidebar.selectbox('What type of event?', ['flood', 'drought'])
input_text = st.sidebar.text_input('Enter some text')

if option == 'drought':
  "You selected drought, but it's not available yet"
else:
  'text is:', input_text

# download the model
@st.cache
def download_model(gdrive_id: str, save_dest: Path):
    """
    gdrive_id: the id fo the file (eg from the sharable link)
    save_dest: path (dir/filename.extension) where to store the downloaded file
    """
    save_dest.parent.mkdir(exist_ok=True, parents=True)
    if not save_dest.exists():
        with st.spinner("Downloading model... this may take awhile! \n Don't stop it!"):
            from helpers import download_file_from_google_drive
            download_file_from_google_drive(gdrive_id, save_dest)

MODELS_DIR = Path('/downloads')
flood_model = dict(
    local_path=MODELS_DIR/'20210604_dummy_test.pkl',
    gdrive_id='1E9xrqSo8QGk7zKYB3xkFKjN88sdcGk_U',
)
download_model(flood_model['gdrive_id'], flood_model['local_path'])

if input_text:
  learn = load_learner(flood_model['local_path'])
  'prediction is:', learn.predict(input_text)