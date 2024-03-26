import os
from openai import OpenAI
from dotenv import load_dotenv 
from IPython.display import Image 
import streamlit as st 
from StoryMethods import StoryMethods as sm
from gtts import gTTS
from io import BytesIO


client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

# Initialize the OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Function to convert text to speech
def text_to_speech(text):
    # Convert the text to speech using gTTS
    tts = gTTS(text, lang='en')

    # Create an in-memory file-like object to store the audio
    sound_file = BytesIO()

    # Write the speech to the in-memory file
    tts.write_to_fp(sound_file)

    # Return the audio file
    return sound_file

def main():
    
    st.title('BedTime Story')

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

        # Add a button to convert the generated story text to speech
        if st.button('Convert Story to Speech'):
            # Call the text_to_speech function with the generated story text
            audio_file = text_to_speech(story)
            # Play the generated speech in the Streamlit app
            st.audio(audio_file, format='audio/wav')


if __name__ == "__main__":
    main()


