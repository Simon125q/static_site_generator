import os
from re import template
from block_conversions import BlockType, get_block_type, markdown_to_blocks
from markdown_conversions import markdown_to_html_node


def extract_title(markdown: str) -> str:
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if get_block_type(block) == BlockType.heading and block[:2] == "# ":
            return block.lstrip("# ").strip()
    raise Exception("No title is provided")

def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown_file = open(from_path, mode='r')
    markdown = markdown_file.read()
    template_file = open(template_path, mode='r') 
    template = template_file.read()
    html_node = markdown_to_html_node(markdown)
    html_repr = html_node.to_html()
    title = extract_title(markdown)
    html_result = template.replace("{{ Title }}", title).replace("{{ Content }}", html_repr)
    if not os.path.isdir("/".join(dest_path.split("/")[:-1])):
        os.makedirs("/".join(dest_path.split("/")[:-1]))
    result_file = open(dest_path, 'w')
    result_file.write(html_result)
    result_file.close()

def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str) -> None:
    dir_list = os.listdir(dir_path_content) 
    for dir in dir_list:
        path_in = os.path.join(dir_path_content, dir)
        path_out = os.path.join(dest_dir_path, dir)
        if os.path.isfile(path_in):
            if dir.split(".")[-1] == "md":
                generate_page(path_in, template_path, path_out.replace(".md", ".html"))
        else:
            generate_pages_recursive(path_in, template_path, path_out)


