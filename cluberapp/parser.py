import requests
import re

def urls_of_vids():
    url = requests.get('https://www.youtube.com/feeds/videos.xml?channel_id=UC1XHf8VA850M5qT_mhupTZg')
    title_pattern = re.compile(r'<title>Трек-(.+)<\/title>')
    url_pattern = re.compile(r'<yt:videoId>(.+)<\/yt:videoId>')
    title_list = title_pattern.findall(url.text)
    url_list = url_pattern.findall(url.text)
    prop_list = ['https://www.youtube.com/embed/' + url_list[0], title_list[0]]
    return prop_list

def main():
    print(urls_of_vids())

if __name__  == '__main__':
    main()