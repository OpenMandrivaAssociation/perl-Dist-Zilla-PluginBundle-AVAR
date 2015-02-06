%define upstream_name    Dist-Zilla-PluginBundle-AVAR
%define upstream_version 0.16

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Use L<Dist::Zilla> like AVAR does
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Dist::Zilla)
BuildRequires:	perl(Dist::Zilla::Plugin::AutoPrereq)
BuildRequires:	perl(Dist::Zilla::Plugin::CompileTests)
BuildRequires:	perl(Dist::Zilla::Plugin::MakeMaker::Awesome)
BuildRequires:	perl(Dist::Zilla::Plugin::MetaNoIndex)
BuildRequires:	perl(Dist::Zilla::Plugin::ReadmeFromPod)
BuildRequires:	perl(Dist::Zilla::Plugin::VersionFromPrev)
BuildRequires:	perl(Dist::Zilla::PluginBundle::Filter)
BuildRequires:	perl(Dist::Zilla::PluginBundle::Git)
BuildRequires:	perl(Dist::Zilla::Role::PluginBundle)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Autobox)

BuildArch:	noarch

%description
This is the plugin bundle that AVAR uses.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE README META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*

