import requests

API_ANAHTARI = "fa6a3ea8b7ab39c71cf1ac43"

def doviz_kurlarini_getir():
    url = f"https://v6.exchangerate-api.com/v6/{API_ANAHTARI}/latest/USD"
    try:
        response = requests.get(url)
        response.raise_for_status() 
        veri = response.json()
        return veri['conversion_rates']
    except requests.exceptions.RequestException as e:
        print(f"Hata: Döviz kurları alınamadı. {e}")
        return None


def doviz_cevir(miktar, kaynak_kur, hedef_kur, kurlar):
    if kurlar is None:
        return None

  
    usd_miktari = miktar / kurlar[kaynak_kur]
    
    hedef_miktari = usd_miktari * kurlar[hedef_kur]

    return hedef_miktari


if __name__ == "__main__":
    kurlar = doviz_kurlarini_getir()

    if kurlar:
        print("Döviz Çeviriciye Hoş Geldiniz!")
        print("Mevcut dövizler: " + ", ".join(kurlar.keys()))

        try:
            
            miktar = float(input("\nÇevirmek istediğiniz miktarı girin: "))
            kaynak_kur = input("Kaynak para birimini girin (örn: USD): ").upper()
            hedef_kur = input("Hedef para birimini girin (örn: TRY): ").upper()

            
            if kaynak_kur not in kurlar or hedef_kur not in kurlar:
                print("Hata: Geçerli bir para birimi girdiniz mi? Lütfen tekrar deneyin.")
            else:
                sonuc = doviz_cevir(miktar, kaynak_kur, hedef_kur, kurlar)
                print(f"\n{miktar} {kaynak_kur} = {sonuc:.2f} {hedef_kur}")

        except ValueError:
            print("Hata: Lütfen geçerli bir sayı girin.")
