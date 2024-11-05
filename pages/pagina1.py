import streamlit as st
import os 
from PIL import Image

# Caminho para a pasta de imagens
image_folder = "img/"

# Lista todas as imagens na pasta
image_files = [f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

# Título da aplicação
st.title("Selecionar Imagens")

# Selectbox para o usuário escolher a imagem
selected_image = st.sidebar.selectbox("Escolha uma imagem", image_files)

# Caminho completo da imagem selecionada
selected_image_path = os.path.join(image_folder, selected_image)

# Exibe a imagem selecionada
if selected_image:
    st.write("Imagem Selecionada:")
    image = Image.open(selected_image_path)
    st.image(image, caption=selected_image, use_column_width=True)
else:
    st.write("Nenhuma imagem selecionada.")