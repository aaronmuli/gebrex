import os
import platform


class GenerateCSS:

    verbosity = False

    def __init__(self, verbosity):
        self.verbosity = verbosity

    def get_current_directory(self, css=False):
        # get path based on the system because of different path delimeters
        sys = platform.system()
        cwd = os.getcwd()  # get the current working directory

        if not css:
            if sys == "Linux" or sys == "Darwin":
                cwd += "/"
            elif sys == "Windows":
                cwd += "\\"  # reverse slash has to be escaped
        elif css:
            if sys == "Linux" or sys == "Darwin":
                cwd += "/css/"
            elif sys == "Windows":
                cwd += "\\css\\"  # reverse slash has to be escaped

        return cwd

    def create_css_directory(self):

        if self.verbosity:
            print("[+] Creating css directory ...")
        cwd = self.get_current_directory()
        os.mkdir(cwd + "css")

        if self.verbosity:
            print("[+] CSS directory created!")

        self.generate_css()

    def generate_css(self):
        if self.verbosity:
            print("[+] Generating css file ...")

        file_path = self.get_current_directory(True)
        with open(file_path + "index.css", "w") as file:
            file.write("")

            if self.verbosity:
                print("[+] CSS file generated!")
