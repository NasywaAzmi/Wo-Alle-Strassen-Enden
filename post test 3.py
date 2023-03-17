class Senjata:
    def __init__(self, nama, tipe, harga):
        self.nama = nama
        self.tipe = tipe
        self.harga = harga
        self.next = None

class KatalogSenjata:
    def __init__(self):
        self.head = None

    def tambah_senjata(self, nama, tipe, harga):
        senjata_baru = Senjata(nama, tipe, harga)
        if not self.head:
            self.head = senjata_baru
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = senjata_baru

    def tampilkan_katalog(self):
        if not self.head:
            print("Katalog kosong")
        else:
            current_node = self.head
            while current_node:
                print(f"Nama: {current_node.nama}, tipe: {current_node.tipe}, Harga: {current_node.harga}")
                current_node = current_node.next

    def tampilkan(self, halaman): 
        if not self.head: # Jika Tidak Ada Daftar Tas
            print("Data Tas Kosong")
            return
        
        count = 0
        daftar = self.head
        nomor = 1

        print("-"*28)
        print("Katalog Senjata Paman Osama")
        print("-"*28)

        while daftar:
            count += 1
            # Awal Halaman
            if count % halaman == 1: 
                print("\nHalaman", (count-1)//halaman+1)
                print("-"*20)
            
            print(f"{nomor}. {daftar.nama, daftar.harga, daftar.tipe}")
            
            # Akhir Halaman
            if count % halaman == 0: 
                input("Pencet enter untuk pergi ke halaman selanjutnya")
                print("-"*20)
                
            daftar = daftar.next
            nomor += 1
        
        input("Halaman Terakhir")

katalog_senjata = KatalogSenjata()

# Contoh penggunaan
katalog_senjata = KatalogSenjata()
katalog_senjata.tambah_senjata("AK-47", "Rifle", 15000000)
katalog_senjata.tambah_senjata("M16", "Rifle", 20000000)
katalog_senjata.tambah_senjata("MP5", "Submachine Gun", 12000000)
katalog_senjata.tambah_senjata("P90", "Submachine Gun", 18000000)
katalog_senjata.tambah_senjata("M249 SAW", "Light Machine Gun", 25000000)
katalog_senjata.tambah_senjata("RPK-74", "Light Machine Gun", 22000000)
katalog_senjata.tambah_senjata("M60E4", "General Purpose Machine Gun", 30000000)
katalog_senjata.tambah_senjata("Browning M2HB-QCB", "Heavy Machine Gun", 40000000)
katalog_senjata.tambah_senjata("RPG-7V2", "Rocket Propelled Grenade Launcher", 35000000)
katalog_senjata.tambah_senjata("FIM-92 Stinger MANPADS", "Anti-Aircraft Missile System", 50000000)
katalog_senjata.tambah_senjata("M136 AT4 CS HPAA (High Penetration Anti-Armor)", "Anti-Tank Weapon System",45000000)

katalog_senjata.tampilkan(halaman = 3)