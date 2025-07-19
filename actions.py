import os
import subprocess
import platform
import shutil
import stat

def create_file(filepath, content=""):
    try:
        filepath = os.path.abspath(filepath)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"File '{filepath}' created."
    except Exception as e:
        return f"Error creating file: {e}"

def delete_file(filepath):
    try:
        filepath = os.path.abspath(filepath)
        if not os.path.exists(filepath):
            return f"File '{filepath}' not found."
        confirm = input(f"Are you sure you want to delete file '{filepath}'? (yes/no): ")
        if confirm.lower() != "yes":
            return "File deletion canceled by user."
        os.remove(filepath)
        return f"File '{filepath}' deleted."
    except Exception as e:
        return f"Error deleting file: {e}"

def open_file(filepath):
    try:
        filepath = os.path.abspath(filepath)
        if platform.system() == "Windows":
            os.startfile(filepath)
        elif platform.system() == "Darwin":
            subprocess.run(["open", filepath])
        else:
            subprocess.run(["xdg-open", filepath])
        return f"Opened file '{filepath}'"
    except Exception as e:
        return f"Error opening file: {e}"

def modify_file(filepath, content):
    try:
        filepath = os.path.abspath(filepath)
        with open(filepath, 'a', encoding='utf-8') as f:
            f.write("\n" + content)
        return f"Modified file '{filepath}' with new content."
    except Exception as e:
        return f"Error modifying file: {e}"

def close_file(filepath):
    return f"Simulated closing of file '{filepath}'"

def create_folder(folder_path):
    try:
        folder_path = os.path.abspath(folder_path)
        os.makedirs(folder_path, exist_ok=True)
        return f"Folder '{folder_path}' created."
    except Exception as e:
        return f"Error creating folder: {e}"

def delete_folder(folder_path):
    def onerror(func, path, exc_info):
        os.chmod(path, stat.S_IWRITE)
        func(path)
    try:
        folder_path = os.path.abspath(folder_path)
        if not os.path.exists(folder_path):
            return f"Folder '{folder_path}' not found."
        if os.listdir(folder_path):
            confirm = input(f"Folder '{folder_path}' is not empty. Delete all contents? (yes/no): ")
            if confirm.lower() != "yes":
                return "Folder deletion canceled by user."
        shutil.rmtree(folder_path, onerror=onerror)
        return f"Folder '{folder_path}' and all contents deleted."
    except Exception as e:
        return f"Error deleting folder: {e}"

def open_folder(folder_path):
    try:
        folder_path = os.path.abspath(folder_path)
        if not os.path.isdir(folder_path):
            return f"Folder '{folder_path}' does not exist."
        if platform.system() == "Windows":
            os.startfile(folder_path)
        elif platform.system() == "Darwin":
            subprocess.run(["open", folder_path])
        else:
            subprocess.run(["xdg-open", folder_path])
        return f"Opened folder: {folder_path}"
    except Exception as e:
        return f"Error opening folder: {e}"
