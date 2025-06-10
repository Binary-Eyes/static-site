import re
from textnode import *

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def split_nodes_image(old_nodes):
    pass


def split_nodes_link(old_nodes):
    pass


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if text_type == TextType.TEXT:
        return old_nodes
    
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        first_split = old_node.text.split(delimiter, 1)
        if len(first_split) != 2:
            new_nodes.append(old_node)
            continue

        last_split = first_split[1].split(delimiter, 1)
        if len(last_split) != 2:
            raise Exception("invalid markdown: missing closing delimiter")
        
        if first_split[0] != "":
            new_nodes.append(TextNode(first_split[0], TextType.TEXT))

        if last_split[0] != "":
            new_nodes.append(TextNode(last_split[0], text_type))
        
        if last_split[1] != "":            
            last_node = TextNode(last_split[1], TextType.TEXT)
            sub_nodes = split_nodes_delimiter([last_node], delimiter, text_type)
            new_nodes.extend(sub_nodes)

    return new_nodes
        



