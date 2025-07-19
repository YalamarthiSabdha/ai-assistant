import os

def parse_command(command, base_path):
    command = command.lower().strip()

    if not os.path.isdir(base_path):
        return f"❌ Invalid base path: {base_path}"

    # Extract intent
    if "create" in command:
        if "file" in command:
            name = extract_name(command, "file")
            return create_file(name, base_path)
        elif "folder" in command or "directory" in command:
            name = extract_name(command, "folder")
            return create_folder(name, base_path)
        else:
            return "⚠️ Please specify what to create (file/folder)."

    elif "delete" in command:
        if "file" in command:
            name = extract_name(command, "file")
            return delete_file(name, base_path)
        elif "folder" in command or "directory" in command:
            name = extract_name(command, "folder")
            return delete_folder(name, base_path)
        else:
            return "⚠️ Please specify what to delete (file/folder)."

    elif "open" in command:
        name = extract_name(command, "file")
        return open_item(name, base_path)

    return "⚠️ Command not understood. Try 'create a file xyz.txt', 'delete folder abc', or 'open xyz.txt'."

# --- Helper functions ---
def extract_name(command, keyword):
    parts = command.split()
    try:
        index = parts.index(keyword)
        return ' '.join(parts[index + 1:]).strip()
    except ValueError:
        return ""

def create_file(name, path):
    try:
        full_path = os.path.join(path, name)
        with open(full_path, "w") as f:
            f.write("")
        return f"📄 File '{name}' created at {path}"
    except Exception as e:
        return f"❌ Failed to create file: {e}"

def create_folder(name, path):
    try:
        full_path = os.path.join(path, name)
        os.makedirs(full_path, exist_ok=True)
        return f"📁 Folder '{name}' created at {path}"
    except Exception as e:
        return f"❌ Failed to create folder: {e}"

def delete_file(name, path):
    full_path = os.path.join(path, name)
    if os.path.exists(full_path):
        try:
            os.remove(full_path)
            return f"🗑️ File '{name}' deleted from {path}"
        except Exception as e:
            return f"❌ Error deleting file: {e}"
    return f"❗ File '{name}' not found in {path}"

def delete_folder(name, path):
    full_path = os.path.join(path, name)
    if os.path.exists(full_path):
        try:
            os.rmdir(full_path)
            return f"🗑️ Folder '{name}' deleted from {path}"
        except Exception as e:
            return f"❌ Error deleting folder: {e}"
    return f"❗ Folder '{name}' not found in {path}"

def open_item(name, path):
    try:
        full_path = os.path.join(path, name)
        os.startfile(full_path)
        return f"📂 Opened '{name}'"
    except Exception as e:
        return f"❌ Couldn't open: {e}"
