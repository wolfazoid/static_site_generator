import os

from block_markdown import heading_to_html, markdown_to_blocks, markdown_to_html_node
from htmlnode import ParentNode

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path) as f:
        md = f.read()
    with open(template_path) as t:
        template = t.read()
    html_content = markdown_to_html_node(md).to_html()
    title = extract_title(md)

    render_template = template.replace("{{ Title }}", title)
    render_template = render_template.replace("{{ Content }}", html_content)
    f.close()

    if not os.path.exists(dest_path):
        os.mkdir(dest_path)
    html = open(f"{title}.html","w")
    


def extract_title(markdown):
    if "# " not in markdown:
        raise Exception('No h1 header available')
    blocks = markdown_to_blocks(markdown)
    
    title = ""

    while title == "":
        for block in blocks:
            if block.startswith('# '):
                title = block.strip('# ')
                title = title.strip()
                return title