import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
Esta pagina es parte de los servicios de BuscoCampo, su informacion no sera compartida con terceros
Sigannos en TW <https://twitter.com/AgRemotegirl>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://search.brave.com/images?q=logos&img=113"
st.sidebar.image(logo)

# Customize page title
st.title("reportes BuscoCampo")

st.markdown(
    """
    describir o presentar algo 
    """
)

st.header("Instrucciones")

markdown = """
1. 
2.
3.

"""

st.markdown(markdown)

m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)


