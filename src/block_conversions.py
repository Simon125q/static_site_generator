
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

