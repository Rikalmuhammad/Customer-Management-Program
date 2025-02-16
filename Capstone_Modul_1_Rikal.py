from tabulate import tabulate
import datetime

#Database Customers (list of dict)
customers = [
    {"customer_id": "CUST-001", "name": "Rikal Muhammad", "phone_number": "081312344432", "usia": 26, "pekerjaan": "Swasta"},
    {"customer_id": "CUST-002", "name": "Rikal Renaldy", "phone_number": "081298765432", "usia": 24, "pekerjaan": "Mahasiswa"},
    {"customer_id": "CUST-003", "name": "Andi", "phone_number": "081345678901", "usia": 30, "pekerjaan": "Pegawai Negeri"},
    {"customer_id": "CUST-004", "name": "Budi Arie", "phone_number": "081234567890", "usia": 28, "pekerjaan": "Freelancer"},
    {"customer_id": "CUST-005", "name": "Citra", "phone_number": "081567890123", "usia": 27, "pekerjaan": "Wiraswasta"},
    {"customer_id": "CUST-006", "name": "Dewi", "phone_number": "081678901234", "usia": 22, "pekerjaan": "Mahasiswa"},
    {"customer_id": "CUST-007", "name": "Eko Patrio", "phone_number": "081789012345", "usia": 35, "pekerjaan": "Dokter"},
    {"customer_id": "CUST-008", "name": "Fajar Arie", "phone_number": "081890123456", "usia": 40, "pekerjaan": "Arsitek"},
    {"customer_id": "CUST-009", "name": "Gita", "phone_number": "081201234567", "usia": 29, "pekerjaan": "Guru"},
    {"customer_id": "CUST-010", "name": "Patrio Hadi", "phone_number": "081812345678", "usia": 31, "pekerjaan": "Teknisi"}
]

#Database Transactions (list of dict)
transactions = [
    {"transaction_id": 101, "customer_id": "CUST-001", "service": "deep clean", "date": "2025-02-01"},
    {"transaction_id": 102, "customer_id": "CUST-002", "service": "fast clean", "date": "2025-02-01"},
    {"transaction_id": 103, "customer_id": "CUST-003", "service": "deep clean", "date": "2025-02-02"},
    {"transaction_id": 104, "customer_id": "CUST-004", "service": "express clean", "date": "2025-02-02"},
    {"transaction_id": 105, "customer_id": "CUST-005", "service": "fast clean", "date": "2025-02-02"},
    {"transaction_id": 106, "customer_id": "CUST-006", "service": "deep clean", "date": "2025-02-03"},
    {"transaction_id": 107, "customer_id": "CUST-007", "service": "express clean", "date": "2025-02-03"},
    {"transaction_id": 108, "customer_id": "CUST-008", "service": "fast clean", "date": "2025-02-04"},
    {"transaction_id": 109, "customer_id": "CUST-009", "service": "deep clean", "date": "2025-02-05"},
    {"transaction_id": 110, "customer_id": "CUST-010", "service": "express clean", "date": "2025-02-05"},
    {"transaction_id": 111, "customer_id": "CUST-003", "service": "deep clean", "date": "2025-02-06"},
    {"transaction_id": 112, "customer_id": "CUST-006", "service": "deep clean", "date": "2025-02-07"},
    {"transaction_id": 113, "customer_id": "CUST-006", "service": "deep clean", "date": "2025-02-07"}
]

#Daftar Harga(dictionary)
pricelist = {
    "deep clean": 40000,
    "fast clean": 30000,
    "express clean": 70000
}

#Fungsi submenu show data cust
def submenu_show_customers():
    while True:
        print("\n=== Sub Menu Show Data ===")
        print("1. Tampilkan Semua Data Customers")
        print("2. Tampilkan Data Customers dengan Filter")
        print("3. Kembali ke Main Menu")
        pilihan = input("Pilih menu (1-3): ")

        if pilihan == "1":
            if not customers:
                print("\nData tidak ditemukan (Database Kosong).")
                continue
            show_customers(customers, transactions)
        elif pilihan == "2":
            if not customers:
                print("\nData tidak ditemukan (Database Kosong).")
                continue
            filtered_results = filter_customers(customers)
            if filtered_results:
                show_customers(filtered_results, transactions)  
            else:
                print("Tidak ada data yang sesuai dengan filter.")
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")

#Fungsi show data cust
def show_customers(customers, transactions):
    table = []
    for i in range(len(customers)):
        customer = customers[i]
        total_transaksi = sum(1 for t in transactions if t["customer_id"] == customer["customer_id"])
        stamp_counter = total_transaksi % 12
        table.append([i+1, customer["customer_id"], customer["name"], customer["phone_number"], customer["usia"], customer["pekerjaan"], total_transaksi, stamp_counter])

    print("\nDaftar Customer")
    print(tabulate(table, headers=["No", "Cust-ID", "Nama", "Kontak", "Usia", "Pekerjaan", "Transaksi", "Stamp"], tablefmt="fancy_grid"))

# Fungsi Filter show data cust
def filter_customers(customers):
    print("Filter Customers:")
    
    filter_criteria = {}  

    while True:
        filter_key = input("Masukkan kata kunci filter (customer_id, name, phone_number, pekerjaan, usia, atau kosong untuk selesai): ").strip().lower()
        
        if not filter_key:
            break
        
        if filter_key not in ["customer_id", "name", "phone_number", "pekerjaan", "usia"]:
            print("Kata kunci filter tidak valid! Pilih antara 'customer_id', 'name', 'phone_number', 'pekerjaan' atau 'usia'.")
            continue
        
        if filter_key not in filter_criteria:
            filter_criteria[filter_key] = []  
        
        while True:
            filter_value = input(f"Masukkan nilai untuk {filter_key} (biarkan kosong untuk selesai menambahkan nilai): ").strip().lower()
            
            if not filter_value:
                break
            
            if filter_value not in filter_criteria[filter_key]:  
                filter_criteria[filter_key].append(filter_value)
            break
        
        while True:
            add_more = input("Apakah ingin menambah filter lain? (ya/tidak): ").strip().lower()
            if add_more in ["ya", "tidak"]:
                break
            print("Input tidak valid! Harap masukkan 'ya' atau 'tidak'.")
        
        if add_more != "ya":
            break

    
    def filter_condition(customer):
        for key, values in filter_criteria.items():
            if key == "customer_id":
                if customer[key].lower() not in values:
                    return False
            elif key == "usia":
                if not any(str(customer["usia"]).startswith(value) for value in values):
                    return False
            else:
                if not any(value in customer[key].lower() for value in values):
                    return False
        return True
    
    filtered_customers = list(filter(filter_condition, customers))
    
    if not filtered_customers:
        print("Tidak ada data yang cocok dengan filter yang diberikan.")
    
    return filtered_customers

#Fungsi submenu Add data cust
def submenu_add_customers():
    while True:
        print("\n=== Sub Menu Add Data ===")
        print("1. Tambahkan Data Customers")
        print("2. Kembali ke Main Menu")
        pilihan = input("Pilih menu (1-2): ")

        if pilihan == "1":
            add_customers()
        elif pilihan == "2":
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")

#Fungsi add data cust
def add_customers():
    # buat customer_id baru
    if not customers:
        new_id = "CUST-001"
    else:
        last_id = max(int(c["customer_id"].split("-")[1]) for c in customers)
        new_id = f"CUST-{last_id + 1:03}"  #padding

    # Input no hp
    while True:
        kontak = input("Masukkan Nomor Handphone: ")
        if not kontak.isdigit() or not (10 <= len(kontak) <= 12):
            print("Nomor Handphone harus berupa angka dengan panjang 10-12 digit.")
            continue
        if any(customer["phone_number"] == kontak for customer in customers):
            print("Nomor Handphone sudah ada.")
            continue
        break

    # Input nama
    while True:
        name = input("Masukkan Nama: ")
        if any(ch.isdigit() for ch in name):
            print("Nama tidak boleh mengandung angka.")
            continue
        break

    # Input usia
    while True:
        usia = input("Masukkan Usia: ")
        if not usia.isdigit() or not (10 <= int(usia) <= 99):
            print("Usia harus berupa angka antara 10 dan 99.")
            continue
        break

    # Input pekerjaan
    while True:
        pekerjaan = input("Masukkan Pekerjaan: ")
        if any(ch.isdigit() for ch in pekerjaan):
            print("Pekerjaan tidak boleh mengandung angka.")
            continue
        break

    print(f"Anda yakin ingin menambahkan {name}, Kontak: {kontak}, Usia: {usia}, Pekerjaan: {pekerjaan}?")
    while True:
        yakin = input("ya / tidak: ").strip().lower()
        if yakin in ["ya", "tidak"]:
            break
        print("Input tidak valid! Harap masukkan 'ya' atau 'tidak'.")
    if yakin == "ya":
        customers.append({"customer_id": new_id, "name": name, "phone_number": kontak, "usia": int(usia), "pekerjaan": pekerjaan})
        print("Customer berhasil ditambahkan!")

#Fungsi submenu update cust
def submenu_update_customers():
    while True:
        print("\n=== Sub Menu Update Data ===")
        print("1. Update Data Customers")
        print("2. Kembali ke Main Menu")
        pilihan = input("Pilih menu (1-2): ")

        if pilihan == "1":
            update_customers()
        elif pilihan == "2":
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")

#Fungsi update cust
def update_customers():
    while True:
        cust_id = input("\nMasukkan Customer ID yang ingin diperbarui (kosongkan untuk batal): ").strip().lower()
        if cust_id == "":
            return
        if not any(customer["customer_id"].lower() == cust_id for customer in customers):
            print("Customer ID tidak ditemukan, coba lagi.")
            continue
        break

    data_update = [customer for customer in customers if customer["customer_id"].lower() == cust_id]
    print("\nData Customer:")
    print(tabulate(data_update, headers="keys", tablefmt="fancy_grid"))
    print("\nLanjutkan update Data di atas?")
    while True:
        yakin = input("ya / tidak: ").strip().lower()
        if yakin in ["ya", "tidak"]:
            break
        print("Input tidak valid! Harap masukkan 'ya' atau 'tidak'.")
    if yakin != "ya":
        print("Update dibatalkan.")
        return

    while True:  # Loop untuk memastikan kolom dan nilai baru valid
        kolom = input("Masukkan Kolom yang ingin diperbarui (customer_id, name, phone_number, usia, pekerjaan): ").strip().lower()
        valid_keys = customers[0].keys()
        if kolom not in valid_keys:
            print("Kolom tidak valid. Pastikan kolom yang dimasukkan sesuai dengan daftar kolom.")
            continue
        # Input nilai baru dengan guard
        while True:
            value = input(f"Masukkan {kolom} baru: ").strip()
            if kolom == "phone_number":
                if not value.isdigit() or not (10 <= len(value) <= 12):
                    print("Nomor Handphone harus berupa angka dengan panjang 10-12 digit.")
                    continue
            elif kolom == "usia":
                if not value.isdigit() or not (10 <= int(value) <= 99):
                    print("Usia harus berupa angka antara 10 dan 99.")
                    continue
                value = int(value)
            elif kolom in ["name", "pekerjaan"]:
                if any(ch.isdigit() for ch in value):
                    print(f"{kolom.capitalize()} tidak boleh mengandung angka.")
                    continue
            break
        while True:
            yakin_update = input("Update Data? (ya/tidak): ").strip().lower()
            if yakin_update in ["ya", "tidak"]:
                break
            print("Input tidak valid! Harap masukkan 'ya' atau 'tidak'.")
        if yakin_update == "ya":
            for customer in customers:
                if customer["customer_id"].lower() == cust_id:
                    customer[kolom] = value
            print("\nData berhasil diperbarui.")
            break
        else:
            print("Update dibatalkan, silakan input kembali kolom dan nilai.")

#Fungsi submenu delete data cust
def submenu_delete_customers():
    while True:
        print("\n=== Sub Menu Delete Data Customers ===")
        print("1. Hapus Data Customers")
        print("2. Hapus Semua Data")
        print("3. Kembali ke Main Menu")
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == "1":
            delete_customers()
        elif pilihan == "2":
            if not customers:
                print("Data yang anda cari tidak ada.")
                continue
            print("Anda yakin ingin menghapus semua data customers?")
            while True:
                yakin = input("ya / tidak: ").strip().lower()
                if yakin in ["ya", "tidak"]:
                    break
                print("Input tidak valid! Harap masukkan 'ya' atau 'tidak'.")
            if yakin == "ya":
                customers.clear()
                print("Data berhasil dihapus.")
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")


                            ###### FITUR TAMBAHAN DIMULAI DISINI #########

#Fungsu delete cust
def delete_customers():
    try:
        index = int(input("Masukkan nomor urut customer yang ingin dihapus: "))
        if not customers or index < 1 or index > len(customers):
            print("Data yang anda cari tidak ada.")
            return
        selected_customer = customers[index - 1]
        print(f"Anda yakin ingin menghapus {selected_customer}?")
        while True:
            yakin = input("ya / tidak: ").strip().lower()
            if yakin in ["ya", "tidak"]:
                break
            print("Input tidak valid! Harap masukkan 'ya' atau 'tidak'.")
        if yakin == "ya":
            del customers[index - 1]
            print("Data berhasil dihapus.")
            
    except ValueError:
        print("Invalid index. Coba Lagi.")
    except IndexError:
        print("Invalid index. Coba Lagi.")
    except KeyboardInterrupt:
        print("Invalid. Coba Lagi.")
    except Exception as e:
        print(f"Invalid {e}. Coba Lagi.")

#Fungsi menjalankan aplikasi
def main():
    while True:
        print("\n=== APLIKASI CUSTOMER & TRANSAKSI ===")
        print("1. Lihat Daftar Customer")
        print("2. Tambah Customer")
        print("3. Update Customer")
        print("4. Hapus Customer")
        print("5. Lihat Riwayat Transaksi Customer")
        print("6. Tambah Transaksi")
        print("7. Update Transaksi")
        print("8. Hapus Transaksi")
        print("9. Keluar")
        pilihan = input("Pilih menu (1-9): ")

        if pilihan == "1":
            submenu_show_customers()
        elif pilihan == "2":
            submenu_add_customers()
        elif pilihan == "3":
            submenu_update_customers()
        elif pilihan == "4":
            submenu_delete_customers()
        elif pilihan == "5":
            show_transactions()
        elif pilihan == "6":
            add_transactions()
        elif pilihan == "7":
            update_transactions()
        elif pilihan == "8":
            delete_transactions()
        elif pilihan == "9":
            print("Terima kasih telah menggunakan aplikasi!")
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")   

# ===================== MULAI DARI SINI ADALAH FITUR TAMBAHAN =====================

#Fungsi show transactions
def show_transactions():
    if not transactions:
        print("\nData transaksi tidak ditemukan (Database Kosong).")
        return

    table = []
    for i, trans in enumerate(transactions, start=1):
        # cari nama customer berdasarkan customer_id, jika ditemukan
        customer_name = next((c["name"] for c in customers if c["customer_id"].lower() == trans["customer_id"].lower()), "Unknown")
        # get harga berdasarkan service (jika ada)
        harga = pricelist.get(trans["service"], "Unknown")
        table.append([i, trans["transaction_id"], trans["customer_id"], customer_name, trans["service"], harga, trans["date"]])
    
    print("\nRiwayat Transaksi")
    print(tabulate(table, headers=["No", "Trans-ID", "Cust-ID", "Nama", "Service", "Harga", "Tanggal"], tablefmt="fancy_grid"))

#Fungsi add transactions
def add_transactions():
    if not transactions:
        new_id = 101
    else:
        new_id = max(t["transaction_id"] for t in transactions) + 1

    while True:
        customer_id = input("Masukkan Customer ID: ").strip()
        if not any(c["customer_id"].lower() == customer_id.lower() for c in customers):
            print("Customer ID tidak ditemukan, coba lagi.")
            continue
        break

    while True:
        print("Layanan yang tersedia:", ", ".join(pricelist.keys()))
        service = input("Masukkan service: ").strip().lower()
        if service not in pricelist:
            print("Service tidak valid, coba lagi.")
            continue
        break

    while True:
        date = input("Masukkan tanggal (YYYY-MM-DD): ").strip()
        try:
            datetime.datetime.strptime(date, "%Y-%m-%d")
            break  # Format tanggal valid, keluar dari loop
        except ValueError:
            print("Format tanggal tidak valid. Harap masukkan dalam format YYYY-MM-DD.")

    print(f"Anda yakin ingin menambahkan transaksi dengan ID {new_id} untuk Customer {customer_id} dengan service {service} pada tanggal {date}?")
    while True:
        yakin = input("ya / tidak: ").strip().lower()
        if yakin in ["ya", "tidak"]:
            break
        print("Input tidak valid! Harap masukkan 'ya' atau 'tidak'.")
    
    if yakin == "ya":
        transactions.append({
            "transaction_id": new_id,
            "customer_id": customer_id,
            "service": service,
            "date": date
        })
        print("Transaksi berhasil ditambahkan!")

#Fungsi update transactions
def update_transactions():
    while True:
        try:
            trans_id = int(input("\nMasukkan Transaction ID yang ingin diperbarui(kosongkan untuk batal): ").strip())
        except ValueError:
            print("Transaction ID harus berupa angka, coba lagi.")
            continue
        if not any(trans["transaction_id"] == trans_id for trans in transactions):
            print("Transaction ID tidak ditemukan, coba lagi.")
            continue
        if trans_id == "":
            return
        break

    data_update = [trans for trans in transactions if trans["transaction_id"] == trans_id]
    print("\nData Transaksi:")
    print(tabulate(data_update, headers="keys", tablefmt="fancy_grid"))
    print("\nLanjutkan update data di atas?")
    while True:
        yakin = input("ya / tidak: ").strip().lower()
        if yakin in ["ya", "tidak"]:
            break
        print("Input tidak valid! Harap masukkan 'ya' atau 'tidak'.")
    
    if yakin != "ya":
        print("Update dibatalkan.")
        return

    while True:
        kolom = input("Masukkan kolom yang ingin diperbarui (customer_id, service, date): ").strip().lower()
        if kolom in ["customer_id", "service", "date"]:
            break
        print("Kolom tidak valid. Silakan masukkan 'customer_id', 'service', atau 'date'.")
    while True:
        value = input(f"Masukkan nilai baru untuk {kolom}: ").strip()
        if kolom == "customer_id":
            if not any(c["customer_id"].lower() == value.lower() for c in customers):
                print("Customer ID tidak ditemukan, coba lagi.")
                continue
        if kolom == "service":
            if value.lower() not in pricelist:
                print("Service tidak valid. Pilih salah satu dari:", ", ".join(pricelist.keys()))
                continue
            value = value.lower()
        elif kolom == "date":  
            try:
                datetime.datetime.strptime(value, "%Y-%m-%d")
            except ValueError:
                print("Format tanggal tidak valid. Harap masukkan dalam format YYYY-MM-DD.")
                continue
        break
    while True:
        yakin_update = input("Update data? (ya/tidak): ").strip().lower()
        if yakin_update in ["ya", "tidak"]:
            break
        print("Input tidak valid! Harap masukkan 'ya' atau 'tidak'.")
    if yakin_update == "ya":
        for trans in transactions:
            if trans["transaction_id"] == trans_id:
                trans[kolom] = value
        print("Data transaksi berhasil diperbarui.")
    else:
        print("Update dibatalkan.")

#Fungsi delete transactions
def delete_transactions():
    while True:
        print("\n=== Sub Menu Delete Transaksi ===")
        print("1. Hapus Transaksi")
        print("2. Hapus Semua Transaksi")
        print("3. Kembali ke Main Menu")
        pilihan_del = input("Pilih menu (1-3): ").strip()

        if pilihan_del == "1":
            try:
                trans_id = int(input("Masukkan Transaction ID yang ingin dihapus: ").strip())
                idx = next((i for i, trans in enumerate(transactions) if trans["transaction_id"] == trans_id), None)
                if idx is None:
                    print("Transaction ID tidak ditemukan.")
                    continue
                print(f"Anda yakin ingin menghapus transaksi berikut:\n{transactions[idx]}")
                while True:
                    yakin = input("ya / tidak: ").strip().lower()
                    if yakin in ["ya", "tidak"]:
                        break
                    print("Input tidak valid! Harap masukkan 'ya' atau 'tidak'.")
                if yakin == "ya":
                    del transactions[idx]
                    print("Transaksi berhasil dihapus.")
            except ValueError:
                print("Transaction ID harus berupa angka.")
            except Exception as e:
                print(f"Error: {e}")
        elif pilihan_del == "2":
            if not transactions:
                print("Tidak ada transaksi untuk dihapus.")
                continue
            print("Anda yakin ingin menghapus semua data transaksi?")
            while True:
                yakin = input("ya / tidak: ").strip().lower()
                if yakin in ["ya", "tidak"]:
                    break
                print("Input tidak valid! Harap masukkan 'ya' atau 'tidak'.")
            if yakin == "ya":
                transactions.clear()
                print("Semua transaksi berhasil dihapus.")
        elif pilihan_del == "3":
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")
      
#Jalankan Aplikasi
main()
