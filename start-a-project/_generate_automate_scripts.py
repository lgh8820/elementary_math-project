#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This script can generate automate scripts for open source python project.
"""

import sys
import datetime
from os import walk, mkdir
from os.path import join, abspath, dirname, basename, relpath


package_name = "ezinstall"
python_version = "python%s%s" % (sys.version_info.major, sys.version_info.minor)
github_username = "MacHu-GWU"
author_name = "Sanhe Hu"
author_email = "husanhe@gmail.com"
maintainer_name = author_name
maintainer_email = author_email
year = str(datetime.datetime.utcnow().year)
s3_bucket = "www.wbh-doc.com"


def write(s, path, encoding="utf-8"):
    """Write string to text file.
    """
    with open(path, "wb") as f:
        f.write(s.encode(encoding))


def read(path, encoding="utf-8"):
    """Read string from text file.
    """
    with open(path, "rb") as f:
        return f.read().decode(encoding)


def generate_files():
    template_dir = join(dirname(abspath(__file__)), "template")
    output_dir = join(dirname(abspath(__file__)), "%s-project" % package_name)
    for src_dir, dir_list, file_list in walk(template_dir):
        # destination directory
        dst_dir = src_dir.replace(template_dir, output_dir, 1)
        if dst_dir.endswith("__package__"):
            dst_dir = dst_dir[:-11] + package_name
        
        # make destination directory
        try:
            mkdir(dst_dir)
        except:
            pass

        # files
        for basename in file_list:
            src = join(src_dir, basename)
            dst = join(dst_dir, basename)
            if dst.endswith(".python"):
                dst = dst[:-7] + ".py"
            
            content = read(src).\
                replace("{{ package_name }}", package_name).\
                replace("{{ python_version }}", python_version).\
                replace("{{ github_username }}", github_username).\
                replace("{{ author_name }}", author_name).\
                replace("{{ author_email }}", author_email).\
                replace("{{ maintainer_name }}", maintainer_name).\
                replace("{{ maintainer_email }}", maintainer_email).\
                replace("{{ year }}", year).\
                replace("{{ s3_bucket }}", s3_bucket)
            write(content, dst)


if __name__ == "__main__":
    generate_files()
