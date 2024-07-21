import os
import shutil

def organize_files(path):
    file_categories = {
        'Photos': ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff'],
        'Documents': {
            'PDFs': ['pdf'],
            'PPTs': ['ppt', 'pptx'],
            'Word': ['doc', 'docx'],
            'Excel': ['xls', 'xlsx']
        },
        'Videos': ['mp4', 'mkv', 'avi', 'mov', 'wmv'],
        'Audio': ['mp3', 'wav'],
        'Archives': ['zip', 'rar']
    }
    
    files = os.listdir(path)
    
    for file in files:
        if not os.path.isfile(os.path.join(path, file)):
            continue
        
        filename, ext = os.path.splitext(file)
        ext = ext[1:].lower()
        
        category = 'Others'
        subfolder = None

        for cat, subcategories in file_categories.items():
            if isinstance(subcategories, dict):
                for subcat, extensions in subcategories.items():
                    if ext in extensions:
                        category = cat
                        subfolder = subcat
                        break
            elif ext in subcategories:
                category = cat
                break
        
        if category == 'Documents' and subfolder is None:
            subfolder = 'Others'
        
        dest_dir = os.path.join(path, category, subfolder if subfolder else '')
        src_file = os.path.join(path, file)
        dest_file = os.path.join(dest_dir, file)

        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        shutil.move(src_file, dest_file)

if __name__ == "__main__":
    path = input("Enter folder path: ").strip()
    organize_files(path)
