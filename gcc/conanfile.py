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

    @property
    def settings_for_target(self):
        if settings_target := getattr(self, "settings_target", None):
            return settings_target
        # It seems when gcc is tool_required from another package building in the
        # build context, settings_target is None.   By definition in this case what's
        # need is a compiler for the build machine, so host, build and target
        # platforms are all the same.  Therefore, if settings_target is not
        # available, default to building a native compiler for host platform
        #
        # see: https://github.com/conan-io/conan/issues/13515
        return self.settings

    @property
    def arch_target(self):
        return self.options.arch_target or self.settings_for_target.arch

    @property
    def os_target(self):
        return self.options.os_target or self.settings_for_target.os

    def validate(self):
        if not self.options.os_target or not self.options.arch_target:
            raise Exception("oh no")

    def configure(self):
        self.options.arch_target = self.arch_target
        self.options.os_target = self.os_target

    def requirements(self):
        self.requires(
            'binutils/2.38@bug',
            visible=False,
            options={
                "arch_target": self.arch_target,
                "os_target": self.os_target,
            },
        )







