from enum import Enum

class BlockType(Enum):
    paragraph = "paragraph"
    heading = "heading"
    code = "code"
    quote = "quote"
    unordered_list = "unordered_list"
    ordered_list = "ordered_list"

def markdown_to_blocks(text: str) -> list[str]:
    lines = text.split("\n")
    blocks = list()
    curr_block = ""
    for line in lines:
        if line.strip() == "":
            if curr_block != "":
                blocks.append(curr_block.strip())
                curr_block = ""
        else:
            curr_block += line.strip() + "\n"
    if curr_block != "":
        blocks.append(curr_block.strip())
    return blocks

def get_block_type(block: str) -> BlockType:
    if block[:2] == "# ":
        return BlockType.heading
    elif block[:3] == "```" and block[-3:] == "```":
        return BlockType.code
    lines = block.split("\n")
    if lines[0][:2] in ["* ", "- "]:
        is_un_list = True
        for line in lines:
            if line[:2] not in ["* ", "- "]:
                is_un_list = False
        if is_un_list:
            return BlockType.unordered_list
    elif lines[0][:3] == "1. ":
        for index, line in enumerate(lines):
            if not line.startswith(str(index + 1) + ". "):
                return BlockType.paragraph
        return BlockType.ordered_list

    return BlockType.paragraph
    

