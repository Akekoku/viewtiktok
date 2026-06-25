import streamlit as st
import streamlit.components.v1 as components

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="TikTok Affiliate Viewer", layout="wide")

st.title("🛒 ระบบจัดการและดูวีดีโอ TikTok (ติดตะกร้า)")
st.write("วางลิงก์วีดีโอ TikTok ที่คุณต้องการติดตามด้านล่างนี้")

# ช่องสำหรับใส่ URL
tiktok_url = st.text_input("🔗 ใส่ลิงก์วีดีโอ TikTok ตรงนี้:")

if tiktok_url:
    st.markdown("---")
    st.subheader("📺 วีดีโอของคุณ")
    
    # ดึง Video ID จาก URL คร่าวๆ
    video_id = tiktok_url.split('/')[-1].split('?')[0]
    
    # โค้ด HTML สำหรับฝังวีดีโอ TikTok
    tiktok_embed_code = f"""
    <blockquote class="tiktok-embed" cite="{tiktok_url}" data-video-id="{video_id}" style="max-width: 605px;min-width: 325px;" >
      <section>
        <a target="_blank" href="{tiktok_url}">กำลังโหลดวีดีโอ...</a>
      </section>
    </blockquote>
    <script async src="https://www.tiktok.com/embed.js"></script>
    """
    
    # แสดงผลวีดีโอ (ต้องกำหนดความสูงให้พอดีกับวีดีโอแนวตั้ง)
    components.html(tiktok_embed_code, height=750)
    
    # พื้นที่สำหรับใส่ลูกเล่นเพิ่มเติม เช่น จดบันทึก
    notes = st.text_area("📝 บันทึกข้อมูลเกี่ยวกับสินค้า/ตะกร้านี้:")
    if st.button("บันทึกข้อมูล"):
        st.success("บันทึกข้อมูลสำเร็จ! (ในเวอร์ชันจริงคุณสามารถเชื่อมกับ Database ได้)")