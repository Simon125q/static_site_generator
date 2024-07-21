
from block_conversions import BlockType, get_block_type, markdown_to_blocks


def extract_title(markdown: str) -> str:
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if get_block_type(block) == BlockType.heading and block[:2] == "# ":
            return block.lstrip("# ").strip()
    raise Exception("No title is provided")
