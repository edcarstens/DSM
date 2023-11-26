Directory Stack Manager (DSM)

Written for Bash shell, this is useful for managing Linux
directories and easily moving from one directory to another.

To install, it is recommended you clone DSM in your home
directory. Then insert this line into your .bash_aliases:

source $HOME/DSM/dsm_env.sh

Then when you start a new Bash shell, you can get help on
DSM anytime by entering:

dh

This will display DSM commands and descriptions. Instead
of using 'cd' to change to a new directory, you should now
use 'pd' and supply a key for that directory. The key
must be alphanumeric characters. Make it a short
mnemonic. You can omit the key and let DSM auto-create
it for you. Once you have a key associated with a
directory, you can use 'g' with that key to go to that
directory (instead of 'cd').

Future Improvements

Support directories with spaces in their names.
Return an ERROR from 'g' if specified key does not exist.
Support directory history and 'pop' to step back, 'pd' to step forward.

