import streamlit as st
import requests

# Page Config
st.set_page_config(page_title="🛒 Platzi Store", layout="wide")

st.title("🛍️ Platzi Store")
st.markdown("### Discover Amazing Products ✨")

# Search Bar
search = st.text_input("🔍 Search Product")

response = requests.get("https://fakestoreapi.com/products")
data_products = response.json()

# Create 3 columns layout
cols = st.columns(3)

for index, product in enumerate(data_products):

    # Search Filter
    if search and search.lower() not in product['title'].lower():
        continue

    with cols[index % 3]:

        st.markdown("---")

        # SAFE IMAGE DISPLAY
        img = product.get("image")

        if img:
            st.image(img, use_column_width=True)
        else:
            st.write("No image available")

        st.subheader(product['title'])

        st.markdown(f"💲 **Price:** ${product['price']}")

        # CATEGORY FIX
        st.markdown(f"🏷️ **Category:** {product['category']}")

        st.write(product['description'][:100] + "...")

        # Product Link (using image as placeholder)
        st.link_button("🛍️ View Product", product['image'])
