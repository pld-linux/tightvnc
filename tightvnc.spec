Summary:	tightvnc - application based on the VNC version 3.3.3r2
Summary(pl):	tightvnc - aplikacja bazuj±ca na VNC w wersji 3.3.3r2
Name:		tightvnc
Version:	1.2.9
Release:	1
License:	GPL
Vendor:		Const Kaplinsky <const_k@users.sourceforge.net>
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/vnc-tight/%{name}-%{version}_unixsrc.tar.bz2
# Source0-md5:	f804b26c098625e3a2675a0aa7709e31
Patch0:		%{name}-vncserver.patch
Source1:	%{name}.desktop
URL:		http://www.tightvnc.com/
BuildRequires:	libjpeg-devel
BuildRequires:	zlib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	vnc

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
VNC is a great client/server software package allowing remote network
access to graphical desktops. TightVNC is optimized to work over slow
network connections such as low-speed modem links. While oroginal VNC
may be verry slow when your connection is not fast enough, with
TightVNC you can work remotely almost in real time in most
environments.

%description -l pl
VNC jest wspania³ym programem client/server umo¿liwiaj±cym zdalny
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
Requires:	xfs
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

%build
xmkmf
%{__make} World \
	CC="%{__cc}" \
	CDEBUGFLAGS="%{rpmcflags}"
cd Xvnc
./configure
%{__make} \
	CC="%{__cc}" \
	CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/vnc/classes} \
	$RPM_BUILD_ROOT%{_applnkdir}/Network

install vncserver vncviewer/vncviewer vncpasswd/vncpasswd \
	vncconnect/vncconnect Xvnc/programs/Xserver/Xvnc $RPM_BUILD_ROOT%{_bindir}

install classes/* $RPM_BUILD_ROOT%{_datadir}/vnc/classes

install vncserver.man $RPM_BUILD_ROOT%{_mandir}/man1/vncserver.1
install vncviewer/vncviewer.man $RPM_BUILD_ROOT%{_mandir}/man1/vncviewer.1
install vncpasswd/vncpasswd.man $RPM_BUILD_ROOT%{_mandir}/man1/vncpasswd.1
install vncconnect/vncconnect.man $RPM_BUILD_ROOT%{_mandir}/man1/vncconnect.1
install Xvnc/programs/Xserver/Xvnc.man $RPM_BUILD_ROOT%{_mandir}/man1/Xvnc.1

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/vncviewer
%{_mandir}/man1/vncviewer.1*
%{_applnkdir}/Network/tightvnc.desktop

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
