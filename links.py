

def clear_list(links_list: list):
    trash = ['\n', '?usp=drive_link', '?usp=share_link', '?usp=sharing', 'https://drive.google.com/drive/folders/', 'https://drive.google.com/drive/u/0/folders/', 'https://drive.google.com/drive/u/1/folders/']
    for t in trash:
        links_list = [_.replace(t, '') for _ in links_list]
    links_list.insert(0, '-i')
    return links_list


def get_pure_list():
    tmp_list = []
    with open('links') as f:
        links_list = f.readlines()
    [tmp_list.append(_) for _ in links_list if _ not in tmp_list]
    links_list = tmp_list
    links_list = clear_list(links_list)
    return links_list


if __name__ == '__main__':
    list1 = get_pure_list()
    for _ in list1:
        print(_)
    print(len(list1))
