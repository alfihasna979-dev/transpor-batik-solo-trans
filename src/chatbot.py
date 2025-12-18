!pip install colorama
# Import library untuk warna di terminal
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

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
    "keunggulan bst": "Nyaman, aman, cepat, tarif terjangkau.",
    "dimana bisa beli tiket": "Loket halte atau aplikasi digital.",
    "apakah ada jalur khusus": "Ya.",
    "siapa yang dapat fasilitas prioritas": "Lansia, disabilitas, ibu hamil, anak kecil.",
    "jam operasional": "Sekitar 05.00–21.00.",
    "apakah bus ini ramah lingkungan": "Ya, menggunakan bahan bakar bersih.",
    "harga tiket bst": "Rp 3.500–5.000 (sesuai rute).",
    "diskon untuk siapa": "Lansia, pelajar, disabilitas.",
    "cara top up kartu bst": "Lewat loket atau aplikasi digital.",
    "tarif koridor 1 sama koridor 2": "Sama, flat rate.",
    "bisa pakai qris": "Ya, di beberapa halte.",
    "apakah ada biaya tambahan bagasi": "Tidak."
}

# Tampilan pembuka
print(Fore.CYAN + "="*60)
print(Fore.GREEN + Style.BRIGHT + "Chatbot Informasi Batik Solo Trans (BST)")
print(Fore.CYAN + "="*60)
print(Fore.YELLOW + "Semua warga Solo dapat menggunakan chatbot ini untuk melihat jadwal dan layanan BST.")
print("Gunakan huruf kecil semua contoh: 'berapa menit sekali bst lewat'")
print("Ketik 'exit' untuk keluar")
print(Fore.CYAN + "-"*60)

# Loop chatbot
while True:
    user = input(Fore.MAGENTA + "Anda: ").lower()

    if user == "exit":
        print(Fore.GREEN + "Terima kasih telah menggunakan chatbot BST!")
        break

    if user in data:
        print(Fore.BLUE + Style.BRIGHT + "Bot: " + Style.NORMAL + data[user])
    else:
        print(Fore.RED + "Bot: Maaf, saya belum paham pertanyaan Anda. " +
              "Coba gunakan kata kunci seperti 'jadwal keberangkatan bst koridor 1'.")
