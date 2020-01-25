Summary:	Perl Startup module
Summary(pl.UTF-8):	Moduł Perla Startup
Name:		perl-Startup
Version:	0.103
Release:	12
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/MS/MSCHWARTZ/Startup-%{version}.tar.gz
# Source0-md5:	8f39b68ee2d5b81caa77d295d6ecacf0
Patch0:		Startup-replace.patch
URL:		http://search.cpan.org/dist/Startup/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Startup privides some nifty options to make your programs more
valuable. See Startup(3pm) for details.

%description -l pl.UTF-8
Startup udostępnia kilka ciekawych opcji, dzięki którym Twoje programy
będą lepsze. Więcej informacji znajdziesz w Startup(3pm).

%prep
%setup -q -n Startup-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%attr(755,root,root) %{_bindir}/replace.pl
%{perl_vendorlib}/Startup.pm
%{_mandir}/man[13]/*
