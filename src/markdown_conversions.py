from conversions import text_to_textnodes
from htmlnode import HTMLNode
from block_conversions import BlockType, markdown_to_blocks, get_block_type
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import TextNode, TextType

def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        children.append(block_to_child_node(block))
    return ParentNode("div", children=children)

def block_to_child_node(block: str) -> ParentNode | LeafNode:
    def _block_to_node(block: str, tag: str) -> ParentNode | LeafNode:
            text_nodes = text_to_textnodes(block)
            if len(text_nodes) == 1:
                return LeafNode(tag, block)
            else:
                children = text_nodes_to_children(text_nodes) 
                return ParentNode(tag, children)

    block_type = get_block_type(block)
    match block_type:
        case BlockType.paragraph:
            return _block_to_node(block, "p")
        case BlockType.heading:
            return _block_to_node(" ".join(block.split(" ")[1:]), 
                                  "h" + str(len(block.split(' ')[0])))
        case BlockType.code:
            return ParentNode("pre", children=[LeafNode("code", block.strip("```"))])
        case BlockType.quote:
            lines = block.split("\n")
            clean_lines = []
            for line in lines:
                clean_lines.append(line.lstrip(">").strip())
            return _block_to_node("\n".join(clean_lines), "blockquote")
        case BlockType.unordered_list:
            list_points = []
            for line in block.split("\n"):
                list_points.append(_block_to_node(line.lstrip("* "), "li"))
            return ParentNode("ul", list_points)
        case BlockType.ordered_list:
            list_points = []
            for line in block.split("\n"):
                cleaned_line = " ".join(line.split(". ")[1:])
                list_points.append(_block_to_node(cleaned_line, "li"))
            return ParentNode("ol", list_points)
        case _:
            raise Exception("Unknown block type")

def text_nodes_to_children(text_nodes: list[TextNode]) -> list[HTMLNode]:
    children = []
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))
    return children

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
            if text_node.url != None:
                return LeafNode(tag="a", value=text_node.text, props={"href":text_node.url})
            else:
                raise Exception("Lacking props in link")
        case TextType.image:
            if text_node.url != None:
                return LeafNode(tag="img", value="", props={"src":text_node.url,
                                                            "alt":text_node.text})
            else:
                raise Exception("Lacking props in image")
            
        case _:
            raise Exception("Unknown text type")
