import streamlit as st
import requests

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="TikTok Affiliate Viewer", layout="wide")

st.title("🛒 ระบบจัดการวีดีโอ TikTok (ติดตะกร้า)")
st.write("ระบบนี้จะดึงข้อมูลหน้าปกคลิปมาให้คุณจดบันทึกรายละเอียดสินค้าได้ง่ายขึ้น")

# ช่องสำหรับใส่ URL
tiktok_url = st.text_input("🔗 ใส่ลิงก์วีดีโอ TikTok ตรงนี้:")

if tiktok_url:
    st.markdown("---")
    
    # ใช้ TikTok oEmbed API ดึงข้อมูลคลิป
    api_url = f"https://www.tiktok.com/oembed?url={tiktok_url}"
    
    try:
        response = requests.get(api_url)
        data = response.json()
        
        if "title" in data:
            col1, col2 = st.columns([1, 2])
            
            with col1:
                # แสดงภาพหน้าปก
                if "thumbnail_url" in data:
                    st.image(data["thumbnail_url"], use_container_width=True)
                
                # ปุ่มกดเด้งไปดูคลิปจริง (สีชมพูแบบ TikTok)
                button_html = f'''
                <a href="{tiktok_url}" target="_blank" style="display: block; width: 100%; padding: 10px 0; background-color: #FE2C55; color: white; text-align: center; text-decoration: none; border-radius: 8px; font-weight: bold; margin-top: 10px;">
                    ▶️ คลิกดูวีดีโอคลิปนี้
                </a>
                '''
                st.markdown(button_html, unsafe_allow_html=True)
                
            with col2:
                # แสดงรายละเอียดคลิป
                st.subheader(f"📌 {data['title']}")
                st.write(f"👤 **ช่อง:** {data['author_name']}")
                
                # พื้นที่สำหรับใส่ลูกเล่นเพิ่มเติม
                st.write("---")
                notes = st.text_area("📝 บันทึกข้อมูลสินค้า / ค่าคอมมิชชัน / ตะกร้า:", height=150)
                if st.button("💾 บันทึกข้อมูล"):
                    st.success("บันทึกข้อมูลเรียบร้อย!")
        else:
            st.error("❌ ลิงก์ไม่ถูกต้อง หรือ TikTok ตั้งค่าคลิปนี้เป็นส่วนตัว")
            
    except Exception as e:
        st.error("เกิดข้อผิดพลาดในการเชื่อมต่อกับ TikTok")
