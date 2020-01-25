Summary:	.NET bindings for libextractor
Summary(pl.UTF-8):	Wiązania .NET do biblioteki libextractor
Name:		dotnet-libextractor
Version:	0.5.23
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	http://ftp.gnu.org/gnu/libextractor/libextractor-mono-%{version}.tar.gz
# Source0-md5:	5353c113cd9ad9e8996dcca549ab5d4b
URL:		http://www.gnu.org/software/libextractor/
BuildRequires:	mono-csharp
BuildRequires:	rpmbuild(monoautodeps)
BuildRequires:	sed >= 4.0
Requires:	libextractor >= 1.0
Requires:	mono
ExclusiveArch:	%{ix86} %{x8664} arm hppa ia64 ppc s390 s390x sparc sparcv9 sparc64
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides bindings for .NET to GStreamer libraries.

%description -l pl.UTF-8
Pakiet ten dostarcza wiązania dla .NET do bibliotek GStreamera.

%package devel
Summary:	Development files for LibExtractor .NET library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki .NET LibExtractor
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for LibExtractor .NET library.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki .NET LibExtractor.

%prep
%setup -q -n LibExtractor

%{__sed} -i -e 's/libextractor\.so\.1\.1\.1/libextractor.so.3/' LibExtractor/LibExtractor.dll.config

%build
# not autoconf configure
./configure \
	--prefix=%{_prefix}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# avoid conflict with libextractor.pc from C library
%{__mv} $RPM_BUILD_ROOT%{_prefix}/lib/pkgconfig/{libextractor,LibExtractor}.pc

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS
%dir %{_prefix}/lib/libextractor
%{_prefix}/lib/libextractor/LibExtractor.dll
%{_prefix}/lib/libextractor/LibExtractor.dll.config

%files devel
%defattr(644,root,root,755)
%{_prefix}/lib/pkgconfig/LibExtractor.pc
