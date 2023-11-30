import requests


def clear_list(links_list: list):
    #trash = ['\n', '?usp=drive_link', '?usp=share_link', '?usp=sharing', 'https://drive.google.com/drive/folders/', 'https://drive.google.com/drive/u/0/folders/', 'https://drive.google.com/drive/u/1/folders/']
    #for t in trash:
    #    links_list = [_.replace(t, '') for _ in links_list]
    links_list.insert(0, '-i')
    return links_list


# fucking rage quit
def check_links_status(links_list: list):
    links200 = []
    for _ in links_list:
        try:
            rq = requests.get(_)
            print(rq.status_code, ' ', _)
            links200.append(_)
        except requests.ConnectionError:
            print(_ + ' is not available')
    return links200



def get_pure_list():

    with open('links') as f:
        links_list = f.readlines()
    links_list = list(set(links_list))
    links_list = check_links_status(links_list)
    links_list = clear_list(links_list)
    return links_list


if __name__ == '__main__':
    list1 = get_pure_list()
    for _ in list1:
        print(_)
    print(len(list1))
