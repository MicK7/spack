# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class GprofngGui(AutotoolsPackage):
    """A graphical environment to analyze the performance data generated by the gprofng"""

    homepage = "https://sourceware.org/binutils/wiki/gprofng"
    url = "https://ftp.gnu.org/gnu/gprofng-gui/gprofng-gui-1.1.tar.gz"
    git = "https://git.savannah.gnu.org/git/gprofng-gui.git"

    maintainers("pramodk")

    license("GPL-3.0-only", checked_by="pramodk")

    version("develop", branch="master")
    version("1.1", sha256="94fa577b856f00b89a2832771a265e221818b88dc0b36d8bca365efe6f08e12a")
    version("1.0", sha256="c88da8ec91a9943636301fb7da9d337fe0851d874f8f7a4d2169bd859ee72dbc")

    depends_on("autoconf", type="build", when="@develop")
    depends_on("automake", type="build", when="@develop")
    depends_on("libtool", type="build", when="@develop")

    depends_on("java", type=("build", "run"))
