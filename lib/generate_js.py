import os
import platform


class GenerateJS:

    verbosity = False

    def __init__(self, verbosity):
        self.verbosity = verbosity

    def get_current_directory(self, js=False):
        # get path based on the system because of different path delimeters
        sys = platform.system()
        cwd = os.getcwd()  # get the current working directory

        if not js:
            if sys == "Linux" or sys == "Darwin":
                cwd += "/"
            elif sys == "Windows":
                cwd += "\\"  # reverse slash has to be escaped
        elif js:
            if sys == "Linux" or sys == "Darwin":
                cwd += "/js/"
            elif sys == "Windows":
                cwd += "\\js\\"  # reverse slash has to be escaped

        return cwd

    def create_js_directory(self):

        if self.verbosity:
            print("[+] Creating js directory ...")
        cwd = self.get_current_directory()
        os.mkdir(cwd + "js")

        if self.verbosity:
            print("[+] JS directory created!")

        self.generate_js()

    def generate_js(self):
        if self.verbosity:
            print("[+] Generating js file ...")

        file_path = self.get_current_directory(True)
        with open(file_path + "index.js", "w") as file:
            file.write("")
            if self.verbosity:
                print("[+] JS file generated!")
