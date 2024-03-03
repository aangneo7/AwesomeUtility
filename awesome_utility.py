def convert_to_uppercase(text):
    return text.upper()

def convert_to_lowercase(text):
    return text.lower()

if __name__ == "__main__":
    input_text = input("Masukkan teks: ")
    print("Teks Kapital:", convert_to_uppercase(input_text))
    print("Teks Kecil:", convert_to_lowercase(input_text))
