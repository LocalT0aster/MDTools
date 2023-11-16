import json
import subprocess

prevType = ""
def create_markdown_tree(node, path=""):
    global prevType
    # If previous type was different, add new line
    nl = "" if prevType == (node["type"] or "") else "\n"
    # Base case: if it's a file, return its markdown link
    if node["type"] == "file":
        filename = node["name"]
        filepath = path + filename
        prevType = node["type"]
        return f"{nl}- [{filename}]({filepath})\n"

    # For directories, we'll create a dropdown
    elif node["type"] == "directory":
        dir_name = node["name"]
        new_path = path + dir_name + "/"
        content = [f"{nl}<details>\n<summary>{dir_name}</summary>\n"]
        
        prevType = node["type"]
        # Recursively process all children (files and sub-directories)
        for child in node["contents"]:
            content.append(create_markdown_tree(child, new_path))
        
        nl = "" if prevType == (node["type"] or "") else "\n"
        content.append(f"{nl}</details>\n")
        prevType = node["type"]
        return "".join(content)

    return ""

def main():
    # Fetch the JSON representation of the directory using tree command
    result = subprocess.run(['tree', '-J'], capture_output=True, text=True)
    data = json.loads(result.stdout)[0]

    markdown_tree = create_markdown_tree(data)
    print(markdown_tree)

if __name__ == "__main__":
    main()
