import re

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    trimmed_blocks = []
    for block in blocks:
        if block == "":
            pass
        else:
            block = block.strip()
            trimmed_blocks.append(block)
    return trimmed_blocks

def is_valid_ordered_list(text):
    pattern = r'^(\d+)\. .*'
    lines = text.splitlines()
    previous_number = 0

    for line in lines:
        match = re.match(pattern, line)
        if not match:
            return False  # Line does not match the required pattern
        
        number = int(match.group(1))  # Extract the number from the line
        if number != previous_number + 1:
            return False  # The number is not incrementing by 1
        
        previous_number = number
    return True

def block_to_block_type(markdown_block):
    if re.search(r'^(#{1,6})\s+.*$', markdown_block):
        block_type = "heading"
    elif re.search(r'^```.*```$', markdown_block):
        block_type = "code"
    elif re.search(r'^(?:\>.*)(\n(?:\>.*))*$', markdown_block):
        block_type = "quote"
    elif re.search(r'^(?:\* .+)(\n(?:\* .+))*$', markdown_block):
        block_type = "unordered_list"
    elif re.search(r'^(?:\- .+)(\n(?:\- .+))*$', markdown_block):
        block_type = "unordered_list"
    elif is_valid_ordered_list(markdown_block):
        block_type = "ordered_list"
    else:
        block_type = "paragraph"
    return block_type
