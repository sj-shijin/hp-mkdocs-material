import os
import re
import sys


def add_newlines_to_formulas(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 公式前后一个空行
    content = re.sub(
        r"(?!`)\n*(\s*\$\$.+?\$\$)\n*(?!`)",
        "\n\n\g<1>\n\n",
        content,
        flags=re.DOTALL,
    )
    # 将两个以上的\n替换为两个
    content = re.sub(r"\n{2,}", "\n\n", content)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)


def process_directory(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith(".md"):
                print(f"check:{file}")
                add_newlines_to_formulas(os.path.join(root, file))


# The directory to process is now the first command line argument
process_directory(sys.argv[1])
