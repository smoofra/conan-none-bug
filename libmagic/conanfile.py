import re
from typing import Any

from conan import ConanFile
from conan.tools.files import get, patch
from conan.tools.build import cross_building

class Libmagic(ConanFile):
    name = "libmagic"
    user = "bug"
    version = '5.44'
    settings: Any = ("os", "arch", "compiler", "build_type")
    description = "Implementation of the file(1) command"
    url = "https://www.darwinsys.com/file/"
    license = "similar to BSD-2-Clause"
    no_copy_source = True
    package_type = "static-library"

    def build_requirements(self):
        if self.settings.os == "Macos":
            pass # self.tool_requires("xcode/12.4@bug")
        else:
            self.tool_requires("gcc/11.3.0@bug")
        if cross_building(self):
            self.tool_requires(f"libmagic/{self.version}@bug")

