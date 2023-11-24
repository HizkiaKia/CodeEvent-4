# Membaca input
n = int(input())
times = list(map(int, input().split()))

# Menjadwalkan pembacaan buku berdasarkan waktu yang diperlukan
times.sort()

# Menghitung total waktu yang diperlukan
total_time = sum(times)

# Menampilkan total waktu yang diperlukan
print(total_time)
