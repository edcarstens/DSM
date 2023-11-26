## Setup Environment for DSM
## Add this line to your .bash_aliases file:
## source $HOME/DSM/dsm_env.sh
export DSM_INSTALL_PATH="$HOME/DSM"
export DSM_CONTEXTS="$DSM_INSTALL_PATH/contexts"
export DSM_DIRS=""
export DSM_DESC="#"
g() { test "$#" -lt "1" && echo "ERROR - 1 arg required" && return 100 || eval cd '$'_$1 ; }
pd() { test "$#" -lt "1" && echo "ERROR - 1 arg required" && return 100 || cd $1 && export DSM_KEY=`python3 $DSM_INSTALL_PATH/dsm_key.py $2` && eval export _$DSM_KEY=$PWD && DSM_DIRS=`python3 $DSM_INSTALL_PATH/dsm_push.py $DSM_KEY` ; }
d() { python3 $DSM_INSTALL_PATH/dsm_dirs.py $DSM_DIRS ; }
sc() { test "$#" -lt "1" && echo "ERROR - 1 arg required" && return 100 || echo $DSM_DESC > $DSM_CONTEXTS/$1 && python3 $DSM_INSTALL_PATH/dsm_dirs.py $DSM_DIRS >> $DSM_CONTEXTS/$1 ; }
c() { test "$#" -lt "1" && echo "ERROR - 1 arg required" && return 100 || source $DSM_INSTALL_PATH/dsm_unset.sh && DSM_DIRS=`python3 $DSM_INSTALL_PATH/dsm_load_context.py $1` && source $DSM_INSTALL_PATH/dsm_set.sh && DSM_DESC=`python3 $DSM_INSTALL_PATH/dsm_load_context.py $1 desc`; }
alias lc='ls $DSM_CONTEXTS'
alias x='x=$PWD'
cpx() { cp $1 $x ; }
alias cc='echo $DSM_DESC'
alias dh='cat $DSM_INSTALL_PATH/README.txt'
rmk() { test "$#" -lt "1" && echo "ERROR - 1 arg required" && return 100 || DSM_DIRS=`python3 $DSM_INSTALL_PATH/dsm_rmkey.py $1` && eval unset _$1 ; }

