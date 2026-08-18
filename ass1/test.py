import hashlib

# 1. ปรับ Dictionary ตามที่โจทย์แนะนำเป๊ะๆ (ตัวเล็ก, ตัวใหญ่, ตัวเลข)
num_to_char = {
    'o': ['o', 'O', '0'],
    'l': ['l', 'L', '1'],
    'i': ['i', 'I', '1']
}

target =  "d54cc1fe76f5186380a0939d2fc1723c44e8a5f7."

def recursive(word, start, stop):
    if start == stop:
        result_str = "".join(word)
        hash_val = hashlib.sha1(result_str.encode('utf-8')).hexdigest()
        
        if hash_val == target:
            return result_str
        else:
            return ""
            
    org = word[start]
    low = org.lower()
    
    # 2. เงื่อนไขการแปลงตัวอักษร
    if low in num_to_char:
        l = num_to_char[low] # ถ้าตรงกับ o, l, i ให้ใช้จาก Dict
    elif low.isalpha():
        l = [low, org.upper()] # ถ้าเป็นตัวอักษรปกติ ให้มีแค่ เล็ก/ใหญ่
    else:
        l = [org] # ถ้าเป็นอักขระพิเศษ (เช่น ตัวเลขที่มีอยู่แล้ว หรือสัญลักษณ์) ให้คงเดิม
        
    for c in l:
        word[start] = c
        result = recursive(word, start+1, stop)
        if result != "":
            return result
            
    word[start] = org # Backtracking
    return ""

# 3. เพิ่มฟังก์ชันสำหรับอ่าน "List of words"
def crack_password(wordlist_path):
    print("Starting dictionary attack...")
    
    # สมมติว่าเราอ่านจากไฟล์ wordlist.txt
    try:
        with open(wordlist_path, 'r', encoding='utf-8') as file:
            for line in file:
                # ตัดช่องว่างและ \n ออกจากคำ
                base_word = line.strip() 
                
                # แปลง string เป็น list เพื่อให้เข้ากับฟังก์ชัน recursive ของคุณ
                word_list = list(base_word) 
                
                # เรียกใช้ฟังก์ชัน
                result = recursive(word_list, 0, len(word_list))
                
                if result:
                    print(f"[+] Password Found! The password is: {result}")
                    return result
                    
        print("[-] Password not found in the list.")
    except FileNotFoundError:
        print(f"Error: Could not find the file {wordlist_path}")

# เรียกใช้งาน
crack_password("10k-most-common.txt")