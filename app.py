import streamlit as st
import streamlit.components.v1 as components
import re # นำเข้าไลบรารีนี้เพิ่มเพื่อช่วยดึงรหัสวีดีโอ

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="TikTok Affiliate Viewer", layout="wide")

st.title("🛒 ระบบจัดการและดูวีดีโอ TikTok (ติดตะกร้า)")
st.write("วางลิงก์วีดีโอ TikTok ที่คุณต้องการติดตามด้านล่างนี้")

# ช่องสำหรับใส่ URL
tiktok_url = st.text_input("🔗 ใส่ลิงก์วีดีโอ TikTok ตรงนี้:")

if tiktok_url:
    st.markdown("---")
    st.subheader("📺 วีดีโอของคุณ")
    
    # ใช้ Regex ดึง Video ID ออกมาจาก URL แบบแม่นยำขึ้น
    match = re.search(r"video/(\d+)", tiktok_url)
    
    if match:
        video_id = match.group(1)
        
        # ใช้ iframe เรียกตัวเล่นวีดีโอของ TikTok โดยตรง
        iframe_code = f"""
        <div style="display: flex; justify-content: center;">
            <iframe 
                src="https://www.tiktok.com/embed/v2/{video_id}" 
                style="width: 325px; height: 750px; border: none; border-radius: 12px;" 
                allow="autoplay; encrypted-media;" 
                allowfullscreen>
            </iframe>
        </div>
        """
        
        # แสดงผลวีดีโอ
        components.html(iframe_code, height=780)
        
        # พื้นที่สำหรับใส่ลูกเล่นเพิ่มเติม เช่น จดบันทึก
        notes = st.text_area("📝 บันทึกข้อมูลเกี่ยวกับสินค้า/ตะกร้านี้:")
        if st.button("บันทึกข้อมูล"):
            st.success("บันทึกข้อมูลสำเร็จ!")
            
    else:
        st.error("❌ ไม่พบ Video ID ในลิงก์ กรุณาตรวจสอบลิงก์อีกครั้ง (ลิงก์ควรมีคำว่า /video/ตัวเลข)")
