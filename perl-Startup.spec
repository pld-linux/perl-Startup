%include	/usr/lib/rpm/macros.perl
Summary:	Perl Startup module
Summary(pl):	Modu� Perla Startup
Name:		perl-Startup
Version:	0.103
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/authors/id/M/MS/MSCHWARTZ/Startup-%{version}.tar.gz
Patch0:		Startup-replace.patch
URL:		http://www.perl.com/CPAN/modules/by-authors/Martin_Schwartz/Startup-%{version}.readme
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl-devel >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Startup privides some nifty options to make your programs more
valuable. See Startup(3pm) for details.

%description -l pl
Startup udost�pnia kilka ciekawych opcji, dzi�ki kt�rym Twoje programy
b�d� lepsze. Wi�cej informacji znajdziesz w Startup(3pm).

%prep
%setup -q -n Startup-%{version}
%patch -p1

%build
%{__perl} Makefile.PL

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%attr(755,root,root) %{_bindir}/replace.pl
%{perl_sitelib}/Startup.pm
%{_mandir}/man[13]/*
