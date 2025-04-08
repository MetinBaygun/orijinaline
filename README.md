# Orijinaline.com - Site Doğrulama ve Yönlendirme Uygulaması

Orijinaline.com, kullanıcıların girdiği marka veya site adıyla ilişkili gerçek ve resmi web sitesini bulan bir platformdur. Bu proje, yanlış yazılmış veya sahte web sitelerinden korunmayı amaçlar.

⸻

## Proje Hakkında

Günümüzde sahte web siteleri, kullanıcıları yanıltmak için gerçek web sitelerini taklit etmektedir. Orijinaline.com, kullanıcıların yalnızca bir marka ya da site adı girerek, doğru ve resmi siteye yönlendirilmesini sağlar.

## Özellikler:
 •	Kullanıcı, sadece marka veya site adını girer.
	•	Yapay zeka, web araması yaparak en doğru siteyi bulur.
	•	Kullanıcıya doğru URL’yi gösterir.

⸻

## Teknolojiler
	•	Frontend: HTML, CSS, JavaScript
	•	Backend: Python (FastAPI, Flask), Node.js (Express)
	•	Yapay Zeka: Web arama API’si, doğal dil işleme
	•	Veritabanı: (Opsiyonel, eklenebilir) Firebase, MongoDB
	•	Diğer: Docker, Heroku (deployment için)
⸻

## Nasıl Çalışır?
	1.	Kullanıcı markanın veya site adını yazdığı bir input alanına girer.
	2.	Yapay zeka motoru, verilen input ile bir web araması yapar ve sonucu analiz eder.
	3.	Kullanıcıya doğru ve resmi siteyi döner.

⸻

## Kurulum

1. Backend (API) Kurulumu

# Python ile FastAPI kurulum örneği
pip install fastapi uvicorn requests

	•	Backend’iniz için gerekli tüm kütüphaneleri yükleyin.

# Uygulamanın başlatılması
uvicorn app:app --reload

2. Frontend Kurulumu

# Frontend dosyalarını indirin ve açın
git clone https://github.com/MetinBaygun/orijinaline
cd originaline

	•	index.html dosyasını açarak kullanıcı arayüzünü görüntüleyebilirsiniz.

⸻

## Proje Yapısı
```
/orijinaline
│
├── /backend
│   └── app.py            # FastAPI uygulaması
│   └── requirements.txt  # Gerekli bağımlılıklar
│
├── /frontend
│   ├── index.html        # Kullanıcı arayüzü
│   └── style.css         # Stil dosyası
│   └── script.js         # Frontend için JavaScript dosyası
│
├── README.md             # Proje açıklaması
```


⸻

## Ekran Görüntüleri
	1.	Ana Sayfa - Kullanıcı Girişi:
Resim1

	2.	Sonuç Sayfası - Gerçek Site:

Resim2

⸻

## Katkıda Bulunma

Proje açık kaynaklıdır ve katkılara açıktır. Yardımcı olmak isterseniz, aşağıdaki adımları izleyebilirsiniz:
	1.	Bu repo’yu fork yapın.
	2.	Kendi branch’inizi oluşturun.
	3.	Yaptığınız değişiklikleri commit edin.
	4.	Bir pull request gönderin.

⸻

## Lisans

https://fxcompany.vercel.app/lisans.html
⸻