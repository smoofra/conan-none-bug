import re
import os
from pathlib import Path
from typing import Any
import filecmp

from conan import ConanFile
from conan.errors import ConanInvalidConfiguration
from conan.tools.files import get
from conan.tools.gnu.get_gnu_triplet import _get_gnu_triplet


class BinutilsConan(ConanFile):
    name = "binutils"
    user = "bug"
    version = "2.38"
    homepage = "https://www.gnu.org/software/binutils/"
    url = "https://www.gnu.org/software/binutils/"
    description = "a collection of binary tools."
    settings: Any = ("os", "arch", "compiler", "build_type")
    options: Any = {
        "os_target": ["Windows", "Linux"],
        "arch_target": ["x86", "x86_64"],
    }
    package_type = "application"



