Summary:	Professional Audio Tools for GNU/Linux - a library
Summary(pl.UTF-8):   Profesjonalne Narzędzia Audio dla GNU/Linuksa - biblioteka
Name:		libmustux
Version:	0.20.1
Release:	2
License:	GPL
Group:		Libraries
Source0:	http://savannah.nongnu.org/download/protux/%{name}-%{version}.tar.gz
# Source0-md5:	2b65d686a867232095c4a89b44b3e415
Patch0:		%{name}-acam.patch
URL:		http://www.nongnu.org/protux/mustux.html
BuildRequires:	alsa-lib-devel >= 0.9.0
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool >= 2:1.4d
# checked for, but not used at all
#BuildRequires:	libogg-devel
# test commented out in configure
#BuildRequires:	libvorbis-devel
BuildRequires:	perl-base
BuildRequires:	qt-devel >= 2.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mustux is a Musician Tools Paradigm Project. It is an initiative to
create a suite of tools for musicians based on a unified concept; the
tools might be able to offer an innovative interface by the usage of
keyboard + mouse actions without a single mouse click. Notice that we
are not talking about "shortcuts". Shortcuts are keyboard actions that
call buttons/icons/widgets events handlers. JMB actions try to
simulate an analogic device, such jog/shuttle rings, sliders, and
other fast manipulation input handlers. Protux and Mustache are some
of the tools that are part of this project.

%description -l pl.UTF-8
Mustux to projekt paradygmatu narzędzi muzycznych. Jest to inicjatywa
stworzenia zestawu narzędzi dla muzyków opartego na ujednoliconej
koncepcji; narzędzia mogą oferować innowacyjny interfejs poprzez
użycie akcji klawiatury i myszy bez żadnego kliknięcia myszą. Należy
zauważyć, że nie chodzi o "skróty". Skróty to akcje klawiatury
wywołujące procedury obsługi przycisków/ikon/widgetów. Akcje JMB
próbują symulować urządzenia analogowe, takie jak pierścienie
jog/shuttle, slidery i inne do szybkiego manipulowania wejściami.
Protux i Mustache to przykładowe narzędzia będące częścią tego
projektu.

%package devel
Summary:	Header files for libmustux library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki libmustux
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	alsa-lib-devel >= 0.9.0
Requires:	qt-devel >= 2.3.0

%description devel
Header files for libmustux library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libmustux.

%package static
Summary:	Static libmustux library
Summary(pl.UTF-8):   Statyczna biblioteka libmustux
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libmustux library.

%description static -l pl.UTF-8
Statyczna biblioteka libmustux.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static \
	--with-qt-lib-dir=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mustux-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/mustux.h
%{_includedir}/libmustux
%{_aclocaldir}/*.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
