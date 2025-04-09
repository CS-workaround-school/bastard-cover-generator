import streamlit as st
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

st.title("BASTARD Style Cover Generator")

uploaded_image = st.file_uploader("Upload a background image (jpg, png)", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
  img = Image.open(uploaded_image)
  st.image(img, caption="Uploaded Image", use_column_width=True)

custom_text = st.text_input("Type your custom word or phrase", value="bastard")

FONT_PATH = "fonts/CooperBlack.ttf"

def add_bastard_style_cover(img_path, text, font_path, output_path):

  img = Image.open(img_path).convert("RGB")
  img = img.resize((800, 800))

draw = ImageDraw.Draw(img)
font = ImageFont.truetype(font_path, 120)

text = text.upper()
text_width, text_height = draw.textsize(text, font=font)
x = (img.width - text_width) // 2
y = (img.height - text_height) // 2

draw.text((x, y), text, font=font, fill=(0, 255, 255))

return img

if uploaded_image and custom_text:
  img = Image.open(uploaded_image)

  final_img = add_bastard_text(img, custom_text, FONT_PATH)

  st.image(final_img, caption="Generated Cover", use_column_width=True)

  st.download_button("Download your cover", final_img, "your_cover.png", "img/png")
