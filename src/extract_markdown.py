import re

def extract_markdown_images(text):
    markdown_images = re.findall(r"\!\[.*?\]\(.*?\)", text)
    lst_images = []
    for link_text in markdown_images:
        alt_text = re.findall(r"\!\[.*?\]", link_text)
        url = re.findall(r"\(.*?\)", link_text)
        for word in alt_text:
            clean_alt_text = word[2:-1]
        for link in url:
            clean_link = link[1:-1]
        lst_images.append((clean_alt_text, clean_link))