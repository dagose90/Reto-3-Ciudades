import streamlit as st

#Configuración principal

st.set_page_config(page_title="Página web reto 3 Entornos de desarrollo", layout="wide")

st.title("Ciudades del mundo")

st.subheader("Imágenes y descripción")

#Menu de navegacion

col1, col2, col3 = st.columns(3)
with col1:
    st.image("https://encrypted-tbn0.gstatic.com/licensed-image?q=tbn:ANd9GcQzOzV1HqbADJ7xP3vEd_iXVIyAkqcgOcwi9SSj9oovV_9K189JQmcR6Kk8j0rnDn0OAG0bT7TCNxz4_xbq1OqHzw8&s=19",caption="Madrid", use_container_width=True)
    with st.expander("Descripción"):
        st.write("Capital de España, de gran interés cultural y donde juega el mejor equipo del mundo.")

with col2:
    st.image("https://encrypted-tbn0.gstatic.com/licensed-image?q=tbn:ANd9GcRmR8n7GRqua92dxmwMJZsIRjcQJNdWqBxSNTvW7ab-Zo-_h0n_Vg9Y25dFDjOESKPSQ-ad0y2lURaDx0MxWWtollM&s=19", caption="Sevilla", use_container_width=True)
    with st.expander("Descripción"):
        st.write("Si vas en verano prepárate para conocer el infierno en persona.")

with col3:
    st.image("https://encrypted-tbn0.gstatic.com/licensed-image?q=tbn:ANd9GcT2VT6JGiJ3SvEx0LYcvdX1QBWWL3hd-mA3kwzdaFf7Bx0tQukz_Mw984uuUu96BtecGT0sOdrFK5K_YbghYJUS5a8&s=19", caption="Barcelona", use_container_width=True)
    with st.expander("Descripción"):
        st.write("Ciudad Condal, segunda ciudad más poblada de España y lo peor que tiene es el FC Barcelona.")
