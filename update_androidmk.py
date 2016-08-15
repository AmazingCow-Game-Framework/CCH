#!/usr/bin/python
#coding=utf-8
##----------------------------------------------------------------------------##
##       █      █                                                             ##
##       ████████                                                             ##
##     ██        ██     File    : update_androidmk.py                         ##
##    ███  █  █  ███    Project : Cocos2d_Compile_Helpers                     ##
##    █ █        █ █    Author  : N2OMatt                                     ##
##     ████████████     Date    : Mon Aug 15 13:31:34 2016 UTC                ##
##   █              █                                                         ##
##  █     █    █     █  Copyright (c) 2016                                    ##
##  █     █    █     █  AmazingCow - www.AmazingCow.com                       ##
##   █              █                                                         ##
##     ████████████     This File / Project is PROPRIETARY                    ##
##                                                                            ##
##                          Enjoy :)                                          ##
##----------------------------------------------------------------------------##


################################################################################
## Imports                                                                   ##
################################################################################
import os;
import sys;
import getopt;


################################################################################
## Constants                                                                  ##
################################################################################
kORIGINAL_FILE = os.path.join(os.path.split(__file__)[0],"Android_Original.mk");
kTARGET_FILE   = "proj.android-studio/app/jni/Android.mk";


################################################################################
## Functions                                                                  ##
################################################################################
def add_include_directories(target_file, lines):
    kWRITE_FORMAT_WITH_ESCAPE    = "    $(LOCAL_PATH)/../../../{0} \\\n";
    kWRITE_FORMAT_WITH_NO_ESCAPE = "    $(LOCAL_PATH)/../../../{0} \n";

    write_lines(
        target_file,
        lines,
        kWRITE_FORMAT_WITH_ESCAPE,
        kWRITE_FORMAT_WITH_NO_ESCAPE
    );


def add_game_sources(target_file, lines):
    kWRITE_FORMAT_WITH_ESCAPE    = "    ../../../{0} \\\n";
    kWRITE_FORMAT_WITH_NO_ESCAPE = "    ../../../{0} \n";

    write_lines(
        target_file,
        lines,
        kWRITE_FORMAT_WITH_ESCAPE,
        kWRITE_FORMAT_WITH_NO_ESCAPE
    );


def write_lines(target_file, lines, espace_format, no_escape_format):
    clean_lines = [];
    for line in lines:
        if(line == "\n" or line.startswith("--")):
            continue;
        clean_lines.append(line);

    lines = clean_lines;

    ## We don't want the last line to be escaped
    ## so write all lines -1 with escape and
    ## let the last unescaped.
    for i in xrange(len(lines) -1):
        line = lines[i].replace("\n", "");
        write_line(target_file, espace_format.format(line));

    last_line = lines[-1];
    write_line(target_file, no_escape_format.format(last_line));

    ## Write a new line.
    write_line(target_file, "\n");




def add_local_module_name(target_file, line, game_name):
    line = line.replace(
            "__UPDATE_CMAKE_GAME_NAME_LOCAL_MODULE__",
            game_name + "_shared"
    );

    write_line(target_file, line);

def add_local_module_filename(target_file, line, game_name):
    line = line.replace(
            "__UPDATE_CMAKE_GAME_NAME_LOCAL_MODULE_FILENAME__",
            "lib" + game_name
    );

    write_line(target_file, line);



################################################################################
## Helpers                                                                    ##
################################################################################
def write_line(target_file, line):
    target_file.write(line);


def canonize(path):
    return os.path.abspath(os.path.expanduser(path));


################################################################################
## Script Initialization                                                      ##
################################################################################
def main():
    game_name             = None;
    working_dir           = None;
    game_sources_def_path = None;
    include_dirs_def_path = None;

    ## COWTODO: Clean up the parsing stuff.
    ## Parse the command line options.
    options = getopt.gnu_getopt(
        sys.argv[1:],
        "",
        ["game-name=",
         "working-dir=",
         "game-sources=",
         "include-dirs="]
    );

    for key, value in options[0]:
        key = key.lstrip("-");
        if(key == "game-name"):
            game_name = value;
        elif(key == "working-dir"):
            working_dir = canonize(value);
        elif(key == "game-sources"):
            game_sources_def_path = canonize(value);
        elif(key == "include-dirs"):
            include_dirs_def_path = canonize(value);

    if(game_name             is None or \
       working_dir           is None or \
       game_sources_def_path is None or \
       include_dirs_def_path is None):
        print "Missing parameters..."
        exit(1);

    original_file_path = canonize(kORIGINAL_FILE);
    target_file_path   = canonize(os.path.join(working_dir, kTARGET_FILE));

    print "Update the Android.mk";
    print "-----------";
    print "CWD:        %s" %(os.getcwd());
    print "Working dir %s" %(working_dir);
    print "-----------";
    print "Original File: %s" %(original_file_path);
    print "Target File  : %s" %(target_file_path);
    print "-----------";
    print "Game Sources Def:        %s" %(game_sources_def_path);
    print "Include Directories Def: %s" %(include_dirs_def_path);
    print "-----------";
    print "Running..."

    ## Read the contents of the files.
    original_file_lines     = open(original_file_path).readlines();
    include_dir_file_lines  = open(include_dirs_def_path).readlines();
    game_sources_file_lines = open(game_sources_def_path).readlines();

    ## Open the target file for writting..
    target_file = open(target_file_path, "w");


    for line in original_file_lines:
        if("__UPDATE_CMAKE_INCLUDE_DIRECTORIES__" in line):
            add_include_directories(target_file, include_dir_file_lines);

        elif("__UPDATE_CMAKE_GAME_SOURCES__" in line):
            add_game_sources(target_file, game_sources_file_lines);

        elif("__UPDATE_CMAKE_GAME_NAME_LOCAL_MODULE__" in line):
            add_local_module_name(target_file, line, game_name);

        elif("__UPDATE_CMAKE_GAME_NAME_LOCAL_MODULE_FILENAME__" in line):
            add_local_module_filename(target_file, line, game_name);

        else:
            write_line(target_file, line);

    target_file.close();

main();
