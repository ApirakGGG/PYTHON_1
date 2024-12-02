# //import lib
from fpdf import FPDF as fpdf

# สร้างตัวอย่าง PDF
pdf = fpdf()
pdf.set_auto_page_break(auto=True, margin=10)
pdf.add_page()

# เพิ่มฟอนต์ภาษาไทย
    # ใช้ raw string โดยการเติมตัว r ข้างหน้า ป้องกันError
pdf.add_font('Sarabun-Bold', '', r'D:\convret_pdf\font\Sarabun-Bold.ttf', uni=True)
pdf.set_font('Sarabun-Bold', size=10)  # กำหนดฟอนต์และขนาด

# เนื้อหา ที่จะ convert to pdf
content = """
คำถามสัมภาษณ์งานสำหรับ React Developer พร้อมคำตอบ

1. React คืออะไร และมีประโยชน์อย่างไร?
   - React เป็น JavaScript library ที่ใช้สำหรับสร้าง UI โดยเฉพาะ การออกแบบ React มีพื้นฐานเป็น component-based 
     ทำให้โค้ดสามารถ reuse ได้ง่าย และมีการจัดการ state ที่มีประสิทธิภาพ  
     ประโยชน์:
     - มีประสิทธิภาพสูงด้วย Virtual DOM
     - ใช้ reusable components เพื่อลดการเขียนโค้ดซ้ำ
     - มีชุมชนที่ใหญ่และ ecosystem ที่แข็งแกร่ง

2. อธิบายความแตกต่างระหว่าง Class Component กับ Function Component
   - Class Component: ใช้ class และมี lifecycle methods เช่น componentDidMount, componentDidUpdate
     ตัวอย่าง:
     class MyComponent extends React.Component {
       render() {
         return <h1>Hello, Class Component</h1>;
       }
     }
   - Function Component: เป็นฟังก์ชันธรรมดาที่รองรับ Hooks เช่น useState, useEffect
     ตัวอย่าง:
     function MyComponent() {
       return <h1>Hello, Function Component</h1>;
     }

     Function Component ได้รับความนิยมมากขึ้นเพราะเขียนโค้ดง่ายกว่าและรองรับ Hooks

3. React Lifecycle Methods คืออะไร?
   - Lifecycle methods เป็นฟังก์ชันที่ React เรียกใช้งานในช่วงต่าง ๆ ของอายุการใช้งาน component:
     - Mounting: เช่น componentDidMount (เมื่อ component ถูกสร้างเสร็จ)
     - Updating: เช่น componentDidUpdate (เมื่อ props หรือ state เปลี่ยน)
     - Unmounting: เช่น componentWillUnmount (เมื่อ component ถูกลบออก)
     สำหรับ Function Component สามารถใช้ Hooks อย่าง useEffect แทน lifecycle methods ได้

4. Virtual DOM คืออะไร? ทำงานอย่างไร?
   - Virtual DOM คือการจำลอง DOM จริงในรูปแบบ JavaScript object การอัปเดต DOM จะทำบน Virtual DOM ก่อนเปรียบเทียบ 
     (diffing) กับ DOM จริงเพื่อลดการอัปเดตที่ไม่จำเป็น

5. State กับ Props ต่างกันอย่างไร?
   - State: ใช้จัดเก็บข้อมูลภายใน component และสามารถเปลี่ยนแปลงได้
   - Props: ข้อมูลที่ส่งจาก parent component มายัง child component และไม่สามารถแก้ไขได้ใน child component

6. Hooks ที่ใช้บ่อยมีอะไรบ้าง และใช้งานอย่างไร?
   - useState: จัดการ state
   - useEffect: จัดการ side effects
   - useContext: ใช้ context API เพื่อแชร์ข้อมูลระหว่าง component

7. อธิบายเกี่ยวกับ Context API
   - Context API ใช้สำหรับแชร์ข้อมูลระหว่าง components โดยไม่ต้องใช้ props drilling

8. Redux คืออะไร? และใช้ทำอะไรใน React?
   - Redux เป็น state management library ที่ช่วยจัดการ state ของแอปพลิเคชันในรูปแบบ global state 
     ทำให้สามารถแชร์ข้อมูลระหว่าง components ได้ง่ายขึ้น

9. การจัดการฟอร์มใน React ทำได้อย่างไร?
   - ใช้ state เพื่อเก็บค่าของ input และจัดการฟังก์ชันการส่งฟอร์ม

10. คุณจะเพิ่มประสิทธิภาพ (Performance) ใน React ได้อย่างไร?
    - ใช้ React.memo เพื่อป้องกันการ re-render ที่ไม่จำเป็น
    - ใช้ useMemo และ useCallback เพื่อบันทึกค่าที่คำนวณไว้ล่วงหน้า
    - แบ่ง component ออกเป็นชิ้นเล็ก ๆ
    - ใช้ lazy loading สำหรับโหลด component ที่ต้องใช้จริง ๆ
"""
for line in content.split("\n"):
    pdf.cell(0, 10 , line, ln=True) # เพิ่มข้อความทีละบรรทัด

# Save to PDF
    # ใช้ raw string โดยการเติมตัว r ข้างหน้า
file_path = r"D:\convret_pdf\React_Interview_Questions.pdf" 
pdf.output(file_path)
print(f"PDF ถูกบันทึกไว้ที่ {file_path}")