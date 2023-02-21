from my_classes.parser_class import RaketaParser

url = "https://nv.ua/ru"

rp_nv_news = RaketaParser(url)


def load_link_news():
    s = rp_nv_news.soup

    all_post_links = s.find_all('div', class_='feed-item')
    nv_post_dict = {}
    for item in all_post_links:
        post_title = item.find('a').text.strip()
        post_link = item.find('a').get('href')
        print(post_title, post_link)
        nv_post_dict[post_title] = post_link
    rp_nv_news.save_info(rp_nv_news, name_file="nv_post", my_dict=nv_post_dict)

    return nv_post_dict


def main():
    load_link_news()


if __name__ == '__main__':
    main()
