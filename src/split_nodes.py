from textnode import *
from extract_markdown import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
        text_nodes_list = []
        for node in old_nodes:
            if node.text_type != "text":  #already in it's final form
                text_nodes_list.append(TextNode(node, node.text_type))
                continue
            elif node.text_type == "text":
                temp_split = node.text.split(delimiter)
                for split_text in temp_split:
                    if temp_split.index(split_text) % 2 == 0:
                        text_nodes_list.append(TextNode(split_text, node.text_type))
                    else:
                        text_nodes_list.append(TextNode(split_text, text_type))
        return text_nodes_list

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        #extract links from the text
        links = extract_markdown_links(node.text)
        #if no links, just add original node
        if not links:
            new_nodes.append(node)
        else:
            #splitting around the link
            remaining_text = node.text
            for link in links:
                link_markdown = f"[{link[0]}]({link[1]})"
                parts = remaining_text.split(link_markdown, 1)
                if parts[0]:
                    new_nodes.append(TextNode(parts[0], node.text_type))
                new_nodes.append(TextNode(link[0], text_type_link, link[1]))
                if len(parts) > 1:
                    remaining_text = parts[1]
                else:
                    remaining_text = ""
            if remaining_text:
                new_nodes.append(TextNode(remaining_text, node.text_type))
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        #extract images from the text
        images = extract_markdown_images(node.text)
        #if no images, just add original node
        if not images:
            new_nodes.append(node)
        else:
            #splitting around the link
            remaining_text = node.text
            for image in images:
                image_markdown = f"![{image[0]}]({image[1]})"
                parts = remaining_text.split(image_markdown, 1)
                if parts[0]:
                    new_nodes.append(TextNode(parts[0], node.text_type))
                new_nodes.append(TextNode(image[0], text_type_image, image[1]))
                if len(parts) > 1:
                    remaining_text = parts[1]
                else:
                    remaining_text = ""
            if remaining_text:
                new_nodes.append(TextNode(remaining_text, node.text_type))
    return new_nodes