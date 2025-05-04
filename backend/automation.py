# backend/automation.py
from script_generator import generate_anchor_script
from text_to_speech import generate_voiceover
from generate_video import generate_avatar_video

if _name_ == "_main_":
    print(">> Generating anchor script...")
    generate_anchor_script()
    print(">> Generating voiceover from script...")
    generate_voiceover()
    print(">> Creating avatar video...")
    generate_avatar_video()
    print(">> Pipeline completed. Video saved as anchor.mp4")