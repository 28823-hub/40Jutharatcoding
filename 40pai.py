import sqlite3
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler

# ================= 1. DATABASE SETUP =================
def init_db():
    conn = sqlite3.connect('lms_simple.db')
    cursor = conn.cursor()
    
    # ตารางผู้ใช้งาน
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    ''')
    
    # ตารางคอร์สเรียน
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            instructor TEXT NOT NULL
        )
    ''')
    
    # เพิ่มข้อมูลตัวอย่าง (ถ้าตารางยังว่าง)
    cursor.execute("SELECT COUNT(*) FROM courses")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO courses (title, description, instructor) VALUES (?, ?, ?)",
                       ("Python for Beginners", "ปูพื้นฐานการเขียนโปรแกรมด้วยภาษา Python", "Teacher Admin"))
        cursor.execute("INSERT INTO courses (title, description, instructor) VALUES (?, ?, ?)",
                       ("Web Development 101", "เรียนรู้การสร้างเว็บไซต์ด้วย HTML และ CSS", "Teacher Admin"))
    
    conn.commit()
    conn.close()

# ================= 2. WEB SERVER HANDLER =================
class RequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        # ดึงข้อมูลคอร์สเรียนทั้งหมดจาก Database
        conn = sqlite3.connect('lms_simple.db')
        cursor = conn.cursor()
        cursor.execute("SELECT title, description, instructor FROM courses")
        courses = cursor.fetchall()
        conn.close()

        # สร้างรายการคอร์สแบบ HTML
        courses_html = ""
        for course in courses:
            courses_html += f"""
            <div style="border: 1px solid #ccc; padding: 15px; margin-bottom: 10px; border-radius: 8px; background: #fff;">
                <h3 style="margin-top:0; color:#0056b3;">{course[0]}</h3>
                <p><b>ผู้สอน:</b> {course[2]}</p>
                <p>{course[1]}</p>
            </div>
            """

        # HTML หน้าเว็บหลัก
        html_content = f"""
        <!DOCTYPE html>
        <html lang="th">
        <head>
            <meta charset="UTF-8">
            <title>ระบบจัดการการเรียนการสอน (LMS)</title>
            <style>
                body {{ font-family: Arial, sans-serif; background-color: #f4f6f9; margin: 0; padding: 20px; }}
                .container {{ max-width: 800px; margin: auto; }}
                .card {{ background: white; padding: 20px; border-radius: 8px; margin-bottom: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
                input, textarea {{ width: 100%; padding: 8px; margin: 5px 0 15px 0; box-sizing: border-box; border: 1px solid #ccc; border-radius: 4px; }}
                button {{ background-color: #28a745; color: white; padding: 10px 15px; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; }}
                button:hover {{ background-color: #218838; }}
                h2 {{ border-bottom: 2px solid #0056b3; padding-bottom: 5px; color: #333; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1 style="text-align: center; color: #0056b3;">ระบบจัดการการเรียนการสอน (LMS)</h1>
                
                <!-- ฟอร์มสร้างคอร์สใหม่ -->
                <div class="card">
                    <h2>+ เพิ่มคอร์สเรียนใหม่ (สำหรับผู้สอน)</h2>
                    <form action="/add_course" method="POST">
                        <label>ชื่อคอร์สเรียน:</label>
                        <input type="text" name="title" required>
                        
                        <label>ชื่อผู้สอน:</label>
                        <input type="text" name="instructor" required>
                        
                        <label>รายละเอียดวิชา:</label>
                        <textarea name="description" rows="3" required></textarea>
                        
                        <button type="submit">บันทึกคอร์สเรียน</button>
                    </form>
                </div>

                <!-- รายการคอร์สที่มี -->
                <div class="card">
                    <h2>คอร์สเรียนทั้งหมดในระบบ</h2>
                    {courses_html}
                </div>
            </div>
        </body>
        </html>
        """
        self.wfile.write(html_content.encode('utf-8'))

    def do_POST(self):
        # รองรับการส่งข้อมูลฟอร์มเพิ่มคอร์สเรียน
        if self.path == '/add_course':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            parsed_data = urllib.parse.parse_qs(post_data)

            title = parsed_data.get('title', [''])[0]
            instructor = parsed_data.get('instructor', [''])[0]
            description = parsed_data.get('description', [''])[0]

            # บันทึกลง SQLite
            if title and instructor:
                conn = sqlite3.connect('lms_simple.db')
                cursor = conn.cursor()
                cursor.execute("INSERT INTO courses (title, description, instructor) VALUES (?, ?, ?)",
                               (title, description, instructor))
                conn.commit()
                conn.close()

            # ส่งกลับหน้าหลัก
            self.send_response(303)
            self.send_header('Location', '/')
            self.end_headers()

# ================= 3. RUN SERVER =================
if __name__ == '__main__':
    init_db()
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print("==================================================")
    print("เซิร์ฟเวอร์เปิดใช้งานสำเร็จ!")
    print("เปิดเว็บเบราว์เซอร์แล้วเข้าไปที่: http://localhost:8000")
    print("กด Ctrl+C เพื่อเลิกรันโปรแกรม")
    print("==================================================")
    httpd.serve_forever()