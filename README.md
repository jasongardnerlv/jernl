#Jernl

###Daily Journal as a Sublime Text 3 Plugin

##Summary
This project provides a way of using Sublime Text to maintain a journal/notes/snippets/etc, with
the ability to tag entries and search for them later.

##Installation
Create a directory, such as "jernl", in your Sublime Text installation's _Packages_ subdirectory.
Place the contents of this project in this directory.

_note:_ The syntax highlighting relies on the use of the Sunburst color theme in Sublime.  If using
another theme, the colors may not appear ideal.  YMMV

##Configuration
Open Sublime Text's User Settings, and add the setting __jernl-dir__.  Set the value to the absolute
path of a directory you would like to use for your jernl files.

##Opening your Journal and Adding New Entries
You can trigger Jernl one of three ways:

1. Type "Jernl" into Sublime Text's Command Palette
1. Select "Jernl" from the Tools menu
1. Using the default keystroke: super+ctrl+j

This triggers a _quick panel_ to select a Jernl command.

If your Jernl file is not currently open in Sublime, you will have a command to __open__ it.
If the file is open, you will have a command to add a __new entry__.  In either case, __search__
is available as a command as well.

Each entry in the Jernl file has the following format:

```
**** 01/01/2015 ************************************************************************

  > This is my entry title - indented 2 spaces with a > and then another space

    This is the entry content.

    This can be anything (any format), just needs to be indented 4 spaces

```

The __New Entry__ command will start a new entry for you, following this format.  A syntax
highlighting file is provided to colorize the different parts of an entry accordingly.

Jernl files will automatically rollover every year.

##Tagging and Searching Entries
When adding entries, you can optionally add tags to the end of any entry title, surrounding with
_@_ symbols

```
**** 01/01/2015 ************************************************************************

  > How to copy a file on Linux @bash,cp,linux@

    $ cp file1.txt file2.txt
```

Once you've added tags, you can use Jernl's __Search__ command.  After invoking it, you're presented
with another _quick panel_, allowing you to search through your available tags.  After choosing a tag,
you get one more _quick panel_, which shows you the title of entries that have the selected tag.
Choosing an entry in the list will take you directly to that entry (opening the corresponding file, if nec.)

##License
Licensed under the [WTFPL](http://www.wtfpl.net/) license :)
