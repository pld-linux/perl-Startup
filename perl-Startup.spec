%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary: 	Perl Startup module
Summary(pl):	Modu³ Perla Startup
Name: 		perl-Startup
Version: 	0.103
Release: 	1
Copyright: 	GPL
Group: 		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source: 	ftp://ftp.perl.org/pub/CPAN/modules/by-authors/Martin_Schwartz/Startup-%{version}.tar.gz
URL:		http://www.perl.com/CPAN/modules/by-authors/Martin_Schwartz/Startup-%{version}.readme
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Startup privides some nifty options to make your programs more valuable.
See Startup(3pm) for details.

%description -l pl
Startup udostêpnia kilka ciekawych opcji, dziêki którym Twoje programy bêd±
lepsze. Wiêcej informacji znajdziesz w Startup(3pm).

%prep
%setup -q -n Startup-%{version}

%build
perl Makefile.PL

%install
rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{perl_sitearch}
make install \
	DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Startup
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[13]/* \
	README Changes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,Changes}.gz
%attr(755,root,root) %{_bindir}/replace

%{perl_sitelib}/Startup.pm
%{perl_sitearch}/auto/Startup

%{_mandir}/man[13]/*
