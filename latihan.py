import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# baca file CSV (karena pakai ; sebagai pemisah)
data = pd.read_csv('nilai_siswa.csv', sep=';')

# info dasar
print("=== INFO DATA ===")
print(data.info())
print("\n=== 5 BARIS PERTAMA ===")
print(data.head())
print("\n=== DESKRIPSI NUMERIK ===")
print(data.describe(include='all'))

# pastikan kolom Nilai bertipe numerik
data['Nilai'] = pd.to_numeric(data['Nilai'], errors='coerce')

# cek kalau ada nilai NaN
if data['Nilai'].isna().any():
    print("\n⚠ Ada nilai kosong setelah konversi:")
    print(data[data['Nilai'].isna()])

# tampilkan nilai maksimum dan minimum per mata pelajaran
agg_minmax = data.groupby('Matpel')['Nilai'].agg(['max', 'min'])
print("\n=== MAX & MIN per Matpel ===")
print(agg_minmax)

# hitung rata-rata per mata pelajaran
rata = data.groupby('Matpel')['Nilai'].mean()
print("\n=== RATA-RATA per Matpel ===")
print(rata)

warna = ['#E4E0E1', '#D6C0B3', '#AB886D', '#493628', '#3B3030']

# buat grafik batang (bar chart)
rata.plot(kind='bar', color=warna[:len(rata)], edgecolor='black')
plt.title('Rata-Rata Nilai per Mata Pelajaran')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-Rata')
plt.tight_layout()
plt.show()

# (opsional) tampilkan boxplot sebaran nilai per mapel
# sb.boxplot(x='Matpel', y='Nilai', data=data)
# plt.title('Sebaran Nilai per Mata Pelajaran')
# plt.tight_layout()
# plt.show()