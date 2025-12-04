import pandas as pd
import math

# KAMUS GLOBAL
path = "https://raw.githubusercontent.com/rennndys/MAAAA/refs/heads/main/data_makanan.csv"
df = pd.read_csv(path)

lokasi = [
    [0, "Gerbang Utama", 0, 0],
    [1, "Parkir Mobil Mahasiswa", -408, 135],
    [2, "Masjid Al-Jabbar", 2160, 764],
    [3, "Labtek V C", 2111, 1195],
    [4, "Labtek V B", 1972, 1396],
    [5, "Labtek V A", 1972, 1396],
    [6, "IPST", 1616, 2590],
    [7, "Labtek IV", 563, 1788],
    [8, "Lab. Terbuka SDA", -330, 2544],
    [9, "Labtek I C (Lab. Sedimentasi)", -303, 3039],
    [10, "GKU II", 426, 2862],
    [11, "GKU I", 960, 3356],
    [12, "Labtek I A", 63, 3390],
    [13, "Labtek I B", 426, 3183],
    [14, "Gedung Kuliah E", 636, 3512],
    [15, "Gedung Kuliah D", 891, 3695],
    [16, "Gedung Kuliah C", 792, 4035],
    [17, "Gedung Kuliah A", 595, 4266],
    [18, "Mushola dan Studio Kriya", 469, 3946],
    [19, "Gedung Utama", 1541, 3946],
    [20, "Labtek III (KOICA)", 1222, 4218],
    [21, "GKU III", 1390, 4600],
    [22, "GSG / Studio TPB FSRD", 920, 5169],
    [23, "GOR Futsal", 560, 5534],
    [24, "Asrama TB I", 390, 5212],
    [25, "Asrama TB II", 240, 5062],
    [26, "Asrama TB III", 90, 4912],
    [27, "Asrama TB IV", -60, 4762],
    [28, "Labtek II A", -254, 4421],
    [29, "Labtek II B", -113, 4245],
    [30, "Screenhouse", -299, 4570],
    [31, "Gedung Kuliah SBM", 268, 4355],
    [32, "GOR Tenis Meja", 339, 5991],
    [33, "GOR Pencak Silat", 317, 6632],
    [34, "Lapangan Sepak Bola", -335, 5802],
    [35, "Water Treatment Plant", -918, 4740],
    [36, "Situ II", 546, 313],
    [37, "Bunderan", 402, 1317],
    [38, "Amphiteater", 520, 4566],
    [39, "Lapangan Multifungsi", 1185, 4889]
]

id_kantin = [10, 18, 20, 21, 25, 26]

def pilihan(x):
# Fungsi untuk input pilihan user, dengan parameter x sebagai banyak pilihan yang tersedia

  # KAMUS LOKAL
  # status : boolean
  # y : integer

  # ALGORITMA
  status = True
  while status == True:
    y = int(input("Silakan masukkan pilihan Anda: "))
    if 1 <= y and y <= x:
      print('─' * 52)
      return y
    else:
      print("Pilihan tidak valid!")

def jarak(a, b):
# Menghitung jarak antara titik a dan b

  # ALGORITMA
  return math.sqrt((lokasi[a][2] - lokasi[b][2])**2 + (lokasi[a][3] - lokasi[b][3])**2)

def konversi_jarak(a):
# Mengembalikan nilai jarak sesungguhnya

  # ALGORITMA
  return a * 0.1474

def tabel_jarak(a):
# Membuat tabel yang berisikan jarak dari lokasi a ke tiap-tiap kantin.

  # KAMUS LOKAL
  # jarak_kantin = array of [0..5] of int

  # ALGORITMA
  jarak_kantin = [0 for i in range(len(id_kantin))]
  for i in range(len(id_kantin)):
    jarak_kantin[i] = jarak(a-1, id_kantin[i])
  return jarak_kantin

def menu(text, width=52, border="═"):
    padding = width - len(text) - 2
    left = padding // 2
    right = padding - left
    return border * left + " " + text + " " + border * right

def cek_toko():
  print("Mau cek tokonya?")
  print("1. Ya")
  print("2. Tidak")
  return pilihan(2)

def item():
# Memberikan pilihan item

  # ALGORITMA
  print("Lagi cari apa nih?")
  print("1. Makanan")
  print("2. Minuman")
  print("3. Apa pun")

def makan():
# Memberikan pilihan tipe makanan

  # ALGORITMA
  print("Mau makanan berat atau makanan ringan?")
  print("1. Makanan Berat")
  print("2. Makanan Ringan")
  print("3. Apa pun")

def protein():
# Memberikan pilihan protein

  # ALGORITMA
  print("Tipe proteinnya mau apa nih?")
  print("1. Daging Ayam")
  print("2. Daging Sapi")
  print("3. Daging Kambing")
  print("4. Telur Ayam")
  print("5. Tahu")
  print("6. Tempe")
  print("7. Apa pun")

def karb():
# Memberikan pilihan karbohidrat

  # ALGORITMA
  print("Tipe karbohidratnya mau apa nih?")
  print("1. Nasi")
  print("2. Mie")
  print("3. Kentang")
  print("4. Apa pun")

def rasa(x):
# Memberikan pilihan rasa dengan x sebagai makanan atau minuman

  # ALGORITMA
  print(f"Mau rasa {x} yang kaya gimana nih?")
  print("1. Pedas")
  print("2. Asam")
  print("3. Manis")
  print("4. Gurih")
  print("5. Netral")
  print("6. Pahit")
  print("7. Apa pun")

def minum():
# Memberikan pilihan minuman

  # ALGORITMA
  print("Mau minuman dingin atau hangat?")
  print("1. Minuman Dingin")
  print("2. Minuman Hangat")
  print("3. Minuman Netral (Suhu Ruang)")
  print("4. Apa pun")

def ringan():
# Memberikan pilihan tipe makanan ringan

  # ALGORITMA
  print("Mau makanan ringan yang kaya gimana?")
  print("1. Gorengan")
  print("2. Roti")
  print("3. Pastry")
  print("4. Kue Basah")
  print("5. Kue Kering")
  print("6. Snack Tepung")
  print("7. Apa pun")

def filter_item(df_temp):
  item()
  tipe_item = pilihan(3)
  if tipe_item == 1:
    df_temp = df_temp[df_temp["tipe_item"] == "Makanan"]
  elif tipe_item == 2:
    df_temp = df_temp[df_temp["tipe_item"] == "Minuman"]
  return df_temp, tipe_item

def filter_tipe_makanan(df_temp):
  makan()
  tipe_makanan = pilihan(3)
  if tipe_makanan == 1:
    df_temp = df_temp[df_temp["tipe_makanan"] == "Berat"]
  elif tipe_makanan == 2:
    df_temp = df_temp[df_temp["tipe_makanan"] == "Ringan"]
  return df_temp, tipe_makanan

def filter_karbo(df_temp):
  karb()
  tipe_karb = pilihan(4)
  if tipe_karb == 1:
    df_temp = df_temp[df_temp["tipe_karbohidrat"] == "Nasi"]
  elif tipe_karb == 2:
    df_temp = df_temp[df_temp["tipe_karbohidrat"] == "Mie"]
  elif tipe_karb == 3:
    df_temp = df_temp[df_temp["tipe_karbohidrat"] == "Kentang"]
  return df_temp

def filter_protein(df_temp):
  protein()
  tipe_protein = pilihan(7)
  if tipe_protein == 1:
    df_temp = df_temp[df_temp["tipe_protein"] == "Daging Ayam"]
  elif tipe_protein == 2:
    df_temp = df_temp[df_temp["tipe_protein"] == "Daging Sapi"]
  elif tipe_protein == 3:
    df_temp = df_temp[df_temp["tipe_protein"] == "Daging Kambing"]
  elif tipe_protein == 4:
    df_temp = df_temp[df_temp["tipe_protein"] == "Telur Ayam"]
  elif tipe_protein == 5:
    df_temp = df_temp[df_temp["tipe_protein"] == "Tahu"]
  elif tipe_protein == 6:
    df_temp = df_temp[df_temp["tipe_protein"] == "Tempe"]
  return df_temp

def filter_makanan_ringan(df_temp):
  ringan()
  tipe_makanan_ringan = pilihan(7)
  if tipe_makanan_ringan == 1:
    df_temp = df_temp[df_temp["tipe_menu_ringan"] == "Gorengan"]
  elif tipe_makanan_ringan == 2:
    df_temp = df_temp[df_temp["tipe_menu_ringan"] == "Roti"]
  elif tipe_makanan_ringan == 3:
    df_temp = df_temp[df_temp["tipe_menu_ringan"] == "Pastry"]
  elif tipe_makanan_ringan == 4:
    df_temp = df_temp[df_temp["tipe_menu_ringan"] == "Kue Basah"]
  elif tipe_makanan_ringan == 5:
    df_temp = df_temp[df_temp["tipe_menu_ringan"] == "Kue Kering"]
  elif tipe_makanan_ringan == 6:
    df_temp = df_temp[df_temp["tipe_menu_ringan"] == "Snack Tepung"]
  return df_temp

def filter_tipe_minuman(df_temp):
  minum()
  tipe_minuman = pilihan(4)
  if tipe_minuman == 1:
    df_temp = df_temp[df_temp["tipe_minuman"] == "Dingin"]
  elif tipe_minuman == 2:
    df_temp = df_temp[df_temp["tipe_minuman"] == "Hangat"]
  elif tipe_minuman == 3:
    df_temp = df_temp[df_temp["tipe_minuman"] == "Netral"]
  return df_temp

def filter_rasa(df_temp, x):
  rasa(x)
  tipe_rasa = pilihan(7)
  if tipe_rasa == 1:
    df_temp = df_temp[df_temp["tipe_rasa"] == "Pedas"]
  elif tipe_rasa == 2:
    df_temp = df_temp[df_temp["tipe_rasa"] == "Asam"]
  elif tipe_rasa == 3:
    df_temp = df_temp[df_temp["tipe_rasa"] == "Manis"]
  elif tipe_rasa == 4:
    df_temp = df_temp[df_temp["tipe_rasa"] == "Gurih"]
  elif tipe_rasa == 5:
    df_temp = df_temp[df_temp["tipe_rasa"] == "Netral"]
  elif tipe_rasa == 6:
    df_temp = df_temp[df_temp["tipe_rasa"] == "Pahit"]
  return df_temp

def filtering(df_temp):
  df_temp, tipe_item = filter_item(df_temp)
  if tipe_item == 1: # Makanan
    df_temp, tipe_makanan = filter_tipe_makanan(df_temp)
    if tipe_makanan == 1:
      df_temp = filter_karbo(df_temp)
      df_temp = filter_protein(df_temp)
      df_temp = filter_rasa(df_temp, "makanan")
    else:
      df_temp = filter_makanan_ringan(df_temp)
      df_temp = filter_rasa(df_temp, "makanan")
  else: # Minuman
    df_temp = filter_tipe_minuman(df_temp)
    df_temp = filter_rasa(df_temp, "minuman")
  return df_temp

def tampil_tabel(df_temp, lokasi_user=None):
  # Tidak ada data
  if df_temp.empty:
    print("Maaf, tidak ada menu yang cocok dengan kriteria kamu :(")
    return

  df_show = df_temp.copy()

  # Pakai lokasi
  if lokasi_user is not None:
    # Hitung jarak ke kantin
    jarak_kantin = tabel_jarak(lokasi_user)

    # Bikin tabel nama-nama kantin
    nama_kantin = ["" for i in range(len(id_kantin))]
    for i, idx_lok in enumerate(id_kantin):
      nama_kantin[i] = lokasi[idx_lok][1]

    # Konversi jarak ke kantin
    def jarak2(lok):
      for i, nama in enumerate(nama_kantin):
        if nama == lok:
          return konversi_jarak(jarak_kantin[i])
      return None

    # Penambahan kolom jarak ke data
    df_show["jarak"] = df_show["lokasi"].apply(jarak2)

    sort_cols = ["jarak"]
    cols = ["nama_makanan", "lokasi", "nama_kantin", "harga", "rating", "jarak"]
    headers = ["Nama Makanan", "Lokasi", "Kantin", "Harga", "Rating", "Jarak (m)"]
  
  # Submenu 2: Budget
  else:
    sort_cols = ["harga"]
    cols = ["nama_makanan", "lokasi", "nama_kantin", "harga", "rating"]
    headers = ["Nama Makanan", "Lokasi", "Kantin", "Harga", "Rating"]

  # Sort dan ambil 10 teratas
  df_show = df_show.sort_values(by=sort_cols)[cols].head(10)

  if df_show.empty:
    print("Maaf, tidak ada menu yang bisa ditampilkan :(")
    return

  rows = df_show.values.tolist()

  # Hitung lebar kolom
  col_widths = [0 for i in range(len(headers))]
  for i in range(len(headers)):
    max_len = len(headers[i])
    for row in rows:
      if len(str(row[i])) > max_len:
        max_len = len(str(row[i]))
    col_widths[i] = max_len

  # Bikin border
  border = "+"
  for w in col_widths:
    border += "-" * (w + 2) + "+"

  # Print header
  print(border)
  header_line = "|"
  for i in range(len(headers)):
    header_line += " " + headers[i].ljust(col_widths[i]) + " |"
  print(header_line)
  print(border)

  # Print isi
  for row in rows:
    row_line = "|"
    for i in range(len(headers)):
      row_line += " " + str(row[i]).ljust(col_widths[i]) + " |"
    print(row_line)

  print(border)
  print('─' * 52)


# ALGORITMA

# Header
print("≡" * 52)
print("M A A A A".center(52))
print("(Makan Apa Aja, Aman Aja!)".center(52))
print("≡" * 52)

# Main program
status = True
while status == True:
  df_temp = df.copy()
  lokasi_user = None
  budget = None

  print(menu("MENU UTAMA"))
  print("Silakan pilih salah satu menu di bawah ini")
  print("1. Rekomendasi Makanan")
  print("2. Toko JAWARA")
  print("3. Toko Terdekat")
  print("4. Exit")

  # Input Pilihan
  menu_utama = pilihan(4)

  # End submenu
  print

  # Menu Utama: Rekomendasi Makanan
  if menu_utama == 1:
    print(menu("FILTER"))
    print("Nah, sekarang, mau filter makanannya gimana, nih?")
    print("1. Lokasi")
    print("2. Harga")
    print("3. Lokasi dan Harga")

    # Input Pilihan
    sub_menu_1 = pilihan(3)

    # Sub Menu 1: Lokasi
    if sub_menu_1 == 1:

      # Set Lokasi
      print(menu("LOKASI"))
      print("Mau cari toko yang terdekat dari mana nih?")
      for i in range(len(lokasi)):
        print(f"{i+1}. {lokasi[i][1]}")
      lokasi_user = pilihan(40)

      # Filtering
      df_temp = filtering(df_temp)

      # Print
      tampil_tabel(df_temp, lokasi_user)

    # Sub Menu 2: Harga
    elif sub_menu_1 == 2:

      # Set Budget
      print("Budget maksimalnya berapa nih?")
      budget = int(input("Masukkan budget Anda: "))
      df_temp = df[df["harga"] <= budget]

      # Filtering
      df_temp = filtering(df_temp)

      # Print
      tampil_tabel(df_temp, lokasi_user)

    else:
      # Set Lokasi
      print("Mau cari toko yang terdekat dari mana nih?")
      for i in range(len(lokasi)):
        print(f"{i+1}. {lokasi[i][1]}")
      lokasi_user = pilihan(40)

      # Set Budget
      print("Budget maksimalnya berapa nih?")
      budget = int(input("Masukkan budget Anda: "))
      df_temp = df[df["harga"] <= budget]

      # Filtering
      df_temp = filtering(df_temp)

      # Print
      tampil_tabel(df_temp, lokasi_user)

  elif menu_utama == 2:
    # Hitung rata-rata rating per toko
    avg_rating = df.groupby("nama_kantin")["rating"].mean()

    # Ambil 5 terbaik (descending)
    top5 = avg_rating.sort_values(ascending=False).head(5)

    # Tampilkan tabel bernomor
    print(menu("5 TOKO JAWARA"))
    print("+-----+-----------------------+--------+")
    print("| No. |       Nama Toko       | Rating |")
    print("+-----+-----------------------+--------+")

    top5_list = list(top5.items())

    for i, (nama, rating) in enumerate(top5_list, start=1):
      print(f"|  {str(i)}  | {nama.ljust(21)} |  {rating:.2f}  |")

    print("+-----+-----------------------+--------+")
    print('─' * 52)

    # Input pilihan untuk menampilkan deskripsi
    pilihan_toko = cek_toko()

    # Deskripsi toko
    if pilihan_toko == 1:
      print("Mau cek toko nomor berapa, nih?")
      cek_toko_jawara = pilihan(5)
      print(f"Nama Toko: {top5_list[cek_toko_jawara-1][0]}")
      
      # Filter untuk satu kantin
      df_temp = df_temp[df_temp["nama_kantin"] == top5_list[cek_toko_jawara-1][0]]
      lokasi_kantin = df_temp["lokasi"].iloc[0]
      print(f"Lokasi: {lokasi_kantin}")

      # Rentang harga
      print(f"Rentang harga: Rp{df_temp["harga"].min()}–Rp{df_temp["harga"].max()} ")

      # Menu terbaik
      print(f"Tiga menu terbaik:")
      print("+------------------------------------------+---------+--------+")
      print("|               Nama Makanan               |  Harga  | Rating |")
      print("+------------------------------------------+---------+--------+")

      df_temp = df_temp.sort_values(by="rating", ascending=False).head(3)
      list_top3 = df_temp[["nama_makanan", "harga", "rating"]].values.tolist()

      for i in range(3):
        print(f"| {list_top3[i][0].ljust(40)} | {str(list_top3[i][1]).ljust(7)} |  {list_top3[i][2]:.2f}  |")
      print("+------------------------------------------+---------+--------+")

    # End submenu
    print("─" * 52)

  # Submenu 3: Kantin Terdekat
  elif menu_utama == 3:
    print("Mau cari kantin yang terdekat dari mana nih?")
    for i in range(len(lokasi)):
      print(f"{i+1}. {lokasi[i][1]}")
    lokasi_user = pilihan(40)
    jarak_kantin = tabel_jarak(lokasi_user)

    # List of list jarak dan id kantin
    daftar_jarak = [[0,0] for i in range(len(jarak_kantin))]
    for i in range(len(jarak_kantin)):
      daftar_jarak[i][0] = id_kantin[i]
      daftar_jarak[i][1] = jarak_kantin[i]

    # Sort jarak
    daftar_jarak.sort(key=lambda x: x[1])

    # Header
    print(menu("KANTIN TERDEKAT"))
    print("+-----+---------------------------+-----------+")
    print("| No. |        Nama Kantin        |   Jarak   |")
    print("+-----+---------------------------+-----------+")

    # Print
    for i in range(len(daftar_jarak)):
      jarak_ke_kantin = konversi_jarak(daftar_jarak[i][1])
      nama = lokasi[daftar_jarak[i][0]][1]
      print(f"|  {str(i+1)}  | {nama.ljust(25)} |  {f'{jarak_ke_kantin:.3f}'.ljust(7)}  |")
    print("+-----+---------------------------+-----------+")
    print('─' * 52)

    # Input pilihan untuk menampilkan deskripsi
    pilihan_deskripsi = cek_toko()

    # Deskripsi toko
    if pilihan_deskripsi == 1:
      print("Mau cek kantin nomor berapa, nih?")
      pilihan_kantin = pilihan(6)
      print(f"Nama Kantin: {lokasi[daftar_jarak[pilihan_kantin-1][0]][1]}")
      print(f"Jarak: {konversi_jarak(daftar_jarak[pilihan_kantin-1][1]):.2f} meter ")

      # Filter hanya kantin yang dipilih
      df_temp = df_temp[df_temp["lokasi"] == lokasi[daftar_jarak[pilihan_kantin-1][0]][1]]
      avg_rating = df_temp.groupby("nama_kantin")["rating"].mean()
      avg_rating_list = list(avg_rating.items())

      # Header
      print(f"Toko-toko di {lokasi[daftar_jarak[pilihan_kantin-1][0]][1]}:")
      print("+-----------------------+--------+")
      print("|       Nama Toko       | Rating |")
      print("+-----------------------+--------+")

      for i in range(len(avg_rating_list)):
        print(f"| {avg_rating_list[i][0].ljust(21)} |  {avg_rating_list[i][1]:.2f}  |")
      
      print("+-----------------------+--------+")

      # End submenu
      print("─" * 52)

  # Exit
  else: 
    status = False
