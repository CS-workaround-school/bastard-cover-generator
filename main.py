import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import os

st.title("Bastard Style Cover Generator")

custom_text = st.text_input("Type your custom word or phrase", value="bastard")

FONT_PATH = "CooperBlack.ttf/CooperBlack.ttf"

IMAGES_PATH = "sample.jpg/sample.jpg"

def add_bastard_text(background_img, text, font_path):

  img = background_img.convert("RGB")
  img = img.resize((800, 800))

  draw = ImageDraw.Draw(img)
  font = ImageFont.truetype(font_path, 120)

  text = text.upper()
  text_width, text_height = draw.textsize(text, font=font)
  x = (img.width - text_width) // 2
  y = (img.height - text_height) // 2

  draw.text((x, y), text, font=font, fill=(0, 255, 255))

  return img

if custom_text:
  
  image_file = os.path.join(IMAGES_PATH, "sample.jpg")

  if os.path.exists(image_file):

    background = Image.open(image_file)
else:
  st.error(f"No background image found in {IMAGES_PATH}. Please make sure sample.jpg exists.")
  
  final_img = add_bastard_text(background, custom_text, FONT_PATH)

  st.image(final_img, caption="Generated Cover", use_column_width=True)

  st.download_button("Download your cover", final_img, "your_cover.png", "img/png")
