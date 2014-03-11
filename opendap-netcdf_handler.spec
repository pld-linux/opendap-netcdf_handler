#
# Conditional build:
%bcond_with	tests	# make check (requires BES server)
#
Summary:	NetCDF 3 data handler module for the OPeNDAP data server
Summary(pl.UTF-8):	Moduł obsługujący dane NetCDF 3 dla serwera danych OPeNDAP
Name:		opendap-netcdf_handler
Version:	3.10.3
Release:	1
License:	LGPL v2.1+
Group:		Daemons
Source0:	http://www.opendap.org/pub/source/netcdf_handler-%{version}.tar.gz
# Source0-md5:	a4453fbf1f2a73ede4aa399cd02021c3
URL:		http://opendap.org/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake >= 1:1.10
%{?with_tests:BuildRequires:	bes >= 3.9.0}
BuildRequires:	bes-devel >= 3.9.0
BuildRequires:	libdap-devel >= 3.11.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	netcdf-devel >= 3.6
BuildRequires:	pkgconfig
Requires:	bes >= 3.9.0
Requires:	libdap >= 3.11.0
Requires:	netcdf >= 3.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the NetCDF data handler module for the OPeNDAP data server. It
reads NetCDF 3 files and returns DAP responses that are compatible
with DAP2 and the dap-server software.

%description -l pl.UTF-8
Ten pakiet zawiera moduł obsługujący dane NetCDF dla serwera danych
OPeNDAP. Odczytuje pliki NetCDF 3 i zwraca odpowiedzi DAP zgodne z
oprogramowaniem DAP2 i dap-server.

%prep
%setup -q -n netcdf_handler-%{version}

%build
# rebuild autotools for -as-needed to work
%{__libtoolize}
%{__aclocal} -I conf
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/bes/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT ChangeLog NEWS README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/nc.conf
%attr(755,root,root) %{_libdir}/bes/libnc_module.so
%dir %{_datadir}/hyrax/data/nc
%{_datadir}/hyrax/data/nc/*.das
%{_datadir}/hyrax/data/nc/*.nc
%doc %{_datadir}/hyrax/data/nc/*.nc.html
