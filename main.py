
import requests
from datetime import datetime
from bs4 import BeautifulSoup

sehirler = ("1)"+ 'Korkuteli\n'+'2)' + "Antalya\n" +  "3)"+ "Ankara\n")

print("Şehrinizi Seçin: ")
print(sehirler)
sehir = input()

if sehir == "":
    sehir = "korkuteli"
url = 'https://namazvakitleri.diyanet.gov.tr/tr-TR/9234/'+ sehir + '-icin-namaz-vakti'


response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

content_div = soup.find('div', id='today-pray-times-row')
sayi1=3
sayi2=4
su_an = datetime.now()
saat = su_an.strftime("%H:%M")
if content_div:
    yazi = content_div.text.split('\n')
    while(sayi2 < 35):

        print(yazi[sayi1]+" "+yazi[sayi2])
        if (saat > yazi[sayi2]) and (saat < yazi[sayi2+6]):
            son_yazi = ("Şuan " + sehir + " Bölgesinde " +  yazi[sayi1] + " Vaktindesiniz")
        sayi1 = sayi2 + 5
        sayi2 = sayi1 + 1
else:
    print("Belirtilen ID'ye sahip bir div bulunamadı.")


print("\n"+son_yazi)


