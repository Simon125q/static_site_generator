from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str,
                          text_type: TextType) -> list[TextNode]:
    result_nodes = list()
    for node in old_nodes:
        if node.text_type == TextType.text:
            new_nodes = node.text.split(delimiter)
            if len(new_nodes) == 1:
                result_nodes.append(node)
            elif len(new_nodes) % 2 == 0:
                raise Exception("Invalid markdown syntax")
            else:
                for index, text in enumerate(new_nodes):
                    if index % 2 == 0:
                        result_nodes.append(TextNode(text, TextType.text))
                    else:
                        result_nodes.append(TextNode(text, text_type))
        else:
            result_nodes.append(node)
    return result_nodes

def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    return list(map(lambda x: x[-2:], re.findall(r"(^|[^!])\[(.*?)\]\((.*?)\)", text)))

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    result = list()
    for node in old_nodes:
        if node.text_type != TextType.text:
            result.append(node)
        else:
            text = node.text
            imgs = extract_markdown_images(text)
            for img in imgs:
                temp = text.split(f"![{img[0]}]({img[1]})", 1)
                if temp[0] != "":
                    result.append(TextNode(temp[0], TextType.text))
                result.append(TextNode(img[0], TextType.image, img[1]))
                text = temp[1]
            if text != "":
                result.append(TextNode(text, TextType.text))

    return result

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    result = list()
    for node in old_nodes:
        if node.text_type != TextType.text:
            result.append(node)
        else:
            text = node.text
            links = extract_markdown_links(text)
            for l in links:
                temp = text.split(f"[{l[0]}]({l[1]})", 1)
                if temp[0] != "":
                    result.append(TextNode(temp[0], TextType.text))
                result.append(TextNode(l[0], TextType.link, l[1]))
                text = temp[1]
            if text != "":
                result.append(TextNode(text, TextType.text))

    return result

def text_to_textnodes(text: str) -> list[TextNode]:
    nodes = [TextNode(text, TextType.text)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.bold)
    nodes = split_nodes_delimiter(nodes, "*", TextType.italic)
    nodes = split_nodes_delimiter(nodes, "`", TextType.code)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)
    return nodes
