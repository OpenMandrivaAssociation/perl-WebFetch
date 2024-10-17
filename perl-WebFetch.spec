%define upstream_name    WebFetch
%define upstream_version 0.12

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Perl module to download and save information from the Web
License:	GPL
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://cpan.perl.org/modules/by-module/WebFetch/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Date::Calc)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl-libwww-perl
BuildRequires:  perl(XML::Parser)
# Just to make sure it exists
BuildRequires:	perl(Locale::Codes)

BuildArch:	noarch

Requires:	perl(Locale::Codes)
Requires:	perl(Date::Calc)
Requires:	perl(XML::Parser)

%description
WebFetch is a Perl module to download and save information from the Web, and
to display on the Web.  It will download from sites such as CNet, CNN,
Freshmeat, Slashdot, LinuxToday, Yahoo, and more.  It can even export your
site's news for other sites to include in their web pages.

%prep 
%setup -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test


%install
%makeinstall_std

%files
%doc Changes MANIFEST TODO README
%{perl_vendorlib}/WebFetch*
%{perl_vendorlib}/*.pod
%{_mandir}/*/*


%changelog
* Mon Aug 31 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.120.0-1mdv2010.0
+ Revision: 422889
- update to 0.12

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.10-14mdv2009.0
+ Revision: 258785
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.10-13mdv2009.0
+ Revision: 246701
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.10-11mdv2008.1
+ Revision: 136364
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Oct 28 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 0.10-11mdv2007.0
+ Revision: 73532
- Fix Build
- import perl-WebFetch-0.10-10mdk

* Fri Sep 30 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.10-10mdk
- Fix url

* Fri Sep 30 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.10-9mdk
- remove -q

* Wed Jun 30 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.10-8mdk
- rebuild

