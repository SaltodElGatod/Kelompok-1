def get_film_list(genre):
    film_list = {
        "action": [
            {"judul": "Avengers: Endgame", "harga": 20000, "waktu": "14:10", "tanggal": "2024-04-10", "ruangan": "Bioskop 1"},
            {"judul": "Inception", "harga": 18000, "waktu": "15:10", "tanggal": "2024-04-09", "ruangan": "Bioskop 3"},
            {"judul": "The Matrix", "harga": 15000, "waktu": "09:00", "tanggal": "2024-04-18", "ruangan": "Bioskop 5"},
            {"judul": "Spider-Man: Across the Spider-Verse", "waktu": "18:45", "harga": 30000, "tanggal": "2024-04-12", "ruangan": "Bioskop 1"},
            {"judul": "The Flash", "harga": 20000, "waktu": "15:20", "tanggal": "2024-04-14", "ruangan": "Bioskop 2"},
            {"judul": "Transformers: Rise of the Beasts", "waktu": "10:50", "harga": 19000, "tanggal": "2024-04-20", "ruangan": "Bioskop 4"},
            {"judul": "Jhon Wick: Chapter 4", "harga": 15000, "waktu": "12:15", "tanggal": "2024-04-16", "ruangan": "Bioskop 5"},
            {"judul": "Guardian of the Galaxy", "harga": 18000, "waktu": "13:00", "tanggal": "2024-04-10", "ruangan": "Bioskop 6"},
        ],
        "horror": [
            {"judul": "Pemandi Jenazah", "harga": 20000, "waktu": "21:35", "tanggal": "2024-04-08", "ruangan": "Bioskop 2"},
            {"judul": "Sijjin", "harga": 15000, "waktu": "19:55", "tanggal": "2024-04-08", "ruangan": "Bioskop 5"},
            {"judul": "Valak", "harga": 17000, "waktu": "17:20", "tanggal": "2024-04-19", "ruangan": "Bioskop 1"},
            {"judul": "Suzzanna: Malam Jumat Kliwon", "waktu": "20:45", "harga": 30000, "tanggal": "2024-04-13", "ruangan": "Bioskop 4"},
            {"judul": "Waktu Maghrib", "harga": 23000, "waktu": "22:35", "tanggal": "2024-04-24", "ruangan": "Bioskop 3"},
            {"judul": "The Nun II", "harga": 16000, "waktu": "18:00", "tanggal": "2024-04-11", "ruangan": "Bioskop 6"},
            {"judul": "Sewo Dino", "harga": 22000, "waktu": "21:20", "tanggal": "2024-04-20", "ruangan": "Bioskop 2"},
            {"judul": "Kultus Iblis", "harga": 25000, "waktu": "20:00", "tanggal": "2024-04-14", "ruangan": "Bioskop 1"},
        ],
        "komedi": [
            {"judul": "Onde Mande!", "harga": 20000, "waktu": "09:00", "tanggal": "2024-04-15", "ruangan": "Bioskop 1"},
            {"judul": "Jangkrik Bos (DKI)", "harga": 19000, "waktu": "13:20", "tanggal": "2024-04-19", "ruangan": "Bioskop 4"},
            {"judul": "Hangout", "harga": 15000, "waktu": "10:50", "tanggal": "2024-04-07", "ruangan": "Bioskop 5"},
            {"judul": "Jin & Jun (2023)", "harga": 20000, "waktu": "11:45", "tanggal": "2024-04-15", "ruangan": "Bioskop 2"},
            {"judul": "Star Syndrome", "harga": 15000, "waktu": "11:20", "tanggal": "2024-04-16", "ruangan": "Bioskop 3"},
            {"judul": "Ngeri - Ngeri Sedap", "harga": 19000, "waktu": "14:20", "tanggal": "2024-04-08", "ruangan": "Bioskop 6"},
            {"judul": "Ganjil Genap", "harga": 20000, "waktu": "13:00", "tanggal": "2024-04-16", "ruangan": "Bioskop 1"},
            {"judul": "Kejar Mimpi, Gaspol!", "harga": 25000, "waktu": "17:15", "tanggal": "2024-04-21", "ruangan": "Bioskop 5"},
            {"judul": "Agak Laen", "harga": 25000, "waktu": "11:35", "tanggal": "2024-04-20", "ruangan": "Bioskop 2"},
        ],
    }
    return film_list.get(genre, [])

def get_film_info(film):
    return f"{film['judul']} - Rp{film['harga']} - Waktu : {film['waktu']} - Tanggal : {film['tanggal']} - Ruangan : {film['ruangan']}"

def main():
    while True:
        print("""
===============================================
=============== BIOSKOP CIHUY =================
===============================================
1. Action
2. Horror
3. Komedi""")
        print("===============================================")
        genre = input("Masukkan angka dari 1, 2, atau 3 untuk memilih genre yang ingin ditonton: ")

        if genre not in ['1', '2', '3']:
            print("Maaf, pilihan yang Anda masukkan tidak valid.")
            continue

        genre_map = {'1': 'action', '2': 'horror', '3': 'komedi'}
        genre = genre_map[genre]
        film_list = get_film_list(genre)

        if not film_list:
            print("Maaf, genre yang Anda pilih tidak tersedia.")
            continue

        pesan_lagi_genre = True
        while pesan_lagi_genre:
            for i, film in enumerate(film_list):
                print(f"{i+1}. {get_film_info(film)}")
                print("===============================================")
            choice = int(input("Pilih film dengan angka yang sesuai: ")) - 1

            film = film_list[choice]

            print("Detail Pemesanan:")
            print("Film       : " + film['judul'])
            print("Harga      : Rp" + str(film['harga']))
            print("Waktu      : " + film['waktu'])
            print("Tanggal    : " + film['tanggal'])
            print("Ruangan    : " + film['ruangan'])

            while True:
                jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin dipesan: "))
                total_harga = film['harga'] * jumlah_tiket
                print(f"Total Harga : Rp{total_harga}")

                yakin = input("Yakin membeli tiket ini? (ya/tidak): ")
                print("===============================================")
                if yakin.lower() == "ya":
                    break
                elif yakin.lower() == "tidak":
                    pesan_lagi_genre = False
                    break
                else:
                    continue

            if yakin.lower() == "tidak":
                break

            pembayaran = float(input("Konfirmasi pembayaran : "))

            if pembayaran < total_harga:
                print("Maaf, jumlah pembayaran yang Anda masukkan tidak cukup.")
                kembali = input("Apakah Anda ingin kembali? (ya/tidak): ")
                if kembali.lower() == "ya":
                    continue
                else:
                    break

            print("Pembayaran berhasil. Terima kasih atas pemesanan Anda.")

            ulangi = input("Apakah Anda ingin memesan lagi? (ya/tidak): ")
            if ulangi.lower() != "ya":
                pesan_lagi_genre = False
                continue

        ulangi_genre = input("Apakah Anda ingin memilih genre lain? (ya/tidak): ")
        if ulangi_genre.lower() != "ya":
            break

    print("Terima kasih telah melakukan pemesanan tiket di Bioskop Cihuy ('3')!!!.")

if __name__ == "__main__":
    main()