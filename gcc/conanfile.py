import re
import os
from textwrap import dedent
from typing import Any, Union, Iterable
from pathlib import Path
import shutil
import filecmp


from conan import ConanFile
from conan.tools.files import get
from conan.tools.env import Environment
from conan.errors import ConanInvalidConfiguration
from conan.tools.gnu.get_gnu_triplet import _get_gnu_triplet


class GccConan(ConanFile):

    name = "gcc"
    user = "bug"
    version = '11.3.0'
    settings: Any = ("os", "arch", "compiler", "build_type")
    options: Any = {
        "libc": [True, False],
        "threads": [False, "posix"],
        "os_target": ["Windows", "Linux"],
        "arch_target": ["x86", "x86_64"],
    }
    package_type = "application"
    default_options = {"libc": True, "threads": "posix"}
    url = "https://www.gnu.org/software/gcc/"
    description = "GCC, the GNU Compiler Collection"
    no_copy_source = True


    def configure(self):
        # record target information in options
        if settings_target := getattr(self, "settings_target", None):
            self.options.os_target = self.options.os_target or settings_target.os
            self.options.arch_target = self.options.arch_target or settings_target.arch


    def requirements(self):
        self.requires(
            'binutils/2.38@bug',
            visible=False,
            options={
                "arch_target": self.options.arch_target,
                "os_target": self.options.os_target,
            },
        )







