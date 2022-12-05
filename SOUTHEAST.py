import streamlit as st  
from PIL import Image  
def AtlantaHawks():
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('Atlanta_Hawks.png')
    st.image(image) 
  with col2:
     st.title('Atlanta Hawks')
     st.subheader('老闆:Tony Ressler')
     st.subheader('GM:Landry Fields')
     st.subheader('總教練:Nate McMillan')     
  st.write('水牛城野牛（1946年）三城黑鷹（1946年-1951年）密爾瓦基老鷹（1951年-1955年）聖路易斯老鷹（1955年-1968年）亞特蘭大老鷹（1968年-至今）') 
  st.write('亞特蘭大老鷹的英文隊名為Atlanta Hawks，老鷹隊之名象徵著速度和進攻，球隊成立於1946年，在1949年加入NBA，是NBA的元老之一。目前所在城市是美國喬治亞州亞特蘭大市(Atlanta, Georgia)，主場為飛利浦球場(Philips Arena)。球隊最初名為「三城黑鷹隊」，1951年主場遷移到密爾瓦基市，改名「密爾瓦基鷹隊」，直到1968年主場移到亞特蘭大後才改成現在的亞特蘭大老鷹隊。')
  col1, col2= st.columns(2)
  col1.metric("聯盟冠軍🏆", "4  次")
  col2.metric("分組冠軍🏆", "1  次")   
def BrooklynNets():
  st.header('Brooklyn Nets')
  image = Image.open('teams logo/BrooklynNets.png')
  st.image(image) 
  st.write('Brooklyn Nets(1946年-至今)')
  col1, col2= st.columns(2)
  col1.metric("聯盟冠軍🏆", "22  次")
  col2.metric("分組冠軍🏆", "32  次")
  st.write('　布魯克林籃網隊的英文隊名為Brooklyn Nets，球隊成立於1967年，目前所在城市是美國紐約州布魯克林(Brooklyn, New York)，主場為大陸航空中心體育館(Prudential Center)。球隊原名紐澤西籃網隊（New Jersey Nets），2012年球隊遷至紐約布魯克林，4月底更名為「布魯克林籃網隊（Brooklyn Nets）。')

  
  
  
