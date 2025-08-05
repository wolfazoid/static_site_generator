import os

from block_markdown import heading_to_html, markdown_to_blocks, markdown_to_html_node
from htmlnode import ParentNode

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path) as f:
        md = f.read()
    with open(template_path) as t:
        template = t.read()
    html_content = markdown_to_html_node(md).to_html()
    title = extract_title(md)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_content)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path!= "":
        os.makedirs(dest_dir_path, exist_ok = True)
    with open(dest_path,"w") as html_file:
        html_file.write(template) 
    
    
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for fpath in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, fpath)
        dest_path = os.path.join(dest_dir_path, fpath)
        if dest_path.endswith('md'):
            html_path = dest_path.rstrip('.md') + '.html'
            generate_page(from_path, template_path, html_path, basepath)
        else:
            generate_pages_recursive(from_path, template_path, dest_path, basepath)

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