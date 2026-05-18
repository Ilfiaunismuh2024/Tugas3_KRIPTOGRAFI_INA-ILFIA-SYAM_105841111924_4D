import hashlib

# Database sementara untuk menyimpan username dan hash password
database = {}

# Fungsi untuk hash SHA-256
def hash_sha256(password):
    return hashlib.sha256(password.encode()).hexdigest()


while True:
    print("=======================")
    print("  SISTEM LOGIN SHA-256")
    print("=======================")
    print("1. Registrasi")
    print("2. Login")
    print("3. Keluar")

    pilihan = input("Pilih menu (1-3): ")

    # MENU REGISTRASI
    if pilihan == "1":
        print("\n=== MENU REGISTRASI USER ===")

        username = input("Masukkan Username Baru: ")
        password = input("Masukkan Password Baru: ")

        # Hash password
        hashed_password = hash_sha256(password)

        # Simpan ke database
        database[username] = hashed_password

        print("\n--- DATA REGISTRASI ---")
        print("Username     :", username)
        print("Hash SHA-256 :", hashed_password)
        print("------------------------")
        print("Status: Registrasi Berhasil!\n")

    # MENU LOGIN
    elif pilihan == "2":
        print("\n=== MENU LOGIN USER ===")

        username = input("Masukkan Username: ")
        password = input("Masukkan Password: ")

        # Hash password input
        input_hash = hash_sha256(password)

        print("\n--- PROSES VERIFIKASI ---")
        print("Hash Input    :", input_hash)

        # Cek username
        if username in database:
            db_hash = database[username]
            print("Hash Database :", db_hash)

            # Verifikasi password
            if input_hash == db_hash:
                print(f"\nStatus Login: BERHASIL! Selamat datang, {username}.")
            else:
                print("\nStatus Login: GAGAL! Password salah.")

        else:
            print("Username tidak ditemukan!")

        print()

    # MENU KELUAR
    elif pilihan == "3":
        print("Program selesai.")
        break

    # Jika input salah
    else:
        print("Menu tidak valid!\n")