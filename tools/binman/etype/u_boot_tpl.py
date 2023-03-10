# SPDX-License-Identifier: GPL-2.0+
# Copyright (c) 2016 Google, Inc
# Written by Simon Glass <sjg@chromium.org>
#
# Entry-type module for tpl/u-boot-tpl.bin
#

from binman.entry import Entry
from binman.etype.blob import Entry_blob

class Entry_u_boot_tpl(Entry_blob):
    """U-Boot TPL binary

    Properties / Entry arguments:
        - filename: Filename of u-boot-tpl.bin (default 'tpl/u-boot-tpl.bin')

    This is the U-Boot TPL (Tertiary Program Loader) binary. This is a small
    binary which loads before SPL, typically into on-chip SRAM. It is
    responsible for locating, loading and jumping to SPL, the next-stage
    loader. Note that SPL is not relocatable so must be loaded to the correct
    address in SRAM, or written to run from the correct address if direct
    flash execution is possible (e.g. on x86 devices).

    SPL can access binman symbols at runtime. See :ref:`binman_fdt`.

    in the binman README for more information.

    The ELF file 'tpl/u-boot-tpl' must also be available for this to work, since
    binman uses that to look up symbols to write into the TPL binary.

    Note that this entry is automatically replaced with u-boot-tpl-expanded
    unless --no-expanded is used or the node has a 'no-expanded' property.
    """
    def __init__(self, section, etype, node):
        super().__init__(section, etype, node, auto_write_symbols=True)
        self.elf_fname = 'tpl/u-boot-tpl'

    def GetDefaultFilename(self):
        return 'tpl/u-boot-tpl.bin'
