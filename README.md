# Directory Stack Manager (DSM) Version 1.0

Written for Bash shell, this is useful for managing Linux
directories and easily moving from one directory to another.

To install, it is recommended you clone DSM in your home
directory. Then insert this line into your .bash_aliases:

    source $HOME/DSM/dsm_env.sh

Then when you start a new Bash shell, you can get help on
DSM anytime by entering:

    dh

This will display DSM commands and descriptions. Instead
of using *cd* to change to a new directory, you should now
use *pd* and supply a key for that directory. The key
must be alphanumeric characters. Make it a short
mnemonic. You can omit the key and let DSM auto-create
it for you. Once you have a key associated with a
directory, you can use *g* with that key to go to that
directory (instead of *cd*).

## Future Improvements

1. Support directories with spaces in their names.
2. Return an ERROR from *g* if specified key does not exist.
3. Support directory history and *pop* to step back, *pd* to step forward.

## Funny Behaviors

1. You can use *pd* to change the key of an existing dir, but the old key can still be used by *g* in the same shell. This is because the old key stored as an env var is not unset. To remove it, use *rmk*.
2. If you specify a nonexistent key to *g*, it takes you to your home directory instead of reporting an error.

