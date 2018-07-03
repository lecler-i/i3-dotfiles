export XDG_CONFIG_HOME=$HOME/.config
export XDG_CONFIG_HOME=$HOME/.config

export PATH=$PATH:$HOME/.local/bin


[[ -z $DISPLAY && $XDG_VTNR -eq 1 ]] && exec startx