var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]

#menggunakan metode jumpsearch
def method(var, x,):
    n = len(var)

    #digunakan untuk menentukan ukuran lompatan
    jump = int(n ** 0.5)

    #digunakan untuk menentukan indeks awal dan indeks akhir
    kiri, kanan = 0, 0

    while kanan < n and var[kanan] <= x:
        kiri = kanan
        kanan += jump

    #Digunakan untuk melakukan pencarian linear
    for i in range(kiri, min(kanan, n)):
        if var[i] == x:
            return i
    for kolom in range(len(var[i])):
        if (var[i][kolom] == x):
            return i
        
    #Jika indeks tidak ditemukan
    return -1

#Digunakan untuk Mencari data pada list
print("1. Arsel berada di Indeks", method(var, "Arsel"))
print("   Avivah berada di Indeks", method(var, "Avivah"))
print("   Daiva berada di Indeks", method(var, "Daiva"))
print("2. Wahyu berada di Indeks", method(var, "Wahyu"), "pada kolom 0")
print("3. Wibi berada di Indeks", method(var, "Wibi"), "pada kolom 1")