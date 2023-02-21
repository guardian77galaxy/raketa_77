from my_classes.parser_class import RaketaParser

url = "https://amountwork.com/rabota/polsha-krakov/"   #  https://amountwork.com/rabota/polsha-krakov/?page=4

rp_work = RaketaParser(url)


def work_parse():
    s = rp_work.soup

    all_title = s.find('div', class_='vacancies-list').find_all('a')
    all_title_list = []
    all_title_dict = {}

    for item in all_title:
        title_vacancy = item.text.strip()
        link_vacancy = "https://amountwork.com" + item.get('href')
        all_title_dict[title_vacancy] = link_vacancy
        title_link = (title_vacancy, link_vacancy)
        all_title_list.append(title_link)
    all_description = s.find('div', class_='vacancies-list').find_all('p', class_='short-desc')
    all_description_list = []
    for el in all_description:
        short_desc = el.text.strip().replace("\xa0в", "")
        all_description_list.append(short_desc.replace("\xa0", ""))
    print(all_title_dict)
    rp_work.save_info(rp_work, name_file="work_vacancy", my_dict=all_title_dict)





def pagination_work_parse():
    for n in range(2, 5):
        url = f"https://amountwork.com/rabota/polsha-krakov/?page={n}"
        RP_work = RaketaParser(url)

        s = RP_work.soup

        all_vacancy_link = s.find('div', class_='vacancies-list').find_all('a')
        all_title_dict = {}
        for item in all_vacancy_link:
            title_vacancy = item.text.strip()
            link_vacancy = "https://amountwork.com" + item.get('href')
            all_title_dict[title_vacancy] = link_vacancy
            print(all_title_dict)
        name_file = f"vacancy_dict{n}"
        rp_work.save_info(rp_work, name_file=name_file, my_dict=all_title_dict)
        print(f"page{n}")


def main():
    work_parse()
    pagination_work_parse()


if __name__ == '__main__':
    main()
