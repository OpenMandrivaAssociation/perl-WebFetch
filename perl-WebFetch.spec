%define name perl-WebFetch
%define module WebFetch
%define version 0.10
%define release %mkrel 11

Name:		%{name}
Summary:	Perl module to download and save information from the Web
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		%{module}-%{version}.tar.bz2
Buildrequires:	perl(Date::Calc)
Buildrequires:  perl(HTML::Parser)
Buildrequires:  perl-libwww-perl 
Buildrequires:  perl(XML::Parser)
%if %{mdkversion} < 1010
Buildrequires:perl-devel
%endif
Requires:	perl-Locale-Codes 
Requires:       perl-Date-Calc 
Requires:       perl-XML-Parser 
Buildarch:	noarch

%description
WebFetch is a Perl module to download and save information from the Web, and
to display on the Web.  It will download from sites such as CNet, CNN,
Freshmeat, Slashdot, LinuxToday, Yahoo, and more.  It can even export your
site's news for other sites to include in their web pages.

%prep 
rm -rf $RPM_BUILD_ROOT

%setup -n %{module}-%{version}

%build

CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
make
make test


%install

rm -rf $RPM_BUILD_ROOT
make PREFIX=$RPM_BUILD_ROOT%{_prefix} DESTDIR=$RPM_BUILD_ROOT install


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes MANIFEST TODO README
%{perl_vendorlib}/WebFetch*
%{perl_vendorlib}/auto/WebFetch
%{perl_vendorlib}/*.pod
%_mandir/*/*



