import streamlit as st
import folium 
from PIL import Image  
from streamlit_folium import folium_static 
def AtlantaHawks_map():
    st.header('主場:州立農業球館')
    StateFarmArena= folium.Map(location=[33.75737827997708, -84.39633513151331], zoom_start=16)
        # add marker for Liberty Bell
    tooltip = "州立農業球館"
    folium.Marker([33.75737827997708, -84.39633513151331], popup="州立農業球館", tooltip=tooltip
    ).add_to(StateFarmArena)
    folium_static(StateFarmArena)
    col1, col2 = st.columns(2)
    with col1:
        image = Image.open('State Farm Arena.jpeg')
        st.image(image)        
    with col2:        
        image1 = Image.open('State Farm Arena1.jpeg')
        st.image(image1)
    st.write('地址：1 State Farm Dr, Atlanta, GA 30303美國,觀眾席數：18,371席')
  
def CharlotteHornets_map():
    st.header('主場:光譜中心')
    SpectrumCenter= folium.Map(location=[35.22528408738218, -80.83934793137779], zoom_start=16)
        # add marker for Liberty Bell
    tooltip = "光譜中心"
    folium.Marker([35.22528408738218, -80.83934793137779], popup="光譜中心", tooltip=tooltip
    ).add_to(SpectrumCenter)
    folium_static(SpectrumCenter)
    col1, col2 = st.columns(2)
    with col1:          
        image = Image.open('Spectrum Center.jpeg')       
        st.image(image)
    with col2:
        image1 =Image.open('Spectrum Center1.jpeg')
        st.image(image1)
    st.write('地址：333 E Trade St, Charlotte, NC 28202美國,觀眾席數：20,200席')
def MiamiHeat_map():
    st.header('主場:FTX球館')
    FTXArena= folium.Map(location=[25.781565618522425, -80.18702264697642], zoom_start=16)
        # add marker for Liberty Bell
    tooltip = "FTX球館"
    folium.Marker([25.781565618522425, -80.18702264697642], popup="FTX球館", tooltip=tooltip
    ).add_to(FTXArena)
    folium_static(FTXArena)
    col1, col2 = st.columns(2)
    with col1:          
        image = Image.open('FTX Arena.jpeg')       
        st.image(image)
    with col2:
        image1 =Image.open('FTX Arena1.jpg')
        st.image(image1)
    st.write('地址：601 Biscayne Blvd, Miami, FL 33132美國,觀眾席數：19,600席')
def OrlandoMagic_map():
    st.header('主場:安麗中心')
    AmwayCenter= folium.Map(location=[28.539343909610295, -81.38387496040187], zoom_start=16)
        # add marker for Liberty Bell
    tooltip = "安麗中心"
    folium.Marker([28.539343909610295, -81.38387496040187], popup="安麗中心", tooltip=tooltip
    ).add_to(AmwayCenter)
    folium_static(AmwayCenter)
    col1, col2 = st.columns(2)
    with col1:          
        image = Image.open('Amway Center.jpeg')       
        st.image(image)
    with col2:
        image1 =Image.open('Amway Center1.jpeg')
        st.image(image1)
    st.write('地址：400 W Church St Suite 200, Orlando, FL 32801美國,觀眾席數：18,846席')
def WashingtonWizards_map():
    st.header('主場:第一資本競技館')
    CapitalOneArena= folium.Map(location=[38.89830942692672, -77.02088898904876], zoom_start=16)
        # add marker for Liberty Bell
    tooltip = "第一資本競技館"
    folium.Marker([38.89830942692672, -77.02088898904876], popup="第一資本競技館", tooltip=tooltip
    ).add_to(CapitalOneArena)
    folium_static(CapitalOneArena)
    col1, col2 = st.columns(2)
    with col1:          
        image = Image.open('Capital One Arena.jpeg')       
        st.image(image)
    with col2:
        image1 =Image.open('Capital One Arena1.jpeg')
        st.image(image1)
    st.write('地址：601 F St NW, Washington, DC 20004美國,觀眾席數：20,356席')
