
import os

def get_files_info(working_directory, directory=None):

    if directory not in working_directory:
        return f"Error: Cannot list '{directory}' as it is outside the permitted working directory"
    
    if directory != dict:
        return f"Error: '{directory}' is not a directory"
    
    else:
        try:
            return f"{directory}: file_size={os.path.getsize(directory)} bytes, is_dir={os.path.isdir(directory)}"
        except OSError as e:
            print(f"Error: {e}")

    