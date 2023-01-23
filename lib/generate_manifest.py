import os
import platform
import json


class ManifestGen:

    verbosity = False

    def __init__(self, verbosity):
        self.verbosity = verbosity

    def manifest(self, manifest_data, msg):
        # get path based on the system because of different path delimeters
        sys = platform.system()
        file_path = os.getcwd()

        if sys == "Linux" or sys == "Darwin":
            file_path += "/"
        elif sys == "Windows":
            file_path += "\\"  # reverse slash has to be escaped

        with open(file_path + "manifest.json", "w") as man:
            data = json.dumps(manifest_data)
            man.write(data)
            if self.verbosity:
                print(f"[+] {msg}!")

    def generate_manifest(self, name, author, version, manifest_version, description, default_popup):

        if self.verbosity:
            print("[+] creating manifest.json ...")

        manifest_data = {
            "name": name,
            "version": version,
            "author": author,
            "description": description,
            "manifest_version": int(manifest_version),
            "action": {
                "default_popup": default_popup
            }
        }

        self.manifest(manifest_data=manifest_data,
                      msg="manifest.json file created")

    def generate_full_manifest(self, name, author, version, manifest_version, description, default_popup):
        if self.verbosity:
            print("[+] creating full manifest.json")

        manifest_data = {
            # Required
            "name": name,
            "author": author,
            "version": version,
            "manifest_version": manifest_version,

            # Recommended
            "description": description,
            "action": {
                "default_popup": default_popup
            },
            "developer": {},
            "icons": {},
            "default_locale": "en",

            # Pick one (or none)
            "browser_action": {},
            "page_action": {},

            # Add any of these that you need
            "background": {"persistent": False, },
            "background": {"persistent": True, },
            "content_scripts": [],
            "content_security_policy": "policyString",
            "homepage_url": "http://path/to/homepage",
            "incognito": "spanning",  # or "split"
            "key": "publicKey",
            "options_page": "aFile.html",
            "permissions": [],
            "requirements": {},
            "update_url": "http://path/to/updateInfo.xml",
            "web_accessible_resources": [],
            "sandbox": []
        }

        self.manifest(manifest_data=manifest_data,
                      msg="full manifest.json file created")
