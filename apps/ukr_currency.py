from my_classes.parser_class import RaketaParser

url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"

rp_currency = RaketaParser(url)


def load_currency():
    res = rp_currency.response.json()

    for item in res:
        if item["txt"] in ["Фунт стерлінгів", "Долар США", "Євро", "Злотий"]:
            print(f'{item["txt"]}: >>> {item["rate"]}грн.')
    rp_currency.save_info(rp_currency, name_file="ukr_currency", my_dict=res)


