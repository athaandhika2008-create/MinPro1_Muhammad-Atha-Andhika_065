print(">>>>>>>>>>GAMECLOUD<<<<<<<<<<")
print("!Tempat Dimana Anda Memainkan Game Tanpa Harus Membeli Langsung Atau Membayar Mahal!")

print("\nSilahkan Registrasi Terlebih Dahulu!")
admin_username = input("Buat Username Admin Anda: ")
admin_password = input("Buat Password Admin Anda: ")
print("Akun Admin Berhasil Dibuat!")

print("\nSilahkan Login untuk Masuk ke GameCloud!")
print("Mohon Memasukan Username dan Password yang telah Anda Buat!")

while True:
    username = input("Masukan Username Anda: ")
    password = input("Masukan Password Anda: ")

    if username == admin_username and password == admin_password:
        print(f"\nLogin berhasil, anda adalah admin! Selamat datang di GameCloud {username}!")
        break
    else:
        print("\nUsername atau Password anda salah. Silahkan coba lagi!")

daftar_gamesewa = (
    "Grand Theft Auto 7 (GTA 7)",
    "Red Dead Redemption 3",
    "Resident Evil Veronica",
    "Forza Horizon 9",
    "EA SPORTS FC 29",
    "NBA 2K29 Special Edition",
    "God of War Laufey",
    "Assassin's Creed 9",
    "Marvel's Wolverine",
    "Final Fantasy VII"
)
data_penyewaan = []

while True:
    print("\n-MENU ADMIN GAMECLOUD: ")
    print("1. Tambah data penyewaan")
    print("2. Lihat data penyewaan")
    print("3. Ubah data penyewaan")
    print("4. Ubah status pembayaran")
    print("5. Perpanjang durasi sewa")
    print("6. Cari data penyewa")
    print("7. Hapus data penyewa")
    print("8. Kelola game penyewa")
    print("9. Selesai")

    menu = input("Pilih menu (1-9): ")
    if menu == "1":

        print("\n-TAMBAH DATA PENYEWA")
        nama = input("Masukan nama penyewa: ")

        while nama.strip() == "":
            print("Nama tidak boleh kosong!")
            nama = input("Masukan nama penyewa: ")

        daftar_game_penyewa = []
        total_harga = 0

        while True:
            print("\n-DAFTAR GAME GAMECLOUD")
            for i in range(len(daftar_gamesewa)):
                print(f"{i+1}. {daftar_gamesewa[i]}")

            nomor = input("Pilih nomor game yang ingin disewa: ")

            if nomor.isdigit() == False:
                print("Masukan nomor yang valid!")
                continue

            nomor = int(nomor)

            if nomor >= 1 and nomor <= len(daftar_gamesewa):

                print("\n-DURASI PENYEWAAN")
                print("1. Per hari (10.000)")
                print("2. Per minggu (60.000)")
                print("3. Per bulan (180.000)")

                durasi = input("Pilih durasi: ")

                if durasi == "1":
                    lama_sewa = "1 Hari"
                    harga = 10000

                elif durasi == "2":
                    lama_sewa = "1 Minggu"
                    harga = 60000

                elif durasi == "3":
                    lama_sewa = "1 Bulan"
                    harga = 180000

                else:
                    print("Pilihan durasi tidak valid!")
                    continue

                daftar_game_penyewa.append(
                    (daftar_gamesewa[nomor-1], lama_sewa, harga)
                )

                total_harga += harga

                print("\nGame berhasil ditambahkan!")
                print("Game   :", daftar_gamesewa[nomor-1])
                print("Durasi :", lama_sewa)
                print("Harga  : Rp", harga)

                lagi = input("\nApakah anda ingin menambahkan game lagi? (ya/tidak): ")
                if lagi.lower() == "tidak":
                    break
                elif lagi.lower() == "ya":
                    continue
                else:
                    print("Jawaban tidak valid, kembali ke daftar game!")
            else:
                print("Nomor game tidak tersedia!")

        status = "Belum Dibayar"

        data_penyewaan.append(
            (nama, daftar_game_penyewa, total_harga, status)
        )

        print("\n-DATA BERHASIL DITAMBAHKAN")
        print("Nama Penyewa: ", nama)
        print("\n-Daftar game yang disewa: ")
        for i in range(len(daftar_game_penyewa)):
            print(f"{i+1}. {daftar_game_penyewa[i][0]}")
            print(f"  Durasi: {daftar_game_penyewa[i][1]}")
            print(f"  Harga: Rp{daftar_game_penyewa[i][2]}")

        print("\nTotal Biaya: Rp", total_harga)
        print("Status Bayar:", status)

        input("\nTekan enter untuk kembali ke menu!")

    elif menu == "2":
        print("\n-DATA PENYEWA")
        if len(data_penyewaan) == 0:
            print("Belum ada data penyewaan!")
        else:
            for i in range(len(data_penyewaan)):
                print(f"\n-Penyewa {i+1}")
                print("Nama Penyewa: ", data_penyewaan[i][0])

                print("-Daftar Game: ")
                for j in range(len(data_penyewaan[i][1])):
                    print(f"{j+1}. {data_penyewaan[i][1][j][0]}")
                    print(f"   Durasi: {data_penyewaan[i][1][j][1]}")
                    print(f"   Harga : Rp{data_penyewaan[i][1][j][2]}")

                print("Total Biaya: Rp", data_penyewaan[i][2])
                print("Status Bayar: ", data_penyewaan[i][3])

        input("\nTekan enter untuk kembali ke menu!")

    elif menu == "3":
        if len(data_penyewaan) == 0:
            print("Belum ada data penyewaan!")

        else:
            print("\n-UBAH DATA PENYEWA")
            for i in range(len(data_penyewaan)):
                print(f"{i+1}. {data_penyewaan[i][0]}")

            pilih = int(input("Pilih nomor penyewa: "))
            if pilih < 1 or pilih > len(data_penyewaan):
                print("Nomor penyewa tidak valid!")
                input("\nTekan enter untuk kembali!")
                continue

            nama_baru = input("Nama penyewa baru: ")

            while nama_baru.strip() == "":
                print("Nama tidak boleh kosong!")
                nama_baru = input("Nama penyewa baru: ")

            daftar_game_penyewa = list(data_penyewaan[pilih-1][1])

            print("\n-Daftar Game yang Dimiliki Penyewa")
            for i in range(len(daftar_game_penyewa)):
                print(f"{i+1}. {daftar_game_penyewa[i][0]}")

            game_pilih = int(input("Pilih nomor game yang ingin diubah: "))
            if game_pilih < 1 or game_pilih > len(daftar_game_penyewa):
                print("Nomor game tidak tersedia!")
                input("\nTekan enter untuk kembali!")
                continue
            print("\n-Daftar Game Baru")
            for i in range(len(daftar_gamesewa)):
                print(f"{i+1}. {daftar_gamesewa[i]}")

            game_baru = int(input("Pilih nomor game baru: "))
            if game_baru < 1 or game_baru > len(daftar_gamesewa):
                print("Nomor game tidak tersedia!")
                input("\nTekan enter untuk melanjutkan!")
                continue

            game_lama = daftar_game_penyewa[game_pilih-1]

            daftar_game_penyewa[game_pilih-1] = (
                daftar_gamesewa[game_baru-1],
                game_lama[1],
                game_lama[2]
            )

            data_penyewaan[pilih-1] = (
                nama_baru,
                daftar_game_penyewa,
                data_penyewaan[pilih-1][2],
                data_penyewaan[pilih-1][3]
            )
            print("Data penyewaan berhasil diubah!")
        input("\nTekan enter untuk kembali!")

    elif menu == "4":
        if len(data_penyewaan) == 0:
            print("Belum ada data penyewaan!")

        else:
            print("\n-STATUS PEMBAYARAN")

            for i in range(len(data_penyewaan)):
                print(f"{i+1}. {data_penyewaan[i][0]} - {data_penyewaan[i][3]}")

            pilih = int(input("Pilih nomor penyewa: "))
            if pilih < 1 or pilih > len(data_penyewaan):
                print("Nomor penyewa tidak valid!")
                input("\nTekan enter untuk kembali!")
                continue
            print("\n1. Sudah Dibayar")
            print("2. Belum Dibayar")

            status = input("Pilih status: ")
            if status == "1":
                    bayar = "Sudah Dibayar"
            elif status == "2":
                    bayar = "Belum Dibayar"
            else:
                print("Pilihan status tidak valid!")
                input("\nTekan enter untuk kembali!")
                continue

            data_penyewaan[pilih-1] = (
                data_penyewaan[pilih-1][0],
                data_penyewaan[pilih-1][1],
                data_penyewaan[pilih-1][2],
                bayar
            )
            print("Status pembayaran berhasil diperbarui!")

        input("\nTekan enter untuk kembali!")

    elif menu == "5":
        if len(data_penyewaan) == 0:
            print("Belum ada data penyewaan!")

        else:
            print("\n-PERPANJANG DURASI PENYEWAAN")

            for i in range(len(data_penyewaan)):
                print(f"{i+1}. {data_penyewaan[i][0]}")

            pilih = int(input("Pilih nomor penyewa: "))
            if pilih < 1 or pilih > len(data_penyewaan):
                print("Nomor penyewa tidak valid!")
                input("\nTekan enter untuk kembali!")
                continue

            daftar_game_penyewa = list(data_penyewaan[pilih-1][1])
            total = data_penyewaan[pilih-1][2]

            print("\nDaftar game penyewa")
            for i in range(len(daftar_game_penyewa)):
                print(f"{i+1}. {daftar_game_penyewa[i][0]} ({daftar_game_penyewa[i][1]})")

            game_pilih = int(input("Pilih nomor game yang ingin diperpanjang: "))

            if game_pilih < 1 or game_pilih > len(daftar_game_penyewa):
                print("Nomor game tidak valid!")
                input("\nTekan enter untuk kembali!")
                continue

            game = list(daftar_game_penyewa[game_pilih-1])

            print("\nTambah Durasi? ")
            print("1. Tambah 1 hari")
            print("2. Tambah 1 minggu")
            print("3. Tambah 1 bulan")

            tambah = input("Pilih: ")

            if tambah == "1":
                if "Hari" in game[1]:
                    jumlah = int(game[1].split()[0]) + 1
                    game[1] = f"{jumlah} Hari"
                else:
                    game[1] = game[1] + " + 1 Hari"  

                game[2] += 10000
                total += 10000

            elif tambah == "2":
                if "Minggu" in game[1]:
                    jumlah = int(game[1].split()[0]) + 1
                    game[1] = f"{jumlah} Minggu"
                else:
                    game[1] = game[1] + " + 1 Minggu"

                game[2] += 60000
                total += 60000

            elif tambah == "3":
                if "Bulan" in game[1]:
                    jumlah = int(game[1].split()[0]) + 1
                    game[1] = f"{jumlah} Bulan"
                else:
                    game[1] = game[1] + " + 1 Bulan"

                game[2] += 180000
                total += 180000

            else:
                print("Pilihan durasi tidak valid!")
                input("\nTekan enter untuk kembali ke menu!")
                continue

            daftar_game_penyewa[game_pilih-1] = tuple(game)
            data_penyewaan[pilih-1] = (
                data_penyewaan[pilih-1][0],
                daftar_game_penyewa,
                total,
                data_penyewaan[pilih-1][3]
            )
            print("Durasi penyewaan berhasil diperpanjang!")

        input("\nTekan enter untuk kembali ke menu!")

    elif menu == "6":
        if len(data_penyewaan) == 0:
            print("Belum ada data penyewaan!")

        else:
            cari = input("\nMasukan nama penyewa: ")
            ditemukan = False

            for i in range(len(data_penyewaan)):
                if cari.lower() == data_penyewaan[i][0].lower():

                    print("\n-Data Ditemukan!")
                    print("Nama   :", data_penyewaan[i][0])
                    print("Daftar Game: ")
                    for j in range(len(data_penyewaan[i][1])):
                        print(f"{j+1}. {data_penyewaan[i][1][j][0]}")
                        print(f"Durasi   :{data_penyewaan[i][1][j][1]}")
                        print(f"Harga    : Rp{data_penyewaan[i][1][j][2]}")

                    print("Total Biaya : Rp", data_penyewaan[i][2])
                    print("Status Bayar :",data_penyewaan[i][3])

                    ditemukan = True
                    break
            if ditemukan == False:
                print("Data penyewa tidak ditemukan!")

        input("\nTekan enter untuk kembali!")

    elif menu == "7":
        if len(data_penyewaan) == 0:
            print("Belum ada data penyewaan!")

        else:
            print("\n-HAPUS DATA")
            print("1. Hapus data salah satu penyewa")
            print("2. Hapus semua data")
            pilihan_hapus = input("Pilih menu :")

            if pilihan_hapus == "1":
                for i in range(len(data_penyewaan)):
                    print(f"{i+1}. {data_penyewaan[i][0]}")

                hapus = int(input("Pilih nomor penyewa: "))
                if hapus >= 1 and hapus <= len(data_penyewaan):
                    data = data_penyewaan.pop(hapus-1)
                    print("Data atas nama", data[0], "berhasil dihapus!")

                else:
                    print("Nomor data tidak valid!")

            elif pilihan_hapus == "2":
                konfirm = input("Ingin menghapus semua data? (ya/tidak) : ")
                if konfirm.lower() == "ya":
                    data_penyewaan.clear()
                    print("Semua data penyewa berhasil dihapus!")

                else:
                    print("Penghapusan dibatalkan.")

            else:
                print("Pilihan tidak tersedia!")

        input("\nTekan enter untuk kembali!")

    elif menu == "8":
        if len(data_penyewaan) ==0:
            print("Belum ada data penyewaan!")
        else:
            print("\n-KELOLA GAME PENYEWA")
            for i in range(len(data_penyewaan)):
                print(f"{i+1}. {data_penyewaan[i][0]}")

            pilih = int(input("Pilih nomor penyewa : "))
            if pilih < 1 or pilih > len(data_penyewaan):
                print("Nomor penyewa tidak valid!")
                input("\nTekan enter untuk kembali!")
                continue

            daftar_game_penyewa = list(data_penyewaan[pilih-1][1])
            total = data_penyewaan[pilih-1][2]

            print("\n1. Tambah game")
            print("2. Hapus salah satu game")
            print("3. Hapus semua game penyewa")

            opsi = input("Pilih menu: ")

            if opsi == "1":
                print("\nDaftar Game")
                for i in range(len(daftar_gamesewa)):
                    print(f"{i+1}. {daftar_gamesewa[i]}")

                nomor = int(input("Pilih nomor game yang ingin ditambahkan: "))
                if nomor < 1 or nomor > len(daftar_gamesewa):
                    print("Nomor game tidak tersedia!")
                    input("\nTekan enter untuk kembali!")
                    continue
                print("\n-Pilih Durasi")
                print("1. Per hari")
                print("2. Per minggu")
                print("3. Per bulan")

                durasi = input("Pilih durasi: ")

                if durasi == "1":
                    daftar_game_penyewa.append((daftar_gamesewa[nomor-1], "1 Hari", 10000))
                    total += 10000

                elif durasi == "2":
                    daftar_game_penyewa.append((daftar_gamesewa[nomor-1], "1 Minggu", 60000))
                    total += 60000

                elif durasi == "3":
                    daftar_game_penyewa.append((daftar_gamesewa[nomor-1], "1 Bulan", 180000))
                    total += 180000

                else:
                    print("Pilihan durasi tidak valid!")
                    input("\nTekan enter untuk kembali!")
                    continue

                print("Game berhasil ditambahkan!")

            elif opsi == "2":
                if len(daftar_game_penyewa) == 0:
                    print("Penyewa belum memiliki game yang dipilih!")
                    input("\nTekan enter untuk kembali!")
                    continue

                print("\n-Daftar Game Penyewa")
                for i in range(len(daftar_game_penyewa)):
                    print(f"{i+1}. {daftar_game_penyewa[i][0]}")

                hapus = int(input("Pilih nomor game yang ingin dihapus: "))
                if hapus < 1 or hapus > len(daftar_game_penyewa):
                    print("Nomor game tidak valid!")
                    input("\nTekan enter untuk kembali!")
                    continue

                total -= daftar_game_penyewa[hapus-1][2]
                daftar_game_penyewa.pop(hapus-1)
                print("Game berhasil dihapus!")

            elif opsi == "3":
                if len(daftar_game_penyewa) == 0:
                    print("Penyewa belum memiliki game!")
                    input("\nTekan enter untuk kembali!")
                    continue

                konfirm = input("Ingin menghapus semua game penyewa? (ya/tidak): ")

                if konfirm.lower() == "ya":
                    daftar_game_penyewa.clear()
                    total = 0
                    print("Semua game penyewa berhasil dihapus!")
                else:
                    print("Penghapusan dibatalkan.")

            else:
                print("Pilihan menu tidak valid!")
                input("\nTekan enter untuk kembali!")
                continue

            data_penyewaan[pilih-1] = (
                data_penyewaan[pilih-1][0],
                daftar_game_penyewa,
                total,
                data_penyewaan[pilih-1][3]
            )

        input("\nTekan enter untuk kembali ke menu!")

    elif menu == "9":
        print("\n-RINGKASAN DATA PENYEWAAN")

        if len(data_penyewaan) == 0:
            print("Belum ada data penyewaan!")

        else:
            sudah = 0
            belum = 0
            total_pendapatan = 0

            for i in range(len(data_penyewaan)):
                print(f"\n-Penyewa {i+1}")
                print("Nama Penyewa: ", data_penyewaan[i][0])
                print("-Daftar Game: ")
                for j in range(len(data_penyewaan[i][1])):
                    print(f"{j+1}. {data_penyewaan[i][1][j][0]}")
                    print(f"  Durasi: {data_penyewaan[i][1][j][1]}")
                    print(f"  Harga: Rp{data_penyewaan[i][1][j][2]}")
                print("Total Biaya: Rp", data_penyewaan[i][2])
                print("Status Bayar: ", data_penyewaan[i][3])

                if data_penyewaan[i][3] == "Sudah Dibayar":
                    sudah += 1
                    total_pendapatan += data_penyewaan[i][2]
                else:
                    belum += 1

            print("-STATISTIK")
            print("Jumlah Penyewa: ", len(data_penyewaan))
            print("Sudah Dibayar: ", sudah)
            print("Belum Dibayar: ", belum)
            print("Total Pendapatan: Rp", total_pendapatan)

        print(f"\nTerima kasih telah menggunakan GameCloud, {username}!")
        break

    else:
        print("Menu tidak tersedia! Silahkan pilih menu antara 1 - 9")
