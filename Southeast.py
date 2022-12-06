import streamlit as st  
import SOUTHEAST_map
st.title('NBA數據查詢系統')
st.sidebar.header('選擇球隊及數據')
option = st.sidebar.selectbox( '選擇分組？', ['ATLANTIC', '中央組', 'SOUTHEAST', '西北組','太平洋組','西南組'])
if option=='SOUTHEAST':
  teams=st.sidebar.selectbox( '選擇球隊？', ['Atlanta Hawks', 'Charlotte Hornets', 'Miami Heat', 'Orlando Magic','Washington Wizards'])
  if teams=='Atlanta Hawks':
    SOUTHEAST.AtlantaHawks()
    SOUTHEAST_map.AtlantaHawks_map()
  if teams=='Charlotte Hornets':
    SOUTHEAST.CharlotteHornets()
    SOUTHEAST_map.CharlotteHornets_map()
  if teams=='Miami Heat':
    SOUTHEAST.MiamiHeat()
    SOUTHEAST_map.MiamiHeat_map()
  if teams=='Orlando Magic':
    SOUTHEAST.OrlandoMagic()
    SOUTHEAST_map.OrlandoMagic_map()
  if teams=='Washington Wizards':
    SOUTHEAST.WashingtonWizards()
    SOUTHEAST_map.WashingtonWizards_map()
