Summary:	tightvnc - application based on the VNC version 3.3.3r2
Summary(pl):	tightvnc - aplikacja bazuj�ca na VNC w wersji 3.3.3r2
Name:		tightvnc
Version:	1.2.4
Release:	1
License:	GPL
Vendor:		Const Kaplinsky <const_k@users.sourceforge.net>
Group:		X11/Applications/Networking
Source0:	http://belnet.dl.sourceforge.net/sourceforge/vnc-tight/%{name}-%{version}_unixsrc.tar.gz
Source1:	%{name}.desktop
URL:		http://www.tightvnc.com
BuildRequires:	libjpeg-devel
BuildRequires:	zlib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
VNC jest wspania�ym programem client/server umo�liwiaj�cym zdalny
dost�p do graficznych pulpit�w. TightVNC jest zoptymalizowany do pracy
przy wolniejszych po��czeniach sieciowych takich jak po��czenia
modemowe. Oryginalne VNC mo�e pracowa� wolno kiedy po��czenie nie jest
wystarczaj�co szybkie, natomiast z TightVNC mo�esz pracowa� zdalnie
niemal w czasie rzeczywistym.

%prep
%setup -qn vnc_unixsrc

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
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_applnkdir}/Network}

install vncserver vncviewer/vncviewer vncpasswd/vncpasswd \
	vncconnect/vncconnect $RPM_BUILD_ROOT%{_bindir}

install vncserver.man $RPM_BUILD_ROOT%{_mandir}/man1/vncserver.1
install vncviewer/vncviewer.man $RPM_BUILD_ROOT%{_mandir}/man1/vncviewer.1
install vncpasswd/vncpasswd.man $RPM_BUILD_ROOT%{_mandir}/man1/vncpasswd.1
install vncconnect/vncconnect.man $RPM_BUILD_ROOT%{_mandir}/man1/vncconnect.1

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_applnkdir}/Network/tightvnc.desktop
