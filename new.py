import streamlit as st
import streamlit.components.v1 as components

# 1. ตั้งค่าโครงสร้างหน้า Streamlit
st.set_page_config(
    page_title="โครงงานระบบวางแผนท่องเที่ยวอัจฉริยะด้วย AI",
    page_icon="✈️",
    layout="wide"
)

# 2. รวมโค้ด HTML/CSS ทั้งหมดไว้ในตัวแปร html_content
html_content = """
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>โครงงานระบบวางแผนท่องเที่ยวอัจฉริยะด้วย AI - Presentation</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Kanit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        body {
            font-family: 'Kanit', sans-serif;
            background: linear-gradient(135deg, #090d16, #0f172a, #1e1b4b);
            color: white;
            min-height: 100vh;
            padding-bottom: 50px;
        }
        nav {
            max-width: 1200px;
            margin: auto;
            padding: 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        }
        .logo {
            font-size: 24px;
            font-weight: 700;
            color: white;
            text-decoration: none;
        }
        .logo span {
            color: #3b82f6;
        }
        .badge {
            background: rgba(59, 130, 246, 0.1);
            border: 1px solid rgba(59, 130, 246, 0.3);
            padding: 8px 16px;
            border-radius: 30px;
            font-size: 14px;
            color: #60a5fa;
            font-weight: 500;
        }
        .presentation-cover {
            text-align: center;
            max-width: 900px;
            margin: 40px auto 30px;
            padding: 20px;
        }
        .academic-tag {
            font-size: 14px;
            color: #93c5fd;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 15px;
            display: inline-block;
            background: rgba(255, 255, 255, 0.05);
            padding: 4px 12px;
            border-radius: 4px;
        }
        .presentation-cover h1 {
            font-size: clamp(28px, 4vw, 48px);
            line-height: 1.2;
            margin-bottom: 20px;
            font-weight: 700;
        }
        .presentation-cover h1 span {
            background: linear-gradient(90deg, #3b82f6, #a78bfa);
            -webkit-background-clip: text;
            color: transparent;
        }
        .presentation-cover p.subtitle {
            color: #94a3b8;
            font-size: 16px;
            max-width: 700px;
            margin: 0 auto 30px;
            line-height: 1.6;
        }
        .credentials-card {
            background: rgba(30, 41, 59, 0.5);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 25px;
            max-width: 600px;
            margin: 0 auto 40px;
            text-align: left;
            backdrop-filter: blur(10px);
        }
        .credentials-title {
            font-size: 14px;
            color: #3b82f6;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            padding-bottom: 8px;
            margin-bottom: 15px;
            font-weight: 600;
        }
        .credentials-grid {
            display: grid;
            grid-template-columns: 140px 1fr;
            gap: 10px 15px;
            font-size: 15px;
        }
        .credentials-label {
            color: #64748b;
            font-weight: 500;
        }
        .credentials-value {
            color: #cbd5e1;
        }
        .container {
            max-width: 1200px;
            margin: auto;
            padding: 20px;
        }
        .section-title {
            text-align: center;
            margin: 40px 0 30px;
        }
        .section-title h2 {
            font-size: 28px;
            font-weight: 600;
        }
        .section-title p {
            color: #94a3b8;
            font-size: 15px;
            margin-top: 5px;
        }
        .slides-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px;
            margin-bottom: 40px;
        }
        .slide-card {
            background: rgba(15, 23, 42, 0.8);
            border: 1px solid rgba(255, 255, 255, 0.06);
            border-radius: 20px;
            padding: 25px;
            transition: all 0.3s ease;
        }
        .slide-card:hover {
            transform: translateY(-5px);
            border-color: rgba(59, 130, 246, 0.4);
            box-shadow: 0 10px 30px rgba(59, 130, 246, 0.1);
        }
        .slide-num {
            font-size: 14px;
            font-weight: 700;
            color: #3b82f6;
            margin-bottom: 10px;
            display: block;
        }
        .slide-card h3 {
            font-size: 18px;
            margin-bottom: 12px;
            color: #f8fafc;
        }
        .slide-card ul {
            list-style-type: none;
        }
        .slide-card li {
            color: #94a3b8;
            font-size: 14px;
            line-height: 1.6;
            margin-bottom: 8px;
            position: relative;
            padding-left: 18px;
        }
        .slide-card li::before {
            content: "•";
            color: #3b82f6;
            font-weight: bold;
            font-size: 16px;
            position: absolute;
            left: 0;
            top: -2px;
        }
    </style>
</head>
<body>

    <!-- NAVBAR -->
    <nav>
        <a href="#" class="logo">✈️ AI <span>Travel Project</span></a>
        <div class="badge">🎓 สื่อนำเสนอโครงงาน</div>
    </nav>

    <!-- HERO COVER -->
    <header class="presentation-cover">
        <span class="academic-tag">Project Presentation</span>
        <h1>ระบบวางแผนท่องเที่ยวอัจฉริยะ<br><span>ด้วยเทคโนโลยีปัญญาประดิษฐ์</span></h1>
        <p class="subtitle">
            โครงงานพัฒนาระบบแนะนำกำหนดการเดินทางและจัดสรรงบประมาณส่วนบุคคลโดยใช้ระบบวิเคราะห์ข้อมูลจำลอง เพื่อช่วยลดขั้นตอนและเพิ่มประสิทธิภาพในการออกแบบแผนการท่องเที่ยว
        </p>

        <!-- CREDENTIALS -->
        <div class="credentials-card">
            <div class="credentials-title">ผู้รับผิดชอบโครงงาน</div>
            <div class="credentials-grid">
                <div class="credentials-label">ผู้เสนอโครงงาน:</div>
                <div class="credentials-value">[นาย ณภัทร ภักดีพันธ์]</div>

                <div class="credentials-label">รหัสนักศึกษา:</div>
                <div class="credentials-value">[6906032610552]</div>

                <div class="credentials-label">หลักสูตร/สาขา:</div>
                <div class="credentials-value">คอมพิวเตอร์ช่วยออกเเบบเเละบริหารงานก่อสร้าง</div>

                <div class="credentials-label">เสนออาจารย์:</div>
                <div class="credentials-value">[อาจารย์ ดร.ณัฎฐพล เสาวนะ ]</div>
            </div>
        </div>
    </header>

    <div class="container">
        <!-- PRESENTATION SLIDES SECTION -->
        <section class="section-title">
            <h2>📊 สรุปภาพรวมโครงงาน</h2>
            <p>สไลด์สรุปประเด็นสำคัญสำหรับใช้นำเสนอต่อหน้าชั้นเรียน</p>
        </section>

        <div class="slides-container">
            <!-- Slide 1 -->
            <div class="slide-card">
                <span class="slide-num">SLIDE 01</span>
                <h3>ที่มาและความสำคัญ</h3>
                <ul>
                    <li>ปัญหาการวางแผนเที่ยวที่ใช้เวลานาน</li>
                    <li>ความยุ่งยากในการคำนวณงบประมาณ</li>
                    <li>การใช้ AI เข้ามาช่วยวิเคราะห์และจัดลำดับสถานที่</li>
                </ul>
            </div>

            <!-- Slide 2 -->
            <div class="slide-card">
                <span class="slide-num">SLIDE 02</span>
                <h3>วัตถุประสงค์</h3>
                <ul>
                    <li>พัฒนาระบบแนะนำเส้นทางท่องเที่ยวอัตโนมัติ</li>
                    <li>ช่วยบริหารจัดการงบประมาณของผู้ใช้</li>
                    <li>เพิ่มความสะดวกและรวดเร็วในการวางแผน</li>
                </ul>
            </div>

            <!-- Slide 3 -->
            <div class="slide-card">
                <span class="slide-num">SLIDE 03</span>
                <h3>เทคโนโลยีที่ใช้</h3>
                <ul>
                    <li>Python & Streamlit (Web Application)</li>
                    <li>Machine Learning / AI API</li>
                    <li>HTML5 / CSS3 Custom Styling</li>
                </ul>
            </div>
        </div>
    </div>

</body>
</html>
"""

# 3. สั่งแสดงผล HTML ผ่าน Streamlit
components.html(html_content, height=1200, scrolling=True)
