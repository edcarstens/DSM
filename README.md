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
it for you.

Limitations

At present, directories with spaces in their name are
not supported.
