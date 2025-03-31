# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pandas>=1.0.0",
#   "numpy>=1.0.0",
#   "sentence-transformers>=2.0.0",
#   "scikit-learn>=0.24.0",
#   "fastapi>=0.68.0",
#   "openpyxl>=3.0.0",
#   "uvicorn>=0.14.0",
#   "python-multipart>=0.0.5",
#   "faiss-cpu >=1.7.2",
# ]
# ///


import os
import shutil
import tempfile
from fastapi import UploadFile

async def upload(upload_file: UploadFile) -> str:
    """
    Save an upload file temporarily and return the path to the saved file.
    """
    try:
        # Create a temporary directory
        temp_dir = tempfile.mkdtemp()
        
        # Create a path to save the file
        file_path = os.path.join(temp_dir, upload_file.filename)
        
        # Save the file
        with open(file_path, "wb") as f:
            contents = await upload_file.read()
            f.write(contents)
        
        # Return the path to the saved file
        return file_path
    except Exception as e:
        # Clean up the temporary directory if an error occurs
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        raise e