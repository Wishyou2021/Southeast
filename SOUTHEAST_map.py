import streamlit as st
import folium 
from PIL import Image  
from streamlit_folium import folium_static 
def BostonCeltics_map():
    st.header('主場:TD花園')
    TDGarden= folium.Map(location=[42.36622394101576, -71.06214665765047], zoom_start=16)
        # add marker for Liberty Bell
    tooltip = "TD花園"
    folium.Marker([42.36622394101576, -71.06214665765047], popup="TD花園", tooltip=tooltip
    ).add_to(TDGarden)
    folium_static(TDGarden)
    col1, col2 = st.columns(2)
    with col1:
        image = Image.open('Home/TD Garden.jpg')
        st.image(image)        
    with col2:        
        image1 = Image.open('Home/TD Garden1.jpg')
        st.image(image1)
    st.write('地址：100 Legends Way, Boston, MA 02114美國,觀眾席數：18624席')
  
def BrooklynNets_map():
    st.header('主場:巴克萊中心')
    BarclaysCenter= folium.Map(location=[40.682725423383374, -73.97526212020857], zoom_start=16)
        # add marker for Liberty Bell
    tooltip = "巴克萊中心"
    folium.Marker([40.682725423383374, -73.97526212020857], popup="巴克萊中心", tooltip=tooltip
    ).add_to(BarclaysCenter)
    folium_static(BarclaysCenter)
    col1, col2 = st.columns(2)
    with col1:          
        image = Image.open('Home/Barclays Center.jpg')       
        st.image(image)
    with col2:
        image1 =Image.open('Home/Barclays Center1.jpg')
        st.image(image1)
    st.write('地址：620 Atlantic Ave, Brooklyn, NY 11217美國,觀眾席數：17732席')
