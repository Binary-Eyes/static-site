import re
from textnode import *
from htmlnode import *

class MarkdownBlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_html_node(markdown):
    html_nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case MarkdownBlockType.PARAGRAPH:                
                html_nodes.append(create_paragraph_node(block))
                
    return ParentNode("div", html_nodes)


def create_paragraph_node(block):
    paragraph_nodes = []
    text_nodes = text_to_textnodes(block)
    for text_node in text_nodes:
        paragraph_nodes.append(text_node_to_html_node(text_node))
    return ParentNode("p", paragraph_nodes)


def block_to_block_type(markdown):
    if markdown[0:3] == "```" and markdown[-3:] == "```":
        return MarkdownBlockType.CODE
    if markdown[0] == "#":
        return MarkdownBlockType.HEADING
    
    lines = markdown.split("\n")
    if all(line.startswith(">") for line in lines):
        return MarkdownBlockType.QUOTE
    
    if all(line.startswith("-") for line in lines):
        return MarkdownBlockType.UNORDERED_LIST
    
    for i in range(0, len(lines)):
        if not lines[i].startswith(f"{i}."):
            return MarkdownBlockType.PARAGRAPH

    return MarkdownBlockType.ORDERED_LIST


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def text_to_textnodes(text):
    root = TextNode(text, TextType.TEXT)
    nodes = split_nodes_delimiter([root], "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)
    return nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        images = extract_markdown_images(old_node.text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue

        current = old_node.text
        for image in images:
            sections = current.split(f"![{image[0]}]({image[1]})")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))

            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            current = sections[1]

        if current != "":
            new_nodes.append(TextNode(current, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        links = extract_markdown_links(old_node.text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue

        current = old_node.text
        for link in links:
            sections = current.split(f"[{link[0]}]({link[1]})")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))

            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            current = sections[1]

        if current != "":
            new_nodes.append(TextNode(current, TextType.TEXT))

    return new_nodes


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


def markdown_to_blocks(markdown):
    blocks = []
    sections = markdown.split("\n\n")
    for section in sections:
        if section == "":
            continue

        block = section.lstrip("\n").strip().rstrip("\n")
        blocks.append(block)

    return blocks