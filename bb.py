import streamlit as st
import base64
import os
import time
from datetime import datetime

# --- 1. ÖNBELLEKLİ GÖRSEL MOTORU ---
@st.cache_data
def get_base64(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None

def set_background(image_file):
    bin_str = get_base64(image_file)
    if bin_str:
        page_bg_img = f'''
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{bin_str}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        .stMainBlockContainer {{
            background-color: rgba(10, 2, 5, 0.88); 
            border-radius: 20px;
            padding: 25px 15px !important;
            margin-top: 15px;
            border: 1px solid #FFD700;
            box-shadow: 0 0 25px #FFD700;
            width: 95% !important;
        }}
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)
    else:
        st.markdown("<style>.stApp {background-color: #0a0205;}</style>", unsafe_allow_html=True)

# --- 2. SAYFA AYARLARI ---
st.set_page_config(page_title="30 Mart: Asaletim", page_icon="🌹")

# --- 3. PREMIUM MOBİL CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;1,600&family=Great+Vibes&display=swap');
    
    .romantic-title { 
        font-family: 'Great Vibes', cursive; color: #FFD700; text-align: center; 
        font-size: 45px; text-shadow: 2px 2px 8px #000; margin-bottom: 25px;
    }
    
    .siir-box { 
        font-family: 'Playfair Display', serif; 
        color: #ffffff; 
        font-size: 28px; 
        text-align: center; 
        line-height: 2.0; 
        padding: 25px; 
        font-style: italic;
        font-weight: 600; 
        text-shadow: 2px 2px 10px #000; 
        background-color: rgba(0, 0, 0, 0.65); 
        border-radius: 20px;
        letter-spacing: 1px; 
        word-wrap: break-word;
    }

    .report-box { background-color: rgba(255, 215, 0, 0.15); border: 2px solid #FFD700; border-radius: 15px; padding: 20px; color: white; font-size: 19px; text-align: center; line-height: 1.6; }
    .stButton>button { background-color: #D32F2F !important; color: white !important; border-radius: 50px !important; border: 2px solid #FFD700 !important; font-size: 22px !important; width: 100%; height: 3.5em !important; box-shadow: 0 0 20px #FFD700; }
    .stRadio>div { background-color: rgba(255, 255, 255, 0.05); border-radius: 12px; padding: 12px; border: 1px solid #FFD700; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. OTURUM YÖNETİMİ ---
if 'asama' not in st.session_state: st.session_state.asama = 'giris'
if 'ani_no' not in st.session_state: st.session_state.ani_no = 1
if 'cevaplar' not in st.session_state: st.session_state.cevaplar = []

# --- AŞAMA 1: DAVET ---
if st.session_state.asama == 'giris':
    set_background('biz_arkaplan.jpg')
    st.markdown("<h1 class='romantic-title'>Hoşgeldin Asaletim...</h1>", unsafe_allow_html=True)
    st.markdown("<div style='color:white; text-align:center; font-size:24px; margin:30px 0;'>Benimle güzel bir yolculuğa çıkmaya hazır mısın?</div>", unsafe_allow_html=True)
    if st.button("EVET, HAZIRIM! ❤️🌹"):
        st.session_state.asama = 'anilar'
        st.rerun()

# --- AŞAMA 2: ANILAR VE ETİKETLİ SORULAR ---
elif st.session_state.asama == 'anilar':
    current_img = f'biz{st.session_state.ani_no}.jpg'
    set_background(current_img if os.path.exists(current_img) else 'biz_arkaplan.jpg')
    st.markdown("<h1 class='romantic-title'>Hikayemiz</h1>", unsafe_allow_html=True)

    ani = st.session_state.ani_no
    if ani <= 4:
        st.image(current_img if os.path.exists(current_img) else 'biz_arkaplan.jpg', use_container_width=True)
        
        # Senin istediğin o özel etiketler burada kanka
        labels = [
            "Hayranlık duyduğun yanım",
            "Beni kendine bağlayan özelliğim",
            "Mesafelerin bize kattığı değer",
            "Senin için yapacağım ilk büyük jest"
        ]
        
        questions = [
            "Hayranlık duyduğum yanım ne aşkım ?", 
            "Beni sana bağlayan ne bebeğim ?", 
            "Mesafeler sence bize ne kattı aşkım ?", 
            "İlk büyük jestimiz ne olsun sevgilim ?"
        ]
        options = [
            ["Gözlerindeki ışıltı.", "Asalet dolu duruşun.", "En güzel kalbin."],
            ["Sesini duymak.", "Güven veren karakterin.", "Gülüşün."],
            ["Kıymetimizi anladık.", "Özlemeyi öğrendik.", "Aşkımızı kökleştirdi."],
            ["Dev bir gül buketi.", "tutkulu öpüşme .", "Sana sımsıkı sarılmak."]
        ]
        
        st.markdown(f"<p style='text-align:center; color:white; font-size:20px;'>{questions[ani-1]}</p>", unsafe_allow_html=True)
        cevap = st.radio("", options[ani-1], key=f"radio_{ani}")
        
        if st.button("DEVAM ET ✨" if ani < 4 else "ŞİİRİME ULAŞ 🌹"):
            # Tercihleri cümle yapısıyla kaydediyoruz kanka
            st.session_state.cevaplar.append(f"📌 <b>{labels[ani-1]}:</b> {cevap}")
            if ani < 4:
                st.session_state.ani_no += 1
            else:
                st.session_state.asama = 'siir'
            st.rerun()

# --- AŞAMA 3: ŞİİR ---
elif st.session_state.asama == 'siir':
    set_background('biz_arkaplan.jpg')
    st.markdown("<h1 class='romantic-title'>Sevmeden Olur Mu...</h1>", unsafe_allow_html=True)
    
    siir_temiz = """
    <div class="siir-box">
    Ay da bekler mi her gün güneşini?<br>
    Neden onca yıldız içinden tek güneşini?<br>
    Doğmaz mıydı bir kere daha gün,<br>
    Sevmeden olur mu sevgilim...<br><br>
    
    Güneş midir geceyi hep aydınlatan,<br>
    Yoksa gece midir gündüze hasret kalan?<br>
    Gözlerin midir beni sana aşık eden,<br>
    Sevmeden olur mu sevgilim...<br><br>
    
    Bir gün değil, her gün sever mi insan?<br>
    O güzel gülüşünü, sesini, her şeyini...<br>
    Aşkın imkansızı da güzeldir, değil mi?<br>
    Sevmeden olur mu sevgilim...<br><br>
    
    Doğum mudur bizi dünyaya bağlayan,<br>
    Yoksa düşünceler, duygular, hisler mi?<br>
    Doğum gününde de seveceğim seni sevgilim,<br>
    Tıpkı diğer her günde olduğu gibi...<br>
    Sevmeden olur mu sevgilim...
    </div>
    """
    st.markdown(siir_temiz, unsafe_allow_html=True)
    
    if st.button("KALBİMİN ÖZETİ ❤️💎"):
        st.session_state.asama = 'final'
        st.rerun()

# --- AŞAMA 4: FİNAL ---
elif st.session_state.asama == 'final':
    set_background('biz_arkaplan.jpg')
    st.balloons()
    st.markdown("<h1 class='romantic-title'>Seni Seviyorum sevgilim !</h1>", unsafe_allow_html=True)
    # Rapor artık senin istediğin etiketlerle geliyor kanka
    st.markdown("<div class='report-box'>✨ <b>Senin Tercihlerin, Benim Dünyam:</b><br><br>" + 
                "<br>".join(st.session_state.cevaplar) + "</div>", unsafe_allow_html=True)
    st.markdown("<div style='color:#FFD700; text-align:center; font-size:18px; border:1px dashed #FFD700; padding:15px; margin-top:20px;'>📸 Sonuçların ekran görüntüsünü sevgiline atmaya ne dersin?</div>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-size:50px; margin-top:10px;'>🌹🌹🌹</p>", unsafe_allow_html=True)