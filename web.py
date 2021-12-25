from os import write
from threading import Condition
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time
from streamlit.proto.Button_pb2 import Button

st.title("Streamlit 超入門")

st.write("Interactive Widgeets")

'Start!!'

latest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
	latest_interation.text(f'Interration {i+1}')
	bar.progress(i+1)
	time.sleep(0.1)

'Done!!'	




















left_column, right_column = st.columns(2)

Button = left_column.button('右カラムに文字を表示')

if Button:
	right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ')
expander1.write('　　問い合わせ１')
expander2 = st.expander('問い合わせ')
expander2.write('　　問い合わせ2')




# text = st.text_input('あなたの趣味を教えてください。')
# 'あなたの趣味：',text 
# Condition = st.slider('あなたの今の調子？', 0, 100, 50)
# 'コンディション：', Condition










# option = st.selectbox(
# 	'あなたが好きいな文字を教えてください。',
# 	list(range(1,11))
# )
# 'あなたが好きな文字は、', option, 'です。'
# # if st.checkbox('Show Image'):
# # 	img = Image.open('sample.jpg')
# # 	st.image(img, caption='le van son', use_column_width=True)













# df = pd.DataFrame(
# 	np.random.rand(100,2)/[50,50]+[35.59, 139.70],
# 	columns=['lat','lon']
# )
# st.map(df)
# # # st.write(df)
# # st.table(df.style.highlight_max(axis=0))








# """
# # 章
# ## 説
# ### 項


# ``` 


# ```

# """

# {
# 	"folders": []
# }