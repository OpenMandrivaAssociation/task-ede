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




%changelog
* Mon Apr 25 2011 Jani Välimaa <wally@mandriva.org> 1.0-5mdv2011.0
+ Revision: 658721
- require lowercase eterm

* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 1.0-4mdv2010.0
+ Revision: 434276
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.0-3mdv2009.0
+ Revision: 242854
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Jul 01 2007 Adam Williamson <awilliamson@mandriva.org> 1.0-1mdv2008.0
+ Revision: 46845
- Import task-ede

