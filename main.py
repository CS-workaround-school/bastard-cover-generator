from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

def add_bastard_style_cover(img_path, text, font_path, output_path):

  img = Image.open(img_path).convert("RGB")
  img = img.resize((800, 800))

draw = ImageDraw.Draw(img)
font = ImageFont.truetype(font_path, 120)

text = text.upper()
text_width, text_height = draw.textsize(text, font=font)
x = (img.width - text_width) // 2
y = (img.height - text_height) // 2

draw.text((x, y), text, font=font, fill=(0, 255, 255)

          img.save(output_path)
          print(f"cover saved to {output_path}"

if __name__ == "__main__":
                user_text = input("type your bastard-style word or phrase: ")

img_path = "images/sample.jpg"
font_path = "fonts/CooperBlack.ttf"
output_path = "output/your_cover.png"

if not os.path.exists(img_path):
  print ("error: background image not found")
elif not os.path.exists(font_path)
else:
  add_bastard_text(img_path, user_text, font_path, output_path)
