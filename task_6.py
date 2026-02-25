import streamlit as st
import json
import requests

st.title("Platzi Store API")
response = requests.get('https://api.escuelajs.co/api/v1/products')
data_products = response.json()
for product in data_products:
    st.subheader(product['title'])
    st.write(product['description'])
    st.write(f"Price: ${product['price']}")
    st.write(f"Category: {product['category']['name']}")
    st.link_button(f"Source: View Product", product['images'][0])
    img_url = product['images'][0]
    if img_url:
        st.image(img_url, width=300)