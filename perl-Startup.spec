%include	/usr/lib/rpm/macros.perl
Summary:	Perl Startup module
Summary(pl):	Modu³ Perla Startup
Name:		perl-Startup
Version:	0.103
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-authors/Martin_Schwartz/Startup-%{version}.tar.gz
Patch0:		Startup-replace.patch
URL:		http://www.perl.com/CPAN/modules/by-authors/Martin_Schwartz/Startup-%{version}.readme
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Startup privides some nifty options to make your programs more
valuable. See Startup(3pm) for details.

%description -l pl
Startup udostêpnia kilka ciekawych opcji, dziêki którym Twoje programy
bêd± lepsze. Wiêcej informacji znajdziesz w Startup(3pm).

%prep
%setup -q -n Startup-%{version}
%patch -p1

%build
perl Makefile.PL

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README Changes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/replace.pl
%{perl_sitelib}/Startup.pm
%{_mandir}/man[13]/*
