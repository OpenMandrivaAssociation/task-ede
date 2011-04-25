%define name task-ede
%define version 1.0
%define release %mkrel 5

Name: %{name}
Version: %{version}
Release: %{release}
Summary: Metapackage for EDE
Group: Graphical desktop/Other
License: GPL
Requires: ede
Requires: rox
# Explicit require xemacs-extras to avoid the question of xemacs-extras or ctags
Requires: xemacs xemacs-extras
Requires: vim-X11
Requires: abiword
Requires: lyx
Requires: openoffice.org
Requires: graveman
Requires: cooledit
Requires: etranslate
Requires: efluid
Requires: xxgdb
Requires: lbreakout2
Requires: xbill
Requires: gimp
Requires: gqview
Requires: gv
Requires: xdvi
Requires: xpdf
Requires: xsane
Requires: mozilla-firefox
Requires: lynx
Requires: pidgin
Requires: mozilla-thunderbird
Requires: alsaplayer
Requires: mplayer-gui
Requires: xmms
Requires: eterm
Requires: kterm
Requires: drakconf
Requires: rxvt
Requires: xmag
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
This package is a meta-package for the EDE desktop environment. 
Installing it will install all applications in the EDE default menu
layout, along with EDE itself.

%files


