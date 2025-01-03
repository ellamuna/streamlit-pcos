import streamlit as st
import pandas as pd
import pickle as pkl
import plotly.express as px
from streamlit_option_menu import option_menu

# Streamlit Page Configuration
st.set_page_config(
    page_title="PCOS Prediction App",
    page_icon="https://eu-images.contentstack.com/v3/assets/blt6b0f74e5591baa03/blt7c0bf7e21d4410b4/6319700b8cc2fa14e223aa27/8895.png",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        "Get help": "https://github.com/AdieLaine/Streamly",
        "Report a bug": "https://github.com/AdieLaine/Streamly",
        "About": """
            ## Streamly Streamlit Assistant
            ### Powered using GPT-4o-mini

            **GitHub**: https://github.com/AdieLaine/

            The AI Assistant named, Streamly, aims to provide the latest updates from Streamlit,
            generate code snippets for Streamlit widgets,
            and answer questions about Streamlit's latest features, issues, and more.
            Streamly has been trained on the latest Streamlit updates and documentation.
        """
    })

# Sidebar untuk memilih halaman
with st.sidebar:
    selected = option_menu(
    menu_title=None,
    options=["Home", "Data Visualisation", "Prediction"],
    icons=["house", "book", "calculator"],
    menu_icon="cast",
    default_index=0,
    # orientation="horizontal",
)
    
row0_spacer1, row0_1, row0_spacer2 = st.columns((0.1, 3.2, 0.1))
row1_spacer1, row1_1, row1_spacer2, row1_2 = st.columns((0.1, 1.5, 0.1, 1.5))
row0_spacer3, row3_0, row0_spacer4 = st.columns((0.1, 3.2, 0.1))

# Judul aplikasi
row0_1.title("PCOS Prediction App")

# Load dataset
df = pd.read_csv('clean_pcos_data.csv')

if selected == "Home":
    with row0_1:
        st.markdown(
            "PCOS Prediction App adalah sebuah aplikasi yang berguna untuk memprediksi kemungkinan seseorang menderita PCOS berdasarkan beberapa fitur yang dimasukkan. Aplikasi ini menggunakan dataset PCOS dari Kaggle untuk melakukan prediksi. Dengan memasukkan fitur yang relevan, seperti frekuensi siklus menstruasi, jumlah follicle dalam ovarium dan sebagainya, aplikasi ini dapat memberikan prediksi yang cukup akurat mengenai kemungkinan seseorang menderita PCOS. Aplikasi ini sangat bermanfaat bagi orang-orang yang ingin mengetahui apakah mereka berisiko terkena PCOS atau tidak, sehingga dapat memperbaiki pola makan dan gaya hidup mereka untuk mencegah terjadinya PCOS."
        )
        st.markdown('Dataset : https://www.kaggle.com/prasoonkottarathil/polycystic-ovary-syndrome-pcos')
        st.write(df.head())
        st.markdown('Atribut Dataset :')
        st.markdown("1. Target : Merupakan hasil diagnosis pasien PCOS, 0 berarti tidak terkena PCOS, 1 berarti terkena PCOS")
        st.markdown("2. Cycle (R/I) : Merupakan status siklus menstruasi, yang diklasifikasikan sebagai Regular (R) atau Irregular (I).")
        st.markdown("3. AMH : (Anti-Müllerian Hormone) Pada wanita dengan PCOS, kadar AMH cenderung lebih tinggi dibandingkan wanita tanpa PCOS.")
        st.markdown("4. Weight Gain : Merupakan penambahan berat badan pada pasien terutama yang tidak diinginkan atau berlebihan")
        st.markdown("5. Hair Growth : Merupakan pertumbuhan rambut yang tidak diinginkan atau berlebih pada wanita, suatu kondisi yang dikenal sebagai hirsutisme.")
        st.markdown("6. Skin Darkening : Merupakan penggelapan kulit pada pasien jika mengalami resistensi insulin ")
        st.markdown("7. Pimples : Merujuk apakah pasien memiliki masalah jerawat atau tidak.")
        st.markdown("8. Fast Food : Merujuk pada kebiasaan mengonsumsi makanan cepat saji. Apakah pasien sering mengonsumsi fast food atau tidak")
        st.markdown("9. Follicle : Merupakan jumlah folikel yang terlihat di ovarium kanan dan kiri masing-masing pada pasien")
        
elif selected == "Data Visualisation":
    # Data Visualisasi dengan plotly
    with row1_1:
        st.subheader('Pilih fitur yang ingin ditampilkan histogramnya')
        fitur = st.selectbox('Fitur', df.columns.tolist())
        fig = px.histogram(df, x=fitur, color='Target', marginal='box', hover_data=df.columns)
        st.plotly_chart(fig)
        fig = px.histogram(df, x='Target', color='Cycle(R/I)', barmode='group', hover_data=df.columns)
        fig.update_layout(title='Jumlah pasien berdasarkan siklus menstruasi (Regular/Irregular)', xaxis_title='Target', yaxis_title='Jumlah', font=dict(size=15))
        st.plotly_chart(fig)
        st.markdown(
            'Dari grafik diatas menunjukkan bahwa Pasien dengan PCOS cenderung lebih sering memiliki siklus menstruasi tidak teratur dibandingkan pasien tanpa PCOS. Namun, tidak semua pasien dengan PCOS mengalami siklus tidak teratur, yang menunjukkan adanya variabilitas gejala PCOS. Sebagian besar pasien tanpa PCOS memiliki siklus menstruasi yang teratur, sehingga siklus tidak teratur kemungkinan lebih jarang terjadi tanpa adanya faktor hormonal seperti pada PCOS.'
        )
        fig = px.histogram(df, x='Target', color='Weight gain(Y/N)', barmode='group', hover_data=df.columns)
        fig.update_layout(title='Jumlah pasien yang mengalami kenaikan berat badan', xaxis_title='Target', yaxis_title='Jumlah', font=dict(size=15))
        st.plotly_chart(fig)
        st.markdown(
            "Data menunjukkan bahwa Pasien dengan PCOS cenderung lebih banyak mengalami kenaikan berat badan dibandingkan pasien tanpa PCOS. Meskipun sebagian besar pasien PCOS mengalami kenaikan berat badan, ada juga subset pasien yang tidak mengalaminya. Hal ini menunjukkan bahwa kenaikan berat badan mungkin merupakan salah satu gejala PCOS tetapi bukan indikator eksklusif."
        )
        
    with row1_2:
        st.subheader('Pilih fitur yang ingin ditampilkan scatter plotnya')
        fitur1 = st.selectbox('Fitur 1', df.columns.tolist())
        fitur2 = st.selectbox('Fitur 2', df.columns.tolist())
        fig = px.scatter(df, x=fitur1, y=fitur2, color='Target', hover_data=df.columns)
        st.plotly_chart(fig)
        fig = px.histogram(df, x='Target', color='Target', hover_data=df.columns)
        fig.update_layout(title='Jumlah Pasien PCOS', xaxis_title='Target', yaxis_title='Jumlah', font=dict(size=15))
        st.plotly_chart(fig)
        st.markdown(
            'Mari kita lihat grafik di atas. Dari grafik tersebut, terlihat bahwa mayoritas pasien wanita yang dianalisis dalam studi ini tidak terkena PCOS. Namun, terdapat sejumlah kecil pasien wanita yang terdiagnosis dengan PCOS, yaitu hanya 177 pasien wanita dari keseluruhan. Ini menunjukkan bahwa PCOS mungkin masih merupakan masalah kesehatan yang signifikan, namun masih mempengaruhi sebagian kecil populasi.'
        )
        fig = px.histogram(df, x='Target', color='Fast food (Y/N)', barmode='group', hover_data=df.columns)
        fig.update_layout(title='Jumlah pasien berdasarkan sering atau tidaknya konsumsi fast food', xaxis_title='Target', yaxis_title='Jumlah', font=dict(size=15))
        st.plotly_chart(fig)
        st.markdown(
            'Grafik menunjukkan bahwa pasien yang tidak memiliki PCOS (target = 0) didominasi oleh individu yang tidak sering mengonsumsi fast food (fast food = 0), dengan jumlahnya lebih tinggi dibandingkan yang sering mengonsumsi fast food. Dan Pasien yang memiliki PCOS (target = 1) juga memiliki proporsi lebih tinggi untuk kategori sering mengonsumsi fast food (fast food = 1) dibandingkan yang tidak.'
        )
        
        
elif selected == "Prediction":
    # Membuat tiga kolom
    col1, col2, col3= st.columns(3)

    # Input di kolom pertama
    with col1:
        weight_gain = st.radio("Apakah pasien mengalami kenaikan berat badan yang berlebihan?", ["Yes", "No"], index=None)
        cycle = st.radio("Apakah pasien memiliki siklus menstruasi yang teratur (Regular) atau tidak teratur (Irregular)?",  ["Irregular","Regular"], index=None)

    # Input di kolom kedua
    with col2:
        skin_darkening = st.radio("Apakah pasien mengalami penggelapan kulit karena resistensi insulin?",  ["Yes", "No"], index=None)
        pimples = st.radio("Apakah pasien memiliki masalah jerawat atau tidak?",  ["Yes", "No"], index=None)

    # Input di kolom ketiga
    with col3:
        follicle_L = st.number_input("Masukkan folikel sebelah kiri", min_value=0, max_value=30)
    
    
    # Input untuk siklus menstruasi
    with col1:
        hair_growth = st.radio("Apakah pasien mengalami pertumbuhan rambut yang berlebihan?",  ["Yes", "No"], index=None)

    # Input di kolom pertama
    with col2:
        fast_food = st.radio("Apakah pasien sering mengonsumsi fast food atau tidak?",  ["Yes", "No"], index=None)

    # Input di kolom kedua
    with col3:
        amh = st.number_input("Masukkan kadar AMH pada pasien", min_value=0.0, max_value=20.0, step=0.1)
        follicle_R = st.number_input("Masukkan jumlah folikel sebelah kanan", min_value=0, max_value=30)
        
        
        
    #model
    model = pkl.load(open("dataPCOS\RFC3.pkl", "rb"))
    
    
    feature_names = model.feature_names_in_
        
    if st.button("Prediksi PCOS"):
    # Mengonversi input menjadi DataFrame
        features = pd.DataFrame([[
            1 if cycle == "irregular" else 0,
            amh,
            1 if weight_gain == "yes" else 0,
            1 if hair_growth == "yes" else 0,
            1 if skin_darkening == "yes" else 0,
            1 if pimples == "yes" else 0,
            1 if fast_food == "yes" else 0,
            follicle_L,
            follicle_R
        ]], columns=feature_names)
        
        prediction = model.predict(features)
        
        if prediction[0] == 1:
            st.error("Pasien memiliki resiko terkena PCOS, segera periksa ke dokter!")
        else:
            st.success("Pasien aman dari PCOS, tetap jaga kesehatan ya!")
