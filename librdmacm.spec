Summary:	Userspace RDMA Connection Manager
Summary(pl.UTF-8):	Zarządca połączeń RDMA w przestrzeni użytkowika
Name:		librdmacm
Version:	1.0.13
Release:	1
License:	BSD or GPL v2
Group:		Libraries
Source0:	http://www.openfabrics.org/downloads/rdmacm/%{name}-%{version}.tar.gz
# Source0-md5:	2281aa8bf47caf34819842f79e3f9759
URL:		http://www.openfabrics.org/
BuildRequires:	libibverbs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_bindir}/mckey
%attr(755,root,root) %{_bindir}/rdma_client
%attr(755,root,root) %{_bindir}/rdma_server
%attr(755,root,root) %{_bindir}/rping
%attr(755,root,root) %{_bindir}/ucmatose
%attr(755,root,root) %{_bindir}/udaddy
%attr(755,root,root) %{_libdir}/librdmacm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librdmacm.so.1
%{_mandir}/man1/mckey.1*
%{_mandir}/man1/rdma_client.1*
%{_mandir}/man1/rdma_server.1*
%{_mandir}/man1/rping.1*
%{_mandir}/man1/ucmatose.1*
%{_mandir}/man1/udaddy.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librdmacm.so
%{_libdir}/librdmacm.la
%{_includedir}/infiniband/ib.h
%{_includedir}/rdma
%{_mandir}/man3/rdma_*.3*
%{_mandir}/man7/rdma_cm.7*

%files static
%defattr(644,root,root,755)
%{_libdir}/librdmacm.a
