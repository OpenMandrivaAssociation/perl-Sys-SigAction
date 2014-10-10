%define upstream_name	 Sys-SigAction
%define upstream_version 0.21

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Perl extension for Consistent Signal Handling
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Sys/Sys-SigAction-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module implements set_sig_handler(), which sets up a signal handler and
(optionally) returns an object which causes the signal handler to be reset to
the previous value, when it goes out of scope.

Also implemented is timeout_call() which takes a timeout value and a code
reference, and executes the code reference wrapped with an alarm timeout.

Finally, two convenience routines are defined which allow one to get the signal
name from the number -- sig_name(), and get the signal number from the name --
sig_number().

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Sys
%{_mandir}/man3*/*


%changelog
* Tue Jul 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.150.0-1mdv2011.0
+ Revision: 688828
- update to new version 0.15

* Sun Jun 26 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.140.0-1
+ Revision: 687343
- update to new version 0.14

* Fri Jun 24 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.130.0-1
+ Revision: 687000
- update to new version 0.13

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-1mdv2010.0
+ Revision: 404434
- rebuild using %%perl_convert_version

* Sun Feb 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-1mdv2009.1
+ Revision: 336237
- update to new version 0.11

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.10-4mdv2009.0
+ Revision: 258426
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.10-3mdv2009.0
+ Revision: 246493
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.10-1mdv2008.1
+ Revision: 140717
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Jul 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdv2008.0
+ Revision: 48946
- import perl-Sys-SigAction


* Fri Jul 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdv2008.0
- first mdv release 



