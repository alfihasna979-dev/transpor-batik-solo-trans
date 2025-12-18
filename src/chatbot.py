# Data pertanyaan dan jawaban (kamus)
data = {
    "jadwal bus trans solo": "Bus Trans Solo beroperasi mulai pukul 05.30 WIB sampai 21.00 WIB untuk semua koridor utama.",
    "jam berapa bst berangkat": "Bus BST mulai beroperasi pukul 05.30 WIB setiap hari.",
    "jadwal keberangkatan bst koridor 1": "Koridor 1 BST beroperasi dari pukul 05.30 hingga 21.00, dengan keberangkatan setiap 10–15 menit.",
    "jadwal keberangkatan bst koridor 2": "Koridor 2 BST beroperasi pukul 05.30–21.00 dengan interval sekitar 15 menit.",
    "jadwal keberangkatan bst koridor 3": "Koridor 3 beroperasi mulai 05.30 dengan interval 10–20 menit hingga 20.30–21.00.",
    "berapa menit sekali bst lewat": "BST biasanya lewat setiap 10–15 menit pada jam normal dan bisa menjadi 20 menit pada malam hari.",
    "apa itu bst": "Bus Solo Trans adalah layanan angkutan umum berbasis bus rapid transit (BRT) di Kota Solo yang bertujuan memudahkan masyarakat dalam mobilitas.",
    "berapa jumlah koridor atau rute yang dimiliki bst": "Bus Solo Trans memiliki beberapa koridor/rute salah satunya Koridor 1 (terminal Purwosari – Terminal Banyuanyar).",
    "keunggulan bst": "Nyaman aman cepat tarif terjangkau.",
    "dimana bisa beli tiket": "Loket halte atau aplikasi digital.",
    "apakah ada jalur khusus": "Ya.",
    "siapa yang dapat fasilitas prioritas": "Lansia disabilitas ibu hamil anak kecil.",
    "jam operasional": "Sekitar 05.00–21.00.",
    "apakah bus ini ramah lingkungan": "Ya menggunakan bahan bakar bersih."
   
}

print("Chatbot Informasi Batik Solo Trans (BST)")
print("semua warga solo dapat menggunakan untuk melihat jadwal dan layanan bst")
print("gunakan huruf kecil semua contoh (berapa menit sekali bst lewat)")
print("selamat komunikasi dengan chatbot")
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
