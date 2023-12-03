## Setup Environment for DSM
## Add this line to your .bash_aliases file:
## source $HOME/DSM/dsm_env.sh
export DSM_INSTALL_PATH="$HOME/DSM"
export DSM_CONTEXTS="$DSM_INSTALL_PATH/contexts"
export DSM_DIRS="h $HOME"
export DSM_DESC="#"
export DSM_CONTEXT=""
export DSM_KEY="h"
export DSM_STACK=""
export _h=$HOME
PS1="\[\e]0;\$DSM_CONTEXT \$DSM_KEY \w\a\]\${debian_chroot:+(\$debian_chroot)}\[\033[01;32m\]\h\[\033[00m\]\$ "

alias lc='ls $DSM_CONTEXTS'
alias x='x=$PWD'
alias cc='echo $DSM_DESC'
alias ds='echo $DSM_STACK'
alias dh='cat $DSM_INSTALL_PATH/README.txt'

b() { eval `python3 $DSM_INSTALL_PATH/dsm.py b` ; }
c() { eval `python3 $DSM_INSTALL_PATH/dsm.py c $1` ; }
cpx() { cp $1 $x ; }
d() { python3 $DSM_INSTALL_PATH/dsm.py d $1 ; }
f() { eval `python3 $DSM_INSTALL_PATH/dsm.py f` ; }
g() { eval `python3 $DSM_INSTALL_PATH/dsm.py g $1` ; }
k() { python3 $DSM_INSTALL_PATH/dsm.py k $1 ; }
pd() { test "$#" -lt "1" && echo "ERROR - 1 arg required" && return 100 || cd $1 && eval `python3 $DSM_INSTALL_PATH/dsm.py pd $2` ; }
rmk() { eval `python3 $DSM_INSTALL_PATH/dsm.py rmk $1` ; }
sc() { python3 $DSM_INSTALL_PATH/dsm.py sc $1 ; }
