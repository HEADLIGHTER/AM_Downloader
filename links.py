def clear_list(links_list: list):
    trash = ['\n', '?usp=drive_link', '?usp=share_link', '?usp=sharing', 'https://drive.google.com/drive/folders/', 'https://drive.google.com/drive/u/0/folders/', 'https://drive.google.com/drive/u/1/folders/']
    links_list = list(set(links_list))
    for t in trash:
        links_list = [_.replace(t, '') for _ in links_list]
    links_list.insert(0, '-i')
    return links_list


def get_pure_list():

    with open('links') as f:
        links_list = f.readlines()
    links_list = clear_list(links_list)
    return links_list
