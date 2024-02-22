import datetime as dt
today = dt.date.today()

tanggal = int(input("Tanggal : "))
bulan = int(input("Bulan : "))
tahun = int(input("Tahun : "))

date = dt.date(tahun,bulan,tanggal)
age = today-date
years = (age.days // 365)
month = (age.days % 365) // 30
day = (age.days % 365) % 30

print(f"Lahir di hari : {date:%A}")
print(f"umur anda adalah: {years} tahun, {month} bulan, {day} hari")