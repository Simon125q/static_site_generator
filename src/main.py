from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode


def text_node_to_html_node(text_node: TextNode) -> HTMLNode:
    match text_node.text_type:
        case TextType.text:
            return LeafNode(tag=None, value=text_node.text, props=None)
        case TextType.bold:
            return LeafNode(tag="b", value=text_node.text, props=None)
        case TextType.italic:
            return LeafNode(tag="i", value=text_node.text, props=None)
        case TextType.code:
            return LeafNode(tag="code", value=text_node.text, props=None)
        case TextType.link:
            return LeafNode(tag="a", value=text_node.text, props={"href":text_node.url})
        case TextType.image:
            return LeafNode(tag="img", value="", props={"src":text_node.url, "alt":text_node.text})
        case _:
            raise Exception("Unknown text type")

            

def main() -> None:
    test = TextNode("new text node", "bold", "http://www.boot.dev")
    print(test)

if __name__ == "__main__":
    main()
