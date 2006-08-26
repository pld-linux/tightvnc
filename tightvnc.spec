# TODO:
# - tightvnc.init
# - segfaults on amd64
Summary:	tightvnc - application based on the VNC version 3.3.3r2
Summary(pl):	tightvnc - aplikacja bazuj±ca na VNC w wersji 3.3.3r2
Name:		tightvnc
Version:	1.3.8
Release:	0.2
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/vnc-tight/%{name}-%{version}_unixsrc.tar.bz2
# Source0-md5:	9b9b0465834289d1b7899982c0096440
Source1:	%{name}.desktop
Source2:	%{name}48.png
Patch0:		%{name}-vncserver.patch
Patch1:		%{name}-imake.patch
Patch2:		%{name}-security.patch
Patch3:		%{name}-imake-tmpdir.patch
URL:		http://www.tightvnc.com/
BuildRequires:	cpp
BuildRequires:	libjpeg-devel
BuildRequires:	xorg-cf-files >= 1.0.1-0.3
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-util-gccmakedep
BuildRequires:	xorg-util-imake
BuildRequires:	zlib
Provides:	vnc-client
Obsoletes:	vnc
# server proc crashes atm
ExcludeArch:	amd64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VNC is a great client/server software package allowing remote network
access to graphical desktops. TightVNC is optimized to work over slow
network connections such as low-speed modem links. While oroginal VNC
may be verry slow when your connection is not fast enough, with
TightVNC you can work remotely almost in real time in most
environments.

%description -l pl
VNC jest wspania³ym programem klient/serwer umo¿liwiaj±cym zdalny
dostêp do graficznych pulpitów. TightVNC jest zoptymalizowany do pracy
przy wolniejszych po³±czeniach sieciowych takich jak po³±czenia
modemowe. Oryginalne VNC mo¿e pracowaæ wolno kiedy po³±czenie nie jest
wystarczaj±co szybkie, natomiast z TightVNC mo¿esz pracowaæ zdalnie
niemal w czasie rzeczywistym.

%package server
Summary:	VNC X server - tightvnc version
Summary(pl):	X serwer VNC - wersja tightvnc
Group:		X11/Applications/Networking
Requires:	XFree86-common
# for vncpasswd tool
Requires:	%{name}-utils = %{version}-%{release}
# for mcookie
Requires:	util-linux
Obsoletes:	vnc-server

%description server
This package contains VNC X server in tightvnc version.

%description server -l pl
Ten pakiet zawiera X serwer VNC w wersji tightvnc.

%package utils
Summary:	Additional utilities for tightvnc
Summary(pl):	Dodatkowe narzêdzia do tightvnc
Group:		X11/Applications/Networking
Obsoletes:	vnc-utils

%description utils
This package contains additional tightvnc utilities: vncconnect and
vncpasswd. vncconnect tells Xvnc server to connect to a listening
tightvnc viewer. vncpasswd generates password file (both on server and
viewer side).

%description utils -l pl
Ten pakiet zawiera dodatkowe narzêdzia do tightvnc: vncconnect i
vncpasswd. vncconnect s³u¿y do po³±czenia serwera Xvnc z nas³uchuj±cym
vncviewerem. vncpasswd s³u¿y to tworzenia pliku z has³em (zarówno po
stronie serwera, jak i przegl±darki).

%prep
%setup -qn vnc_unixsrc
%patch0 -p1
%patch1 -p1
%patch2 -p2
%patch3 -p1

%build
xmkmf
%{__make} World \
	CC="%{__cc}" \
	CDEBUGFLAGS="%{rpmcflags}" \
	EXTRA_LDOPTIONS="%{rpmldflags}"
cd Xvnc
./configure
%{__make} \
	CC="%{__cc}" \
	CDEBUGFLAGS="%{rpmcflags}" \
	EXTRA_LDOPTIONS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/vnc/classes} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

install vncserver vncviewer/vncviewer vncpasswd/vncpasswd \
	vncconnect/vncconnect Xvnc/programs/Xserver/Xvnc $RPM_BUILD_ROOT%{_bindir}

install classes/* $RPM_BUILD_ROOT%{_datadir}/vnc/classes

install vncserver.man $RPM_BUILD_ROOT%{_mandir}/man1/vncserver.1
install vncviewer/vncviewer.man $RPM_BUILD_ROOT%{_mandir}/man1/vncviewer.1
install vncpasswd/vncpasswd.man $RPM_BUILD_ROOT%{_mandir}/man1/vncpasswd.1
install vncconnect/vncconnect.man $RPM_BUILD_ROOT%{_mandir}/man1/vncconnect.1
install Xvnc/programs/Xserver/Xvnc.man $RPM_BUILD_ROOT%{_mandir}/man1/Xvnc.1

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/vncviewer
%{_mandir}/man1/vncviewer.1*
%{_desktopdir}/tightvnc.desktop
%{_pixmapsdir}/tightvnc.png

%files server
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xvnc
%attr(755,root,root) %{_bindir}/vncserver
%{_datadir}/vnc
%{_mandir}/man1/Xvnc.1*
%{_mandir}/man1/vncserver.1*

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vncconnect
%attr(755,root,root) %{_bindir}/vncpasswd
%{_mandir}/man1/vncconnect.1*
%{_mandir}/man1/vncpasswd.1*
