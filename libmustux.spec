#
# Conditional build:
# _without_alsa	- without ALSA support
#
Summary:	Professional Audio Tools for GNU/Linux - a library
Summary(pl):	Profesjonalne Narzêdzia Audio dla GNU/Linuksa - biblioteka
Name:		libmustux
Version:	0.20.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://savannah.nongnu.org/download/protux/%{name}-%{version}.tar.gz
# Source0-md5:	dab777e2f64928c97b125865c031f719
Patch0:		%{name}-acam.patch
URL:		http://www.nongnu.org/protux/mustux.html
%{!?_without_alsa:BuildRequires:	alsa-lib-devel}
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	perl-base
BuildRequires:	qt-devel
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

%description -l pl
Mustux to projekt paradygmatu narzêdzi muzycznych. Jest to inicjatywa
stworzenia zestawu narzêdzi dla muzyków opartego na ujednoliconej
koncepcji; narzêdzia mog± oferowaæ innowacyjny interfejs poprzez
u¿ycie akcji klawiatury i myszy bez ¿adnego klikniêcia mysz±. Nale¿y
zauwa¿yæ, ¿e nie chodzi o "skróty". Skróty to akcje klawiatury
wywo³uj±ce procedury obs³ugi przycisków/ikon/widgetów. Akcje JMB
próbuj± symulowaæ urz±dzenia analogowe, takie jak pier¶cienie
jog/shuttle, slidery i inne do szybkiego manipulowania wej¶ciami.
Protux i Mustache to przyk³adowe narzêdzia bêd±ce czê¶ci± tego
projektu.

%package devel
Summary:	Header files for libmustux library
Summary(pl):	Pliki nag³ówkowe biblioteki libmustux
Group:		Development/Libraries
Requires:	%{name} = %{version}
%{!?_without_alsa:Requires:	alsa-lib-devel}
Requires:	qt-devel

%description devel
Header files for libmustux library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libmustux.

%package static
Summary:	Static libmustux library
Summary(pl):	Statyczna biblioteka libmustux
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libmustux library.

%description static -l pl
Statyczna biblioteka libmustux.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static \
	%{?_without_alsa:--disable-alsa}

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
