from textnode import TextNode, TextType

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

