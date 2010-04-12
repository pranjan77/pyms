"""
Provides helper functions for MID processing
"""

 #############################################################################
 #                                                                           #
 #    PyMS software for processing of metabolomic mass-spectrometry data     #
 #    Copyright (C) 2005-2010 Vladimir Likic                                 #
 #                                                                           #
 #    This program is free software; you can redistribute it and/or modify   #
 #    it under the terms of the GNU General Public License version 2 as      #
 #    published by the Free Software Foundation.                             #
 #                                                                           #
 #    This program is distributed in the hope that it will be useful,        #
 #    but WITHOUT ANY WARRANTY; without even the implied warranty of         #
 #    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #
 #    GNU General Public License for more details.                           #
 #                                                                           #
 #    You should have received a copy of the GNU General Public License      #
 #    along with this program; if not, write to the Free Software            #
 #    Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.              #
 #                                                                           #
 #############################################################################

from pyms.Utils.Error import error
from pyms.MIDs.Class import MID_table
from pyms.Utils.IO import file_lines
from pyms.Utils.Time import time_str_secs

def parse_ion_defs(in_file):

    """
    @summary: Read ion definitions and return as a list of MID_table objects

    @param in_file: The name of the file containing ion definitions
    @type in_file: StringType

    @return: Empty MID_table object list with compound names, 
        retention times, diagnostic ions and mdv sizes set
    @rtype: ListType

    @author: Milica Ng
    @author: Vladimir Likic
    """

    lines = file_lines(in_file, filter=True)
    mid_table_list = []

    for line in lines:

        # parse input lines
        items = line.split(',')

        # each MID specification must have exactly 4 elements
        if len(items) != 4:
            print "\n Input file: ", in_file
            print " Line: ", line
            error("A MID specification must have exactly 4 elements")

        compound_name = items[0]
        rt = time_str_secs(items[1]) # convert to seconds
        diagnostic_ion = int(items[2])
        mdv_size = int(items[3])

        # set compound name, retention time, diagnostic ions and MDV size
        mid_table = MID_table(compound_name, rt, diagnostic_ion, mdv_size)

        # store MID table in MID table list
        mid_table_list.append(mid_table)

    return mid_table_list

def parse_data_defs(in_file):

    """
    @summary: Read data file names and return as a list

    @param in_file: The name of the file containing data file names
    @type in_file: StringType

    @return: The list of data file names
    @rtype: ListType

    @author: Milica Ng
    @author: Vladimir Likic
    """

    lines = file_lines(in_file, filter=True)

    data_files = []  
    for line in lines:
        data_files.append(line)

    return data_files

def write_mid_tables(mid_table_list, out_file):

    """
    @summary: Write MID tables, including any warnings, to out_file

    @param mid_table_list: List of MID tables 
    @type mid_table_list: ListType
    @param out_file: The name of the file used for writing
    @type out_file: StringType

    @return: None
    @rtype: NoneType

    @author: Milica Ng
    """
    for mid_table in mid_table_list:       
        mid_table.write(out_file)

