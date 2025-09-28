"""
[vmdoc:description] Utility functions for installing emscripten, which is a compiler to compile c++ code for the web [vmdoc:enddescription] 
"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[0]))
sys.path.append(str(Path(__file__).resolve().parents[1]))
sys.path.append(str(Path(__file__).resolve().parents[2]))
sys.path.append(str(Path(__file__).resolve().parents[3]))
sys.path.append(str(Path(__file__).resolve().parents[4]))
sys.path.append(str(Path(__file__).resolve().parents[5]))

from vizpip_env.lib.pyUtil import *
from vizpip_env.installer import install_package


def get_compiler_path():
    if platform.system() == "Windows": # Windows
        return get_directory_path(__file__, 1) + "/emsdk/upstream/emscripten/em++.bat"
    else:
        return get_directory_path(__file__, 1) + "/emsdk/upstream/emscripten/em++"
    

def get_output_file_extension():
    return ".html"


def install():
    install_package("emsdk")

    if platform.system() == "Linux":
        emsdk_path = get_directory_path(__file__, 1) + "/emsdk/emsdk"
        run_command('chmod +x "' + emsdk_path + '"')
        run_command('"' + emsdk_path + '" install latest')
        run_command('"' + emsdk_path + '" activate latest')
    elif platform.system() == "Windows":
        emsdk_path = get_directory_path(__file__, 1) + "/emsdk/emsdk"
        run_command('"' + emsdk_path + '" install latest')
        run_command('"' + emsdk_path + '" activate latest')


if __name__ == "__main__":
    install()