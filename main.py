import streamlit as st
from rembg import remove
from PIL import Image
st.markdown("<h1 style='text-align: center; color: grey;'>Add Keywords </h1>", unsafe_allow_html=True)

file_name=st.file_uploader(label="Upload Invoice",type=['png''jpeg','jpg'])
print(file_name)
if file_name is not None:
    input_img=Image.open(file_name)
    output=remove(input_img)
    co1,co2=st.columns(2)
    co1.title("original image")
    co1.image(input_img)
    co2.title("output Image")
    co2.image(output)

