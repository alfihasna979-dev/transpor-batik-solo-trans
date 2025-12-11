# Data pertanyaan dan jawaban (kamus)
data = {
    "jadwal bus trans solo": "Bus Trans Solo beroperasi mulai pukul 05.30 WIB sampai 21.00 WIB untuk semua koridor utama.",
    "jam berapa bst berangkat": "Bus BST mulai beroperasi pukul 05.30 WIB setiap hari.",
    "jadwal keberangkatan bst koridor 1": "Koridor 1 BST beroperasi dari pukul 05.30 hingga 21.00, dengan keberangkatan setiap 10–15 menit.",
    "jadwal keberangkatan bst koridor 2": "Koridor 2 BST beroperasi pukul 05.30–21.00 dengan interval sekitar 15 menit.",
    "jadwal keberangkatan bst koridor 3": "Koridor 3 beroperasi mulai 05.30 dengan interval 10–20 menit hingga 20.30–21.00.",
    "berapa menit sekali bst lewat": "BST biasanya lewat setiap 10–15 menit pada jam normal, dan bisa menjadi 20 menit pada malam hari."
}

print("Chatbot Informasi Batik Solo Trans (BST)")
print("Ketik 'exit' untuk keluar")

while True:
    user = input("Anda: ").lower()

    if user == "exit":
        print("Terima kasih telah menggunakan chatbot BST!")
        break

    if user in data:
        print("Bot:", data[user])
    else:
        print("Bot: Maaf, saya belum paham pertanyaan Anda. Coba gunakan kata kunci seperti 'jadwal keberangkatan bst koridor 1'.")
