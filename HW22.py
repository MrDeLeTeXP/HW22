from bs4 import BeautifulSoup
import requests
response = requests.get('https://bank.gov.ua/ua/markets/exchangerates')
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features='html.parser')
    soup_list = soup.find_all('td', {'data-label': 'Офіційний курс'})
    print('Курс')
    print('USD =',soup_list[7].text)
    print('EUR =',soup_list[8].text)
    print('PLN =',soup_list[11].text)
    print('CAD =',soup_list[13].text)
    print('AUD =',soup_list[0].text)