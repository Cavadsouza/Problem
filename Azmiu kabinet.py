import requests
from bs4 import BeautifulSoup
import pandas as pd

# Saytın URL-i
url = 'https://kabinet.azmiu.edu.az/'  # Burada URL-ni özünüzə uyğun dəyişdirin

# Saytın HTML-ini çəkirik
response = requests.get(url)

# HTML-i BeautifulSoup ilə parse edirik
soup = BeautifulSoup(response.text, 'html.parser')

# Saytdan lazım olan məlumatları çıxarırıq
# Misal üçün, başlıqları (h1, h2 və s.) çəkmək
headings = soup.find_all(['h1', 'h2', 'h3', 'p'])  # Başlıqlar və mətnlər

# Çıxardığımız məlumatları siyahıya əlavə edirik
data = []
for heading in headings:
    data.append(heading.get_text().strip())  # Hər bir başlıq və ya mətn

# Pandas ilə məlumatları DataFrame-ə çeviririk
df = pd.DataFrame(data, columns=["Mətn"])

# Excel faylına yazırıq
df.to_excel('kabinet_data.xlsx', index=False)

print("Excel faylı yaradıldı!")
