import os
from openai import OpenAI
from dotenv import load_dotenv 
from IPython.display import Image 
import streamlit as st 
from StoryMethods import StoryMethods as sm
from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
import base64

client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)




def main():
    
    st.title('Bed Time Story')

    user_prompt = st.text_area('What is the title of your story')
    if st.button('Generate Story'):

        story =sm.story_ai(user_prompt,client)
        design =sm.design_ai(story,client)
        imgae_url =sm.cover_ai(design,client)
        
        st.image(imgae_url, caption='Generated Cover Image', use_column_width=True)

        st.write('Generated Image Prompt:')
        st.write(design)

        st.divider()

        st.write('Generated Story:')
        st.write(story)

      # Convert the generated story to speech
        tts = gTTS(text=story, lang='en')
        audio_bytes = BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)

        # Create a play button to play the generated speech
        st.audio(audio_bytes, format='audio/wav')



if __name__ == "__main__":
    main()


