# Menyimpan data user dalam dictionary
user_data = {}

print("--------------SELAMAT DATANG-------------")	
print("----------DI PROGRAM DONOR DARAH---------")

# PROGRAM UNTUK ADMIN MEMASUKAN AKUN 
print("----------Admin Memasukan Akun-----------")
admin_user = input("Masukan nama admin: ")
admin_password = input("Masukan password admin: ")

# PROGRAM UNTUK USER LOGIN
print("-----------User Memasukan Akun-----------")

def tambah_user():
    """Menambah user baru"""
    user = input("Masukan nama user: ")
    password = input("Masukan password user: ")
    alamat = input("Masukan alamat user: ")
    no_handphone = input("Masukan nomor handphone: ")
    umur = int(input("Masukan umur: "))
    jenis_kelamin = input("Masukan jenis kelamin: ")
    riwayat_penyakit = input("Masukan riwayat penyakit: ")
    golongan_darah = input("Masukan golongan darah: ")
    berat_badan = input("Masukan berat badan: ")
    alkohol = input("Apakah pernah mengonsumsi alkohol (ya/tidak): ")

    # Cek kelayakan donor
    if umur > 16 and alkohol.lower() == "tidak":
        status = "Berhak Mendonor"
    else:
        status = "Tidak Berhak Mendonor"

    user_data[user] = {
        'password': password,
        'alamat': alamat,
        'no_handphone': no_handphone,
        'umur': umur,
        'jenis_kelamin': jenis_kelamin,
        'riwayat_penyakit': riwayat_penyakit,
        'golongan_darah': golongan_darah,
        'berat_badan': berat_badan,
        'alkohol': alkohol,
        'status': status
    }
    print(f"Data user {user} berhasil ditambahkan.\n")

def lihat_user():
    """Melihat semua data user"""
    if user_data:
        for user, info in user_data.items():
            print(f"Nama: {user}, Umur: {info['umur']}, Status Donor: {info['status']}")
    else:
        print("Belum ada user yang terdaftar.\n")

def update_user():
    """Memperbarui data user"""
    user = input("Masukan nama user yang ingin diperbarui: ")
    if user in user_data:
        print(f"Data lama: {user_data[user]}")
        alamat = input("Masukan alamat baru (biarkan kosong jika tidak diubah): ")
        no_handphone = input("Masukan nomor handphone baru (biarkan kosong jika tidak diubah): ")
        umur = input("Masukan umur baru (biarkan kosong jika tidak diubah): ")
        jenis_kelamin = input("Masukan jenis kelamin baru (biarkan kosong jika tidak diubah): ")
        riwayat_penyakit = input("Masukan riwayat penyakit baru (biarkan kosong jika tidak diubah): ")
        golongan_darah = input("Masukan golongan darah baru (biarkan kosong jika tidak diubah): ")
        berat_badan = input("Masukan berat badan baru (biarkan kosong jika tidak diubah): ")
        alkohol = input("Apakah pernah mengonsumsi alkohol (ya/tidak, biarkan kosong jika tidak diubah): ")

        # Update data sesuai input user
        if alamat:
            user_data[user]['alamat'] = alamat
        if no_handphone:
            user_data[user]['no_handphone'] = no_handphone
        if umur:
            user_data[user]['umur'] = int(umur)
        if jenis_kelamin:
            user_data[user]['jenis_kelamin'] = jenis_kelamin
        if riwayat_penyakit:
            user_data[user]['riwayat_penyakit'] = riwayat_penyakit
        if golongan_darah:
            user_data[user]['golongan_darah'] = golongan_darah
        if berat_badan:
            user_data[user]['berat_badan'] = berat_badan
        if alkohol:
            user_data[user]['alkohol'] = alkohol
            if int(umur) > 16 and alkohol.lower() == "tidak":
                user_data[user]['status'] = "Berhak Mendonor"
            else:
                user_data[user]['status'] = "Tidak Berhak Mendonor"

        print(f"Data user {user} berhasil diperbarui.\n")
    else:
        print("User tidak ditemukan.\n")

def hapus_user():
    """Menghapus data user"""
    user = input("Masukan nama user yang ingin dihapus: ")
    if user in user_data:
        del user_data[user]
        print(f"Data user {user} berhasil dihapus.\n")
    else:
        print("User tidak ditemukan.\n")

# Program utama
while True:
    print("\nPilih menu:")
    print("1. Tambah User")
    print("2. Lihat Semua User")
    print("3. Update User")
    print("4. Hapus User")
    print("5. Keluar")

    pilihan = input("Masukkan pilihan (1-5): ")

    if pilihan == '1':
        tambah_user()
    elif pilihan == '2':
        lihat_user()
    elif pilihan == '3':
        update_user()
    elif pilihan == '4':
        hapus_user()
    elif pilihan == '5':
        print("Terima kasih telah menggunakan program Donor Darah!")
        break
    else:
        print("Pilihan tidak valid. Coba lagi.")






