"""
Ciphertext Decryption Helper
Allows defining a mapping string from cipher characters/words to English plaintext.
Characters not in the mapping dictionary are displayed as '_'.
"""

TARGET = "PRCSOFQX FP QDR AFOPQ CZSPR LA JFPALOQSKR. QDFP FP ZK LIU BROJZK MOLTROE."

# กำหนด Mapping ในรูปแบบ String ได้อย่างอิสระ:
# รองรับทั้งแบบคู่คำ (เช่น "FP:IS, QDR:THE") หรือคู่ตัวอักษร (เช่น "P:S, R:E")
# สามารถคั่นด้วย comma หรือ space และใช้เครื่องหมาย ':', '->', หรือ '=' ได้
# ตัวอย่างด้านล่างเป็นการ Map ตัวอย่างคำ 2-3 ตัวอักษรที่เดาได้ง่ายก่อน:
MAPPING_STR = """
    C:c, S:u, O:r, X:y, Q:t, D:h, F:i, P:s, R:e, A:f, Z:a, L:o, J:m, K:n, B:g, I:l, U:d
"""

# หากต้องการถอดรหัสทั้งหมด สามารถใช้ Full Mapping ด้านล่างนี้ได้:
# MAPPING_STR = "FP:IS, QDR:THE, LA:OF, ZK:AN, LIU:OLD, BROJZK:GERMAN, MOLTROE:PROVERB, CZSPR:CAUSE, AFOPQ:FIRST, PRCSOFQX:SECURITY, JFPALOQSKR:MISFORTUNE"


def parse_mapping_string(mapping_str: str) -> dict[str, str]:
    """
    แปลง mapping string ให้อยู่ในรูป dictionary {cipher_char: plain_char}
    รองรับการระบุทั้งแบบคำ (เช่น 'QDR:THE') และแบบตัวอักษรเดี่ยว (เช่น 'P:S')
    """
    mapping = {}
    # ปรับ normalize ตัวคั่นให้อ่านง่าย
    normalized = mapping_str.replace(",", " ").replace("\n", " ")
    tokens = [t.strip() for t in normalized.split() if t.strip()]

    for token in tokens:
        delimiter = None
        for sep in [":", "->", "="]:
            if sep in token:
                delimiter = sep
                break

        if not delimiter:
            continue

        parts = token.split(delimiter)
        if len(parts) != 2:
            continue

        cipher_part, plain_part = parts[0].strip().upper(), parts[1].strip().upper()

        if len(cipher_part) != len(plain_part):
            print(f"[Warning] ความยาวของ '{cipher_part}' และ '{plain_part}' ไม่เท่ากัน ข้ามคู่นี้")
            continue

        for c_char, p_char in zip(cipher_part, plain_part):
            if c_char in mapping and mapping[c_char] != p_char:
                print(f"[Warning] ตรวจพบตัวอักษรขัดแย้ง: {c_char} แมปกับ {mapping[c_char]} อยู่แล้ว แต่พยายามแมปกับ {p_char}")
            else:
                mapping[c_char] = p_char

    return mapping


def decrypt_partial(target: str, mapping: dict[str, str]) -> str:
    """
    ถอดรหัส target ตาม mapping
    - ตัวอักษรภาษาอังกฤษที่ไม่อยู่ใน mapping จะแสดงผลเป็น '_'
    - เครื่องหมายวรรคตอนและช่องว่างจะคงไว้ตามเดิม
    """
    result = []
    for char in target:
        if char.isalpha():
            upper_char = char.upper()
            if upper_char in mapping:
                plain_char = mapping[upper_char]
                result.append(plain_char if char.isupper() else plain_char.lower())
            else:
                result.append("_")
        else:
            result.append(char)
    return "".join(result)


def main():
    mapping = parse_mapping_string(MAPPING_STR)

    print("=" * 70)
    print("CIPHERTEXT:")
    print(TARGET)
    print("=" * 70)

    print(f"\nCURRENT MAPPING ({len(mapping)} letters):")
    sorted_map = sorted(mapping.items())
    print(", ".join(f"{c}->{p}" for c, p in sorted_map) if sorted_map else "No mapping provided")

    decrypted = decrypt_partial(TARGET, mapping)
    print("\nDECRYPTED RESULT (Unknown letters shown as '_'):")
    print(decrypted)

    # ตรวจสอบตัวอักษร Cipher ที่ยังไม่ได้ถูก Map
    target_alpha = {c.upper() for c in TARGET if c.isalpha()}
    unmapped = sorted(list(target_alpha - set(mapping.keys())))
    print("\n" + "=" * 70)
    print(f"UNMAPPED CIPHER LETTERS ({len(unmapped)} remaining):")
    print(", ".join(unmapped) if unmapped else "All letters have been mapped!")
    print("=" * 70)


if __name__ == "__main__":
    main()
