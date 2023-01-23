import os
import platform
from lib.generate_css import GenerateCSS
from lib.generate_js import GenerateJS


class HTMLGen:

    verbosity = False

    def __init__(self, verbosity):
        self.verbosity = verbosity

    def generate_html(self, entry, title):
        if self.verbosity:
            print("[+] Creating entry file ...")

        # get path based on the system because of different path delimeters
        sys = platform.system()
        file_path = os.getcwd()
        gencss = GenerateCSS(self.verbosity)
        genjs = GenerateJS(self.verbosity)

        if sys == "Linux" or sys == "Darwin":
            file_path += "/"
        elif sys == "Windows":
            file_path += "\\"  # reverse slash has to be escaped

        css_path = gencss.get_current_directory(True) + "index.css"
        js_path = genjs.get_current_directory(True) + "index.js"

        data = f"""
            <!DOCTYPE html>\n
            <html lang="en">\n
            <head>\n
                <meta charset="UTF-8">\n
                <meta http-equiv="X-UA-Compatible" content="IE=edge">\n
                <meta name="viewport" content="width=device-width, initial-scale=1.0">\n
                <title>{title}</title>\n
                <link rel="stylesheet" type="text/css" href="{css_path}">\n
            </head>\n
            <body>\n
                
                <script src="{js_path}"></script>\n
            </body>\n
            </html>
        """

        with open(file_path + entry, "w") as man:
            man.write(data)

            if self.verbosity:
                print("[+] Entry file generated created!")
