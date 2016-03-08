#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cpio
Version  : 2.12
Release  : 18
URL      : http://mirrors.kernel.org/gnu/cpio/cpio-2.12.tar.bz2
Source0  : http://mirrors.kernel.org/gnu/cpio/cpio-2.12.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-3.0 GPL-3.0+
Requires: cpio-bin
Requires: cpio-doc
Requires: cpio-locales
BuildRequires : bison
Patch1: cve-2016-2037.patch

%description
This is the GNU cpio package
============================
* Introduction
==============

%package bin
Summary: bin components for the cpio package.
Group: Binaries

%description bin
bin components for the cpio package.


%package doc
Summary: doc components for the cpio package.
Group: Documentation

%description doc
doc components for the cpio package.


%package locales
Summary: locales components for the cpio package.
Group: Default

%description locales
locales components for the cpio package.


%prep
%setup -q -n cpio-2.12
%patch1 -p1

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install
%find_lang cpio

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/libexec/rmt
/usr/bin/cpio

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man8/*

%files locales -f cpio.lang 
%defattr(-,root,root,-)

