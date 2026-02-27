import streamlit as st
import requests

# Page Config
st.set_page_config(page_title="🛒 Platzi Store", layout="wide")

st.title("🛍️ Platzi Store")
st.markdown("### Discover Amazing Products ✨")

# Search Bar
search = st.text_input("🔍 Search Product")

response = requests.get('https://api.escuelajs.co/api/v1/products')
data_products = response.json()

# Create 3 columns layout
cols = st.columns(3)

for index, product in enumerate(data_products):
    
    # Search Filter
    if search.lower() not in product['title'].lower():
        continue

    with cols[index % 3]:
        st.markdown("---")
        
        st.image(product['images'][0], width="stretch")

        st.subheader(product['title'])
        
        st.markdown(f"💲 **Price:** ${product['price']}")  
        st.markdown(f"🏷️ **Category:** {product['category']['name']}")
        
        st.write(product['description'][:100] + "...")
        
        st.link_button("🛍️ View Product", product['images'][0])
