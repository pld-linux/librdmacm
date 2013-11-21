Summary:	Userspace RDMA Connection Manager
Summary(pl.UTF-8):	Zarządca połączeń RDMA w przestrzeni użytkowika
Name:		librdmacm
Version:	1.0.17.1
Release:	1
License:	BSD or GPL v2
Group:		Libraries
Source0:	http://www.openfabrics.org/downloads/rdmacm/%{name}-%{version}.tar.gz
# Source0-md5:	c41b18794b1b58065fed464a743e23b0
Source1:	%{name}.pc.in
Patch0:		%{name}-link.patch
URL:		http://www.openfabrics.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libibverbs-devel
BuildRequires:	libtool >= 1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

%description
librdmacm provides a userspace RDMA Communication Management API.

%description -l pl.UTF-8
librdmacm udostępnia API RDMA Communication Management (zarządzające
połączeniami RDMA) w przestrzeni użytkownika.

%package devel
Summary:	Header files for librdmacm library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki librdmacm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libibverbs-devel

%description devel
Header files for librdmacm library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki librdmacm.

%package static
Summary:	Static librdmacm library
Summary(pl.UTF-8):	Statyczna biblioteka librdmacm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains the static librdmacm library.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczną bibliotekę librdmacm.

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
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# check if not present already
[ ! -f $RPM_BUILD_ROOT%{_pkgconfigdir}/rdmacm.pc ] || exit 1
install -d $RPM_BUILD_ROOT%{_pkgconfigdir}
sed -e 's,@prefix@,%{_prefix},;
	s,@libdir@,%{_libdir},;
	s,@LIBVERSION@,%{version},' %{SOURCE1} >$RPM_BUILD_ROOT%{_pkgconfigdir}/rdmacm.pc

# preloadable library
%{__rm} $RPM_BUILD_ROOT%{_libdir}/rsocket/librspreload.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_bindir}/mckey
%attr(755,root,root) %{_bindir}/rcopy
%attr(755,root,root) %{_bindir}/rdma_client
%attr(755,root,root) %{_bindir}/rdma_server
%attr(755,root,root) %{_bindir}/rdma_xclient
%attr(755,root,root) %{_bindir}/rdma_xserver
%attr(755,root,root) %{_bindir}/riostream
%attr(755,root,root) %{_bindir}/rping
%attr(755,root,root) %{_bindir}/rstream
%attr(755,root,root) %{_bindir}/ucmatose
%attr(755,root,root) %{_bindir}/udaddy
%attr(755,root,root) %{_bindir}/udpong
%attr(755,root,root) %{_libdir}/librdmacm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librdmacm.so.1
%dir %{_libdir}/rsocket
%attr(755,root,root) %{_libdir}/rsocket/librspreload.so*
%{_mandir}/man1/mckey.1*
%{_mandir}/man1/rcopy.1*
%{_mandir}/man1/rdma_client.1*
%{_mandir}/man1/rdma_server.1*
%{_mandir}/man1/rdma_xclient.1*
%{_mandir}/man1/rdma_xserver.1*
%{_mandir}/man1/rping.1*
%{_mandir}/man1/rstream.1*
%{_mandir}/man1/ucmatose.1*
%{_mandir}/man1/udaddy.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librdmacm.so
%{_libdir}/librdmacm.la
%{_includedir}/infiniband/ib.h
%{_includedir}/rdma
%{_pkgconfigdir}/rdmacm.pc
%{_mandir}/man3/rdma_*.3*
%{_mandir}/man7/rdma_cm.7*
%{_mandir}/man7/rsocket.7*

%files static
%defattr(644,root,root,755)
%{_libdir}/librdmacm.a
