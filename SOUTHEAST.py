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
  col1.metric("聯盟冠軍🏆", "1  次")
  col2.metric("分組冠軍🏆", "4  次")   
def CharlotteHornets():
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('Charlotte Hornets.png')
    st.image(image) 
  with col2:
     st.title('Charlotte Hornets')
     st.subheader('老闆:Michael Jordan')
     st.subheader('GM:Mitch Kupchak')
     st.subheader('總教練:Steve Clifford')     
  st.write('夏洛特黃蜂（1988年–2002年）夏洛特山貓（2004年–2014年）夏洛特黃蜂（1988年–2002年、2014年–至今）') 
  st.write('夏洛特黃蜂隊的英文隊名為Charlotte Hornets，球隊成立於2004年，目前所在城市是美國北卡羅來納州夏洛特市(Charlotte, North Carolina)，主場為時代華納中心球館(Time Warner Cable Arena)。')
  col1, col2= st.columns(2)
  col1.metric("聯盟冠軍🏆", "0  次")
  col2.metric("分組冠軍🏆", "0  次")   
def MiamiHeat():
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('Miami Heat.png')
    st.image(image) 
  with col2:
     st.title('Miami Heat')
     st.subheader('老闆:Micky Arison')
     st.subheader('GM:Andy Elisburg')
     st.subheader('總教練:	Erik Spoelstra')     
  st.write('邁阿密熱火(1988年--至今）') 
  st.write('邁阿密熱火的英文隊名為Miami Heat，成立於1988年，目前所在地區是美國佛羅里達州邁阿密市(Miami, Florida)，主場為美國航空競技館(American Airlines Arena)，熱火隊的三巨頭分別是Dwyane Wade、LeBron James和Chris Bosh。1988年才加入NBA的年輕隊伍，在2005年-06年賽季首度通過東部決賽，打入總冠軍賽，在面對達拉斯小牛隊時原本連輸兩局，但最終倒贏小牛隊以4：2逆轉擊敗而奪冠。直到2011年再度打入NBA總決賽，對手同樣是2006年時遇到的小牛隊，這次邁阿密熱火隊以2：4未能奪得總冠軍，不過2012年再度打入NBA總決賽，對手是奧克拉荷馬雷霆隊，這次邁阿密熱火隊以4：1奪得總冠軍。2013年三度打入NBA總決賽，對手是拿過四次NBA總冠軍的聖安東尼奧馬刺隊，經過激戰七場，邁阿密熱火隊以4：3奪得總冠軍完成二連霸。2014年熱火再次於總決賽和馬刺隊碰頭，然而最終以1：4終止三連霸美夢。')
  col1, col2= st.columns(2)
  col1.metric("聯盟冠軍🏆", "3  次")
  col2.metric("分組冠軍🏆", "6  次")   
def OrlandoMagic():
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('Orlando Magic.png')
    st.image(image) 
  with col2:
     st.title('Orlando Magic')
     st.subheader('老闆:RDV Sports, Inc.(Dan DeVos, chairman)')
     st.subheader('GM:John Hammond')
     st.subheader('總教練:Jamahl Mosley')     
  st.write('奧蘭多魔術(1989年-至今)') 
  st.write('奧蘭多魔術隊的英文隊名為Orlando Magic，球隊成立於1989年，所在地區是美國佛羅里達州奧蘭多市(Orlando, Florida)，主場為安利中心(Amway Center)。')
  col1, col2= st.columns(2)
  col1.metric("聯盟冠軍🏆", "0  次")
  col2.metric("分組冠軍🏆", "2  次")    
def WashingtonWizards():
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('Washington Wizards.png')
    st.image(image) 
  with col2:
     st.title('Washington Wizards')
     st.subheader('老闆:Monumental Sports & Entertainment')
     st.subheader('GM:Tommy Sheppard')
     st.subheader('總教練:Wes Unseld Jr.')     
  st.write('芝加哥包裝工(1961年-1962年)芝加哥西風(1962年-1963年)巴爾的摩子彈(1963年-1972年)首都子彈(1973年-1974年)華盛頓子彈(1974年-1997年)華盛頓巫師(1997年-)') 
  st.write('華盛頓巫師隊的英文隊名為Washington Wizards，球隊成立於1961年，目前所在城市是美國華盛頓特區(Washington, D.C.)，現在主場為Verizon Center(原MIC中心球館 MCI Center)。巫師隊是隊名變化最頻繁的一支球隊，在1961年加入NBA時主場在芝加哥所以取名芝加哥包裝工隊，第二年改名芝加哥和風隊，第三年因為主場遷移到工業城市巴爾的摩，而改名巴爾的摩子彈隊，後來主場又移到華盛頓，隊名更動為華盛頓子彈隊，在1997年-1998年賽季則改為現在的華盛頓巫師隊。')
  col1, col2= st.columns(2)
  col1.metric("聯盟冠軍🏆", "1  次")
  col2.metric("分組冠軍🏆", "4  次")   
