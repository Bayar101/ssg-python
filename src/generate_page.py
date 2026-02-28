import os

from block_markdown import markdown_to_html_node


def extract_title(markdown):
    blocks = markdown.split("\n\n")
    val = None
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        if block.startswith("# "):
            val = block

    if val:
        return val.replace("#", "").strip()

    raise Exception("No title found")


def get_file_content(file_path):
    abs_path = os.path.abspath(file_path)

    if not os.path.isfile(abs_path):
        return f'Error: File not found or is not a refular file: "{file_path}"'

    with open(abs_path, "r") as f:
        content = f.read()

    return content


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    from_content = get_file_content(from_path)
    title = extract_title(from_content)
    template_content = get_file_content(template_path)

    from_node = markdown_to_html_node(from_content)
    html_string = from_node.to_html()

    content = template_content.replace("{{ Title }}", title)
    content = content.replace("{{ Content }}", html_string)

    # Replace root-relative paths
    content = content.replace('href="/', f'href="{basepath}')
    content = content.replace('src="/', f'src="{basepath}')

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(content)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    dir_abs = os.path.abspath(dir_path_content)

    for entry in os.listdir(dir_abs):
        entry_path = os.path.join(dir_abs, entry)

        # If it's a directory → recurse
        if os.path.isdir(entry_path):
            new_dest_dir = os.path.join(dest_dir_path, entry)
            generate_pages_recursive(
                entry_path,
                template_path,
                new_dest_dir,
                basepath,
            )

        # If it's a markdown file → generate page
        elif os.path.isfile(entry_path) and entry.endswith(".md"):
            dest_file_name = entry.replace(".md", ".html")
            dest_file_path = os.path.join(dest_dir_path, dest_file_name)

            generate_page(
                entry_path,
                template_path,
                dest_file_path,
                basepath,
            )
