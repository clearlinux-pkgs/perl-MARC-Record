#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-MARC-Record
Version  : 2.0.7
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/G/GM/GMCHARLT/MARC-Record-2.0.7.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/G/GM/GMCHARLT/MARC-Record-2.0.7.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libm/libmarc-record-perl/libmarc-record-perl_2.0.7-1.debian.tar.xz
Summary  : 'Perl extension for handling MARC records'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-MARC-Record-bin = %{version}-%{release}
Requires: perl-MARC-Record-license = %{version}-%{release}
Requires: perl-MARC-Record-man = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
MARC::Record and its family
===========================
SYNOPSIS
The MARC::* series of modules create a simple object-oriented
abstraction of MARC record handling.  The files are:

%package bin
Summary: bin components for the perl-MARC-Record package.
Group: Binaries
Requires: perl-MARC-Record-license = %{version}-%{release}
Requires: perl-MARC-Record-man = %{version}-%{release}

%description bin
bin components for the perl-MARC-Record package.


%package dev
Summary: dev components for the perl-MARC-Record package.
Group: Development
Requires: perl-MARC-Record-bin = %{version}-%{release}
Provides: perl-MARC-Record-devel = %{version}-%{release}

%description dev
dev components for the perl-MARC-Record package.


%package license
Summary: license components for the perl-MARC-Record package.
Group: Default

%description license
license components for the perl-MARC-Record package.


%package man
Summary: man components for the perl-MARC-Record package.
Group: Default

%description man
man components for the perl-MARC-Record package.


%prep
%setup -q -n MARC-Record-2.0.7
cd ..
%setup -q -T -D -n MARC-Record-2.0.7 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/MARC-Record-2.0.7/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-MARC-Record
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-MARC-Record/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/MARC/Batch.pm
/usr/lib/perl5/vendor_perl/5.28.0/MARC/Doc/Tutorial.pod
/usr/lib/perl5/vendor_perl/5.28.0/MARC/Field.pm
/usr/lib/perl5/vendor_perl/5.28.0/MARC/File.pm
/usr/lib/perl5/vendor_perl/5.28.0/MARC/File/Encode.pm
/usr/lib/perl5/vendor_perl/5.28.0/MARC/File/MicroLIF.pm
/usr/lib/perl5/vendor_perl/5.28.0/MARC/File/USMARC.pm
/usr/lib/perl5/vendor_perl/5.28.0/MARC/Record.pm

%files bin
%defattr(-,root,root,-)
/usr/bin/marcdump

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/MARC::Batch.3
/usr/share/man/man3/MARC::Doc::Tutorial.3
/usr/share/man/man3/MARC::Field.3
/usr/share/man/man3/MARC::File.3
/usr/share/man/man3/MARC::File::Encode.3
/usr/share/man/man3/MARC::File::MicroLIF.3
/usr/share/man/man3/MARC::File::USMARC.3
/usr/share/man/man3/MARC::Record.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-MARC-Record/deblicense_copyright

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/marcdump.1