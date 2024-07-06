import streamlit as st
from PIL import Image, ImageFont, ImageDraw

def text_on_image(image, text, font_size, color):
    try:
        img = Image.open(image)
        font = ImageFont.truetype('arial.ttf', font_size)
        draw = ImageDraw.Draw(img)

        iw, ih = img.size
         # Calculate the size of the text
        bbox = draw.textbbox((0, 0), text, font=font)
        fw, fh = bbox[2] - bbox[0], bbox[3] - bbox[1]

        draw.text(
            (iw - fw)/2, (ih-fh)/2,
            text,
            font=font,
            fill=color
        )

        img.save('D:/OneDrive/Imagens/Meme para chat/last_image.jpeg')
        return 'last_image.jpeg'
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None


image = st.file_uploader('Uma imagem', type=['jpg','jpeg'])
text = st.text_input('Sua marca dágua')
color = st.selectbox(
    'Cor da sua marca', ['black', 'white', 'red', 'green']
)
font_size = st.number_input('Tamanho da fonte', min_value=50)

if image:
    result = st.button(
        'Aplicar',
        type='primary',
        on_click= text_on_image,
        args=(image, text, font_size, color)
    )
    if result:
        st.image('last_image.jpeg')
else:
    st.warning('Ainda não temos imagem!')
    