Summary:	Userspace RDMA Connection Manager
Name:		librdmacm
Version:	1.0.8
Release:	1
License:	BSD or GPLv2
Group:		Libraries
Source0:	http://www.openfabrics.org/downloads/rdmacm/%{name}-%{version}.tar.gz
# Source0-md5:	5f13879a3c066aaea589a19388727bb8
URL:		http://www.openfabrics.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	libibverbs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
librdmacm provides a userspace RDMA Communication Managment API.

%package devel
Summary:	Header files and develpment documentation for librdmacm
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files and documentation for librdmacm.

%package static
Summary:	Static librdmacm library
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
This package contains the static librdmacm library.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/librdmacm.so.*.*
%attr(755,root,root) %ghost %{_libdir}/librdmacm.so.1
%{_mandir}/man1/*.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librdmacm.so
%{_libdir}/librdmacm.la
%{_includedir}/rdma
%{_mandir}/man3/*.3*
%{_mandir}/man7/*.7*

%files static
%defattr(644,root,root,755)
%{_libdir}/librdmacm.a
