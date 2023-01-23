from os import system, name
from lib.generate_manifest import ManifestGen
from lib.generate_css import GenerateCSS
from lib.generate_js import GenerateJS
from lib.generate_html import HTMLGen


class Gebrex:
    # user variables
    name = ''
    version = ''
    author = ''
    description = ''
    manifest_version = ''
    default_popup = ''

    # program variables
    manifest_only = False
    full = False
    show_version = False
    gebrex_version = "0.0.1"
    verbosity = False

    def __init__(self, manifest_only, full, version, verbosity):
        self.manifest_only = manifest_only
        self.full = full
        self.show_version = version
        self.verbosity = verbosity

    def clear_terminal(self):
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

    def generate_files(self):

        self.clear_terminal()
        print("[*] Initializing project ...", end="\n\n")

        mangen = ManifestGen(self.verbosity)
        mangen.generate_manifest(
            self.name,
            self.author,
            self.version,
            self.manifest_version,
            self.description,
            self.default_popup,
        )

        if self.full:
            mangen.generate_full_manifest(
                self.name,
                self.author,
                self.version,
                self.manifest_version,
                self.description,
                self.default_popup,
            )

        if not self.manifest_only:
            gencss = GenerateCSS(self.verbosity)
            genjs = GenerateJS(self.verbosity)
            genhtml = HTMLGen(self.verbosity)

            gencss.create_css_directory()
            genjs.create_js_directory()
            genhtml.generate_html(self.default_popup, self.name)

        print("")
        print("[*] Done!")

    def valid_info(self):
        if self.name == "":
            self.name = "New browser extension"
        if self.author == "":
            self.author = "Mangene"
        if self.version == "":
            self.version = "1.0.0"
        if self.description == "":
            self.description = "simple browser extension"
        if self.manifest_version == "":
            self.manifest_version = 3
        if self.default_popup == "" and not self.manifest_only:
            self.default_popup = "index.html"

        self.generate_files()

    def get_info(self):
        print("[*] Initializing project ...", end="\n\n")
        self.name = input(
            "[*] Name of extension or leave default '(default name)': ")
        self.version = input(
            "[*] Extension version or leave default '(1.0.0)': ")
        self.author = input("[*] Author or leave default '(mangene)': ")
        self.description = input(
            "[*] Enter a description or leave default '(simple browser extension)': ")
        self.manifest_version = input(
            "[*] Manifest version or leave default (3): ")
        if not self.manifest_only:
            self.default_popup = input(
                "[*] Root file or leave default '(index.html)': ")

        self.valid_info()
