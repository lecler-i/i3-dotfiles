# pylint: disable=C0111
from qutebrowser.config.configfiles import ConfigAPI  # noqa: F401
from qutebrowser.config.config import ConfigContainer  # noqa: F401

import subprocess

config = config  # type: ConfigAPI # noqa: F821 pylint: disable=E0602,C0103
c = c  # type: ConfigContainer # noqa: F821 pylint: disable=E0602,C0103
# Autogenerated config.py
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# Uncomment this to still load settings configured via autoconfig.yml
# config.load_autoconfig()

# Aliases for commands. The keys of the given dictionary are the
# aliases, while the values are the commands they map to.
# Type: Dict
c.aliases = {'w': 'session-save', 'q': 'quit', 'wq': 'quit --save'}

# Height (in pixels or as percentage of the window) of the completion.
# Type: PercOrInt
c.completion.height = '25%'

# Custom headers for qutebrowser HTTP requests.
# Type: Dict
c.content.headers.custom = {}

# User agent to send. Unset to send the default.
# Type: String
c.content.headers.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'

# Enable host blocking.
# Type: Bool
c.content.host_blocking.enabled = True

# List of URLs of lists which contain hosts to block.  The file can be
# in one of the following formats:  - An `/etc/hosts`-like file - One
# host per line - A zip-file of any of the above, with either only one
# file, or a file   named `hosts` (with any extension).
# Type: List of Url
c.content.host_blocking.lists = ['https://raw.github.com/reek/anti-adblock-killer/master/anti-adblock-killer-filters.txt', 'https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/gambling-porn-social/hosts', 'https://www.malwaredomainlist.com/hostslist/hosts.txt',
                                 'http://someonewhocares.org/hosts/hosts', 'http://winhelp2002.mvps.org/hosts.zip', 'http://malwaredomains.lehigh.edu/files/justdomains.zip', 'https://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&mimetype=plaintext']

# Enable plugins in Web pages.
# Type: Bool
c.content.plugins = False

# Open new windows in private browsing mode which does not record
# visited pages.
# Type: Bool
c.content.private_browsing = False

# Duration (in milliseconds) to wait before removing finished downloads.
# If set to -1, downloads are never removed.
# Type: Int
c.downloads.remove_finished = -1

# Editor (and arguments) to use for the `open-editor` command. The
# following placeholders are defined: * `{file}`: Filename of the file
# to be edited. * `{line}`: Line in which the caret is found in the
# text. * `{column}`: Column in which the caret is found in the text. *
# `{line0}`: Same as `{line}`, but starting from index 0. * `{column0}`:
# Same as `{column}`, but starting from index 0.
# Type: ShellCommand
c.editor.command = ['termite', '-e',
                    "nvim {file} -c 'normal {line}G{column0}l'"]

# Encoding to use for the editor.
# Type: Encoding
c.editor.encoding = 'utf-8'

# Default monospace fonts. Whenever "monospace" is used in a font
# setting, it's replaced with the fonts listed here.
# Type: Font
c.fonts.monospace = '"FantasqueSansMono Nerd Font", "xos4 Terminus", Terminus, Monospace, "DejaVu Sans Mono", Monaco, "Bitstream Vera Sans Mono", "Andale Mono", "Courier New", Courier, "Liberation Mono", monospace, Fixed, Consolas, Terminal'

# Enable Opera-like mouse rocker gestures. This disables the context
# menu.
# Type: Bool
c.input.rocker_gestures = True

# Additional arguments to pass to Qt, without leading `--`. With
# QtWebEngine, some Chromium arguments (see
# https://peter.sh/experiments/chromium-command-line-switches/ for a
# list) will work.
# Type: List of String
c.qt.args = ['disable-reading-from-canvas']

# Show a scrollbar.
# Type: Bool
c.scrolling.bar = True

# Enable smooth scrolling for web pages. Note smooth scrolling does not
# work with the `:scroll-px` command.
# Type: Bool
c.scrolling.smooth = True

# Position of the tab bar.
# Type: Position
# Valid values:
#   - top
#   - bottom
#   - left
#   - right
c.tabs.position = 'left'

# Page to open if :open -t/-b/-w is used without URL. Use `about:blank`
# for a blank page.
# Type: FuzzyUrl
c.url.default_page = 'file:///home/ghjkl/.config/web/startpage/index.html'

# Search engines which can be used via the address bar. Maps a search
# engine name (such as `DEFAULT`, or `ddg`) to a URL with a `{}`
# placeholder. The placeholder will be replaced by the search term, use
# `{{` and `}}` for literal `{`/`}` signs. The search engine named
# `DEFAULT` is used when `url.auto_search` is turned on and something
# else than a URL was entered to be opened. Other search engines can be
# used by prepending the search engine name to the search term, e.g.
# `:open google qutebrowser`.
# Type: Dict
c.url.searchengines = {
    'DEFAULT': 'https://www.startpage.com/do/search?prf=bcbe0abdbd142a625d3e86470f55dfdf&q={}'}

# Page(s) to open at the start.
# Type: List of FuzzyUrl, or FuzzyUrl
c.url.start_pages = 'file:///home/ghjkl/.config/web/startpage/index.html'

# Format to use for the window title. The same placeholders like for
# `tabs.title.format` are defined.
# Type: FormatString
c.window.title_format = '{perc}{title}{title_sep}{current_url} - qutebrowser'

# Bindings for normal mode
config.bind(',a', 'spawn --userscript toggle_host_blocking')
config.bind(',m', 'spawn --userscript spawn_mpv')
config.bind(',p', 'spawn --userscript fill_password')
config.bind(',r', 'spawn --userscript readability')
config.bind(',s', 'spawn --userscript view_source')
config.bind(',t', 'set-cmd-text -s :spawn --userscript add_task +qutebrowser')
config.bind('gi', 'hint inputs')
