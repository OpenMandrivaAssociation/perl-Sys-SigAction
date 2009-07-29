%define upstream_name	 Sys-SigAction
%define upstream_version 0.11

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Perl extension for Consistent Signal Handling
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Sys/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildArch:	noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Sys
%_mandir/man3*/*
