#
# Copyright 2021-2021 Vrije Universiteit Brussel
#
# This file is part of term_rst_post,
# originally created by the HPC team of Vrije Universiteit Brussel (https://hpc.vub.be),
# with support of Vrije Universiteit Brussel (https://www.vub.be),
# the Flemish Supercomputer Centre (VSC) (https://www.vscentrum.be),
# the Flemish Research Foundation (FWO) (http://www.fwo.be/en)
# and the Department of Economy, Science and Innovation (EWI) (http://www.ewi-vlaanderen.be/en).
#
# https://github.com/sisc-hpc/term_rst_post
#
# term_rst_post is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation v3.
#
# term_rst_post is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this code.  If not, see <http://www.gnu.org/licenses/>.
#
##
"""
Unit tests for term_rst_post.filetools

@author: Alex Domingo (Vrije Universiteit Brussel)
"""

import os
import pytest

from term_rst_post import filetools


@pytest.fixture
def ablog_newspost_file(exampledir):
    return os.path.join(exampledir, 'ablog_newspost_simple.rst')


def test_valid_dirpath(tmpdir):
    assert filetools.valid_dirpath(tmpdir) == f"{tmpdir}"


def test_resolve_path(tmpdir):
    test_filename = 'resolve.test'
    test_abspath = os.path.join(tmpdir, test_filename)

    os.chdir(tmpdir)
    assert filetools.resolve_path(test_filename) == test_abspath


def test_change_file_extension(ablog_newspost_file):
    html_file_reference = os.path.basename(ablog_newspost_file).split('.')[0] + '.html'
    html_file = filetools.change_file_extension(ablog_newspost_file, '.html')
    assert f"{html_file}" == html_file_reference


def test_fileobj_extension(ablog_newspost_file):
    with open(ablog_newspost_file) as testfile:
        assert filetools.fileobj_extension(testfile) == '.rst'


def test_rst_path_from_html_link(ablog_newspost_file, exampledir):
    html_link = '../../examples/ablog_newspost_simple'
    rst_file = filetools.rst_path_from_html_link(html_link, exampledir)
    assert ablog_newspost_file == f"{rst_file}"
