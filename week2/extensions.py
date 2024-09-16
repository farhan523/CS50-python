def main():
    file_name = input("File name ").strip().lower()
    extension_to_mime = {
        ".gif": "image/gif",
        ".jpg": "image/jpg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }
    
    for ext, mime_type in extension_to_mime.items():
        if file_name.endswith(ext):
            print(mime_type)
            return
    
    print("application/octet-stream")

main()
