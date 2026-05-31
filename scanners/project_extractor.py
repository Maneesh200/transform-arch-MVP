import zipfile
import os
import shutil

UPLOAD_DIR = "uploads"

def extract_project(uploaded_file):

    project_name = uploaded_file.name.replace(".zip", "")

    extract_path = os.path.join(UPLOAD_DIR, project_name)

    if os.path.exists(extract_path):
        shutil.rmtree(extract_path)

    os.makedirs(extract_path, exist_ok=True)

    zip_path = os.path.join(UPLOAD_DIR, uploaded_file.name)

    with open(zip_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_path)

    return extract_path