from markdown import markdown_to_html_node

def generate_page(from_path, template_path, dest_path):
    print(f"generating page: from={from_path}, to={dest_path}, template={template_path}")
    with open(from_path, 'r') as md_file:
        markdown = md_file.read()
        
    with open(template_path, 'r') as template_file:
        template = template_file.read()

    html_node = markdown_to_html_node(markdown)
    html = html_node.to_html()
    


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        line = line.lstrip("\n").lstrip()
        if line == "":
            continue

        if line[0] == "#" and line[1] != "#":
            return line.lstrip("#").lstrip()
        else:
            raise Exception("main header line was not found in input markdown")

    raise Exception("main header line was not found in input markdown")