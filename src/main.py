import sys

from generate_page import generate_pages_recursive
from static_to_public import static_to_public

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    print("Copying static files to public directory...")
    static_to_public()

    print("Generating content...")
    generate_pages_recursive(
        dir_path_content,
        template_path,
        dir_path_public,
        basepath,
    )


if __name__ == "__main__":
    main()
