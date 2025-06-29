
import os

def get_files_info(working_directory, directory=None):

    abs_path_working_dir = os.path.abspath(working_directory)
    joined_paths = os.path.join(abs_path_working_dir, directory)
    joined_paths_abs = os.path.abspath(joined_paths)

    if joined_paths_abs.startswith(abs_path_working_dir) == False:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(joined_paths_abs):
        return f'Error: "{directory}" is not a directory'
    
    else:
        try:
            result_list = []

            for item in os.listdir(joined_paths_abs):

                full_path_to_check = os.path.join(joined_paths_abs, item)
                file_size = 0

                check_dir = os.path.isdir(full_path_to_check)
                file_size = os.path.getsize(full_path_to_check)

                result_list.append(f"{item}: file_size={file_size}, is_dir={check_dir}")
                

            return  "\n".join(result_list)
        
        except Exception as e:
            return f"Error: {e}"
    

    