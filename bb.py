import streamlit as st
import base64
import os
import time
from datetime import datetime

# --- 1. FONKSİYONLAR (Hafifletilmiş ve Önbellekli Arka Plan Motoru) ---
@st.cache_data
def get_base64(bin_file):
    """Resmi bir kez okur ve hafızaya atar, siteyi hızlandırır kanka."""
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None

def set_background(image_file):
    bin_str = get_base64(image_file)
    if bin_str:
        # JPG için mime type 'image/jpeg' olmalı kanka kopyala
        page_bg_img = f'''
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{bin_str}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            transition: background 0.5s ease-in-out; /* Yumuşak geçiş */
        }}
        .stMainBlockContainer {{
            background-color: rgba(10, 2, 5, 0.82); 
            border-radius: 25px;
            padding: 35px !important;
            margin-top: 30px;
            border: 2px solid #FFD700;
            box-shadow: 0 0 35px #FFD700;
        }}
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)
    else:
        # Hata kalkanı: Dosya yoksa düz bordo tema yap kanka
        st.markdown("<style>.stApp {background-color: #0a0205;}</style>", unsafe_allow_html=True)

# --- 2. SAYFA AYARLARI ---
st.set_page_config(page_title="30 Mart: Aramızdaki Mucize", page_icon="🌹")

# --- 3. PREMIUM ROMANTİK/ASİL CSS (Okunaklılık ve Şatafat) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Satisfy&family=Great+Vibes&display=swap');
    
    .romantic-title { 
        font-family: 'Great Vibes', cursive; color: #FFD700; text-align: center; 
        font-size: 60px; text-shadow: 2px 2px 10px #000, 0 0 20px #FFD700; 
        margin-bottom: 20px;
    }
    .welcome-text {
        color: white; font-family: 'Georgia', serif; font-size: 26px; 
        text-align: center; margin-top: 30px; margin-bottom: 30px; line-height: 1.6;
        text-shadow: 1px 1px 3px #000;
    }
    .siir-box { 
        font-family: 'Dancing Script', cursive; color: #ffffff; font-size: 30px; 
        text-align: center; line-height: 1.5; padding: 25px; 
        text-shadow: 2px 2px 4px #000; background-color: rgba(0,0,0,0.3); border-radius: 20px;
        border: 1px solid rgba(255, 215, 0, 0.2);
    }
    .report-box { 
        background-color: rgba(255, 215, 0, 0.1); border: 1px solid #FFD700; 
        border-radius: 15px; padding: 20px; color: white; font-size: 19px; 
        text-align: center; font-family: 'Georgia', serif; text-shadow: 1px 1px 2px #000;
    }
    .stButton>button { 
        background-color: #D32F2F !important; color: white !important; 
        border-radius: 50px !important; border: 2px solid #FFD700 !important; 
        font-size: 21px !important; width: 100%; height: 3em !important; transition: 0.3s; 
    }
    .stButton>button:hover { transform: scale(1.05); box-shadow: 0 0 35px #FFD700; }
    .stRadio>div { background-color: rgba(255, 255, 255, 0.05); border-radius: 15px; padding: 15px; border: 1px solid #FFD700; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. OTURUM YÖNETİMİ ---
if 'asama' not in st.session_state: st.session_state.asama = 'giris'
if 'ani_no' not in st.session_state: st.session_state.ani_no = 1
if 'cevaplar' not in st.session_state: st.session_state.cevaplar = []

# --- AŞAMA 1: GİRİŞ (ŞİFRESİZ YENİ DAVET SAHNESİ) ---
if st.session_state.asama == 'giris':
    set_background('biz_arkaplan.jpg')
    st.markdown("<h1 class='romantic-title'>Hoşgeldin Asaletim...</h1>", unsafe_allow_html=True)
    st.markdown("<div class='welcome-text'>Benimle güzel bir yolculuğa çıkmaya hazır mısın?</div>", unsafe_allow_html=True)
    if st.button("EVET, HAZIRIM! ❤️🌹"):
        with st.spinner('Yolculuğumuz başlıyor...'): # Hız göstergesi
            time.sleep(1)
            st.session_state.asama = 'anilar'
            st.rerun()

# --- AŞAMA 2: BİRLEŞTİRİLMİŞ ANILAR ---
elif st.session_state.asama == 'anilar':
    # Sıradaki anıya göre arka planı değiştiriyoruz kanka
    if os.path.exists(f'biz{st.session_state.ani_no}.jpg'):
        set_background(f'biz{st.session_state.ani_no}.jpg')
    else:
        set_background('biz_arkaplan.jpg') # Yedek

    st.markdown("<h1 class='romantic-title'>Bizim Hikayemiz</h1>", unsafe_allow_html=True)

    ani = st.session_state.ani_no
    if ani <= 4:
        if os.path.exists(f"biz{ani}.jpg"):
            st.image(f"biz{ani}.jpg", use_container_width=True)
        else:
            st.error(f"🚨 Kanka 'biz{ani}.jpg' bulunamadı!")

        # Sorular
        if ani == 1:
            st.markdown("<p style='text-align:center; color:white; font-size:22px;'>Beni en çok kendine hayran bırakan ne oldu?</p>", unsafe_allow_html=True)
            cevap = st.radio("", ["Gözlerindeki o eşsiz ışıltı.", "Zarafetin ve asalet dolu duruşun.", "Dünyanın en güzel kalbine sahip olman."])
            if st.button("SONRAKİ ANI ✨"):
                st.session_state.cevaplar.append(f"🌹 Hayranlık: {cevap}")
                st.session_state.ani_no = 2
                st.rerun()
        elif ani == 2:
            st.markdown("<p style='text-align:center; color:white; font-size:22px;'>Beni kendine nasıl aşık ediyorsun?</p>", unsafe_allow_html=True)
            cevap = st.radio("", ["Sadece sesini duymak yetiyor.", "Karakterindeki güç ve güven.", "Hayallerimizden bahsederkenki gülüşün."])
            if st.button("SONRAKİ ANI ✨"):
                st.session_state.cevaplar.append(f"💖 Aşkın Gücü: {cevap}")
                st.session_state.ani_no = 3
                st.rerun()
        elif ani == 3:
            st.markdown("<p style='text-align:center; color:white; font-size:22px;'>Aramızdaki mesafeler sence bize ne kattı?</p>", unsafe_allow_html=True)
            cevap = st.radio("", ["Birbirimizin kıymetini daha iyi anladık.", "Sabretmeyi ve özlemeyi öğrendik.", "Aşkımızı daha da kökleştirdi."])
            if st.button("SONRAKİ ANI ✨"):
                st.session_state.cevaplar.append(f"🗺️ Mesafeler: {cevap}")
                st.session_state.ani_no = 4
                st.rerun()
        elif ani == 4:
            st.markdown("<p style='text-align:center; color:white; font-size:22px;'>Senin için yapacağım ilk büyük jest ne olsun?</p>", unsafe_allow_html=True)
            cevap = st.radio("", ["Dev bir gül buketi.", "Sana özel keman dinletisi.", "Sana sımsıkı sarılıp kokunu içime çekmek."])
            if st.button("ŞİİRİME ULAŞ 🌹💎"):
                st.session_state.cevaplar.append(f"🎁 İlk Jest: {cevap}")
                st.session_state.asama = 'siir'
                st.rerun()

# --- AŞAMA 3: ŞİİR ---
elif st.session_state.asama == 'siir':
    set_background('biz_arkaplan.jpg')
    st.markdown("<h1 class='romantic-title'>Sevmeden Olur Mu...</h1>", unsafe_allow_html=True)
    
    siir = """
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
    Tıpkı diğer tüm günlerde olduğu gibi...<br>
    Sevmeden olur mu sevgilim...
    </div>
    """
    st.markdown(siir, unsafe_allow_html=True)
    
    if st.button("SON SÜRPRİZ VE RAPOR ❤️💎"):
        with st.status("Veriler işleniyor asaletim...", expanded=True) as status:
            time.sleep(1)
            status.update(label="Rapor Hazır!", state="complete", expanded=False)
        st.session_state.asama = 'final'
        st.rerun()

# --- AŞAMA 4: FİNAL VE CEVAP ÖZETİ (RESİMSİZ FİNAL SAHNESİ) ---
elif st.session_state.asama == 'final':
    set_background('biz_arkaplan.jpg')
    st.balloons() # Doğum günü konfetisi
    st.markdown("<h1 class='romantic-title'>İyi Ki Doğdun Asaletim!</h1>", unsafe_allow_html=True)
    
    # Rapor Box
    st.markdown("<div class='report-box'>✨ <b>Bizim Hakkımızdaki Seçimlerin:</b><br><br>" + 
                "<br>".join(st.session_state.cevaplar) + "</div>", unsafe_allow_html=True)

    # Güllü Final ve Screenshot Önerisi (Kanka başa dön tuşu kaldırıldı kopyala)
    st.markdown("<div style='color:#FFD700; text-align:center; font-size:20px; border:1px dashed #FFD700; padding:15px; margin-top:20px;'>📸 Çok sevdiğin sevgiline sonuçların ekran görüntüsünü atmaya ne dersin?</div>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-size:60px; margin-top:20px;'>🌹🌹🌹</p>", unsafe_allow_html=True)