import sys

from cx_Freeze import setup, Executable

companyName = "Shivam kumar"
productName = "Youtube Video Downloader Free"

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable("main.py", base=base, icon="icon.ico")]
filesIncluded = ["icon.ico"]

packages = ["threading", "tkinter", "pytube"]
bdistMSIOptions = {
    "add_to_path": False,
    "initial_target_dir": r"[ProgramFilesFolder]\%s\%s" % (companyName, productName)
}
options = {
    "build_exe": {
        "packages": packages,
        "include_files": filesIncluded
    },
    "bdist_msi": bdistMSIOptions
}

setup(
    name="ytDownloader.exe",
    author="Shivam kumar",
    options=options,
    version="1.0.0",
    description="Download any Youtube Video only by using link",
    executables=executables
)
