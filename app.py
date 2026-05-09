import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="JUHAYNA IT SOP",
    page_icon="🥛",
    layout="wide"
)

# 2. Custom CSS for Juhayna Blue/Green Theme
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Cairo', sans-serif;
        text-align: right;
    }
    
    .main-header {
        background-color: white;
        border-top: 10px solid #0056b3;
        border-bottom: 5px solid #28a745;
        padding: 25px;
        text-align: center;
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 30px;
    }
    
    .company-name { color: #0056b3; font-size: 45px; font-weight: 900; margin: 0; }
    .doc-title { color: #34495e; font-size: 22px; margin-top: 10px; font-weight: 700; }
    .author-badge { background: #28a745; color: white; padding: 8px 20px; border-radius: 25px; font-weight: bold; display: inline-block; margin-top: 15px; }
    
    .step-box {
        background-color: #f0f7ff;
        border-right: 6px solid #0056b3;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 15px;
        direction: rtl;
    }
    .eng-text {
        font-family: 'Arial';
        color: #5a6268;
        font-size: 14px;
        display: block;
        text-align: left;
        direction: ltr;
        margin-top: 8px;
        font-style: italic;
    }
    .stTable { direction: rtl; }
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar Navigation
st.sidebar.markdown("<h2 style='text-align: center; color: #0056b3;'>JUHAYNA IT</h2>", unsafe_allow_html=True)
selection = st.sidebar.radio("القائمة الرئيسية:", [
    "1. Operational Philosophy",
    "2. Managing Visit Steps",
    "3. Credit Management",
    "4. Shipment Bypass",
    "5. Posting & Audit",
    "📌 Troubleshooting Summary"
])

# 4. Header Section
st.markdown(f"""
    <div class="main-header">
        <div class="company-name">JUHAYNA</div>
        <div class="doc-title">Advanced IT & ERP Operations Documentation (SOP)</div>
        <span class="author-badge">Lead by: Mohamed Kotb Ibrahim</span>
        <p style='margin-top:10px; color:#6c757d;'>Version 2.2 | May 2026</p>
    </div>
""", unsafe_allow_html=True)

# 5. Content Logic
if selection == "1. Operational Philosophy":
    st.header("فلسفة التشغيل ومنطق المسارات | Route Logic")
    st.image("https://images.pexels.com/photos/1267338/pexels-photo-1267338.jpeg?w=800")
    st.markdown("""
    <div class="step-box">
        <b>المسارات المبردة (Dairy/Zabado):</b> نستخدم نظام الـ Online Return لسحب التوالف لحظياً وربطها بفواتير الشهر.
        <span class="eng-text">Utilize Online Return for real-time monitoring of short shelf-life products.</span>
    </div>
    <div class="step-box">
        <b>المسارات الجافة (Juice/Milk):</b> نستخدم نظام الـ Manual Return لتبسيط الدورة المستندية نظراً لطول فترة الصلاحية.
        <span class="eng-text">Utilize Manual Return for products with long shelf life (up to 6 months).</span>
    </div>
    """, unsafe_allow_html=True)

elif selection == "2. Managing Visit Steps":
    st.header("إدارة خطوات الزيارة | List Ops")
    st.image("https://images.pexels.com/photos/6330644/pexels-photo-6330644.jpeg?w=800")
    st.markdown("""
    <div class="step-box">
        <b>1. Invoice/Order:</b> تفعيل Visible وتعطيل Can Skip. التجاوز مسموح فقط بذكر سبب (Shop Closed).
    </div>
    <div class="step-box">
        <b>2. Survey:</b> بند رقابي إلزامي لمتابعة رضا العملاء ولا يمكن تجاوزه.
    </div>
    <div class="step-box">
        <b>3. Return:</b> ضبط النوع (Online للمبرد / Standard للجاف) مع تفعيل Can Skip.
    </div>
    """, unsafe_allow_html=True)

elif selection == "3. Credit Management":
    st.header("إدارة الائتمان وسقوط المديونية | SAP SE16")
    st.image("https://images.pexels.com/photos/6801648/pexels-photo-6801648.jpeg?w=800")
    st.markdown("""
    <div class="step-box">
        <b>1. جلب البيانات:</b> استخراج الـ Payment Reference من شاشة ZSD_ZEIN_72.
    </div>
    <div class="step-box">
        <b>2. التنفيذ في SAP:</b> دخول SE16 جدول ZOUTSTAND_COLL وحذف السطر المختار.
    </div>
    <div class="step-box">
        <b>3. الحفظ:</b> الضغط على Save لرد الائتمان وظهور الرصيد في SalesBuzz.
    </div>
    """, unsafe_allow_html=True)
    st.warning("⚠️ لا يتم حذف أي تحصيل من الشهر الحالي بدون موافقة رسمية من المالية.")

elif selection == "4. Shipment Bypass":
    st.header("تعديل النقلات وفك القيود | VT02N & SM30")
    st.image("https://images.pexels.com/photos/6169137/pexels-photo-6169137.jpeg?w=800")
    st.markdown("""
    <div class="step-box">
        <b>1. VT02N:</b> تغيير رقم السيارة في تبويب Addit. Data.
    </div>
    <div class="step-box">
        <b>2. SM30:</b> إلغاء تفعيل Activate عن Route 10 في جدول ZUSER_EXITS.
    </div>
    <div class="step-box">
        <b>3. الأمان:</b> الحفظ في VT02N ثم إعادة تفعيل القيد فوراً في SM30.
    </div>
    """, unsafe_allow_html=True)

elif selection == "5. Posting & Audit":
    st.header("فحص حالة الترحيل والجرد | MB58 Audit")
    st.image("https://images.pexels.com/photos/4483610/pexels-photo-4483610.jpeg?w=800")
    st.markdown("""
    <div class="step-box">
        <b>ZKE:</b> الفاتورة مرحلة ومغلقة مالياً؛ الحذف ممنوع تماماً.
    </div>
    <div class="step-box">
        <b>ZKR:</b> الفاتورة معلقة؛ الحذف مسموح بطلب المالية.
    </div>
    <div class="step-box">
        <b>MB58:</b> مطابقة الباتشات لضمان قبول المرتجع على الـ Handheld.
    </div>
    """, unsafe_allow_html=True)

elif selection == "📌 Troubleshooting Summary":
    st.header("ملخص الحلول السريعة | Quick Fix Guide")
    st.image("https://images.pexels.com/photos/3183150/pexels-photo-3183150.jpeg?w=800")
    
    st.error("ممنوع عمل Update على الـ Handheld وقت شغل المندوب.")
    
    df_data = {
        "المشكلة": ["الائتمان متوقف؟", "مشكلة في المرتجع؟", "تغيير رقم سيارة؟", "بيانات ناقصة؟", "التفتيش الميداني؟"],
        "الحل": [
            "SAP Table ZOUTSTAND_COLL -> حذف المرجع -> Save",
            "List Ops -> General -> التأكد من نوع الـ Return",
            "إلغاء Route 10 (SM30) -> تعديل VT02N -> إعادة التفعيل",
            "مراجعة صلاحيات التقارير (Report Level Permission)",
            "الدخول للمعاينة مسموح؛ التحديث (Update) ممنوع"
        ]
    }
    st.table(df_data)
    st.info("💡 ملاحظة: جميع العمليات تتطلب موافقة مالية رسمية مسبقاً.")

# 6. Footer
st.markdown("---")
st.caption("Juhayna IT Operations - Senior IT Leader: Mohamed Kotb Ibrahim © 2026")
