# Caesar Cipher Brute Force with Dictionary Validation (Exercise 1.d)

# 1. พจนานุกรมคำศัพท์ภาษาอังกฤษที่พบบ่อย สำหรับใช้ตรวจผลลัพธ์
DICTIONARY = {
    "THE", "BE", "TO", "OF", "AND", "A", "IN", "THAT", "HAVE", "I",
    "IT", "FOR", "NOT", "ON", "WITH", "HE", "AS", "YOU", "DO", "AT",
    "THIS", "BUT", "HIS", "BY", "FROM", "THEY", "WE", "SAY", "HER",
    "SHE", "OR", "AN", "WILL", "MY", "ONE", "ALL", "WOULD", "THERE",
    "THEIR", "WHAT", "SO", "UP", "OUT", "IF", "ABOUT", "WHO", "GET",
    "WHICH", "GO", "ME", "IS", "HELLO", "WORLD", "SECRET", "SECURITY"
}


# 2. ฟังก์ชันถอดรหัส Caesar สำหรับ 1 ค่า Shift
def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # หาจุดเริ่มต้น ('A' หรือ 'a')
            base = ord('A') if char.isupper() else ord('a')
            # เลื่อนตัวอักษรถอยหลังตาม shift
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result


# 3. ฟังก์ชันหลักสำหรับ Brute Force หาค่า Shift
def crack_caesar(ciphertext):
    print(f"Ciphertext: {ciphertext}\n")
    print("--- Testing all 26 possible shifts ---")

    best_shift = 0
    best_text = ""
    max_matches = -1

    for shift in range(26):
        plain = decrypt(ciphertext, shift)

        # ตัดคำและลบเครื่องหมายวรรคตอนรอบๆ ออก
        words = [w.strip(".,!?\"'") for w in plain.upper().split()]

        # นับว่ามีคำที่ตรงกับ Dictionary กี่คำ
        matches = sum(1 for w in words if w in DICTIONARY)

        print(f"Shift {shift:2d} (Matched {matches:2d} words): {plain}")

        # เก็บคำตอบที่พบคำภาษาอังกฤษมากที่สุด
        if matches > max_matches:
            max_matches = matches
            best_shift = shift
            best_text = plain

    print("\n" + "=" * 50)
    print(f"Best Result: Shift {best_shift} (Matched {max_matches} English words)")
    print(f"Decrypted Text: {best_text}")
    print("=" * 50)


# 4. ทดสอบโปรแกรม
if __name__ == "__main__":
    # ตัวอย่างข้อความที่เข้ารหัสด้วย Caesar Cipher (Shift = 3)
    sample_ciphertext = "PRCSOFQX FP QDR AFOPQ CZSPR LA JFPALOQSKR. QDFP FP ZK LIU BROJZK MOLTROE."
    crack_caesar(sample_ciphertext)
