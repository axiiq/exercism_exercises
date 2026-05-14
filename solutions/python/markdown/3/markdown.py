import re

def parse_inline_styles(text):
    """Helper function for bold and italic."""
    text = re.sub(r'__(.*?)__', r'<strong>\1</strong>', text)
    text = re.sub(r'_(.*?)_', r'<em>\1</em>', text)
    return text


def parse(markdown):
    """Main markdown parser function"""
    lines = markdown.split('\n')
    res = []
    in_list = False

    for line in lines:
        heading_match = re.match(r'^(#{1,6})\s+(.*)', line)
        if heading_match:
            if in_list:
                res.append('</ul>')
                in_list = False
            level = len(heading_match.group(1))
            content = parse_inline_styles(heading_match.group(2))
            res.append(f'<h{level}>{content}</h{level}>')
            continue

        list_match = re.match(r'^\*\s+(.*)', line)
        if list_match:
            content = parse_inline_styles(list_match.group(1))
            if not in_list:
                res.append('<ul>')
                in_list = True
            res.append(f'<li>{content}</li>')
            continue
        
        if in_list:
            res.append('</ul>')
            in_list = False

        if line:
            content = parse_inline_styles(line)
            res.append(f'<p>{content}</p>')

    if in_list:
        res.append('</ul>')

    return ''.join(res)