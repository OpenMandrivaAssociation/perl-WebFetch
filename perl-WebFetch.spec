%define upstream_name    WebFetch
%define upstream_version 0.12

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Perl module to download and save information from the Web
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://cpan.perl.org/modules/by-module/WebFetch/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
Buildrequires:perl-devel
%endif
Buildrequires:	perl(Date::Calc)
Buildrequires:  perl(HTML::Parser)
Buildrequires:  perl-libwww-perl 
Buildrequires:  perl(XML::Parser)

Buildarch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

Requires:	perl-Locale-Codes 
Requires:   perl-Date-Calc 
Requires:   perl-XML-Parser 

%description
WebFetch is a Perl module to download and save information from the Web, and
to display on the Web.  It will download from sites such as CNet, CNN,
Freshmeat, Slashdot, LinuxToday, Yahoo, and more.  It can even export your
site's news for other sites to include in their web pages.

%prep 
rm -rf $RPM_BUILD_ROOT
%setup -n %{upstream_name}-%{upstream_version}

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
%{perl_vendorlib}/*.pod
%_mandir/*/*
