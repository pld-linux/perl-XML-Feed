#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	Feed
Summary:	XML::Feed - Syndication feed parser and auto-discovery
#Summary(pl.UTF-8):	
Name:		perl-XML-Feed
Version:	0.12
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/XML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	77565d61b511f7ae05623064e04e9f56
URL:		http://search.cpan.org/dist/XML-Feed/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-ErrorHandler
BuildRequires:	perl-DateTime
BuildRequires:	perl-DateTime-Format-Mail
BuildRequires:	perl-DateTime-Format-W3CDTF
BuildRequires:	perl-Feed-Find
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-URI-Fetch
BuildRequires:	perl-XML-Atom >= 0.08
BuildRequires:	perl-XML-RSS >= 1.01
BuildRequires:	perl-libwww
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::Feed is a syndication feed parser for both RSS and Atom feeds. It
also implements feed auto-discovery for finding feeds, given a URI.

The goal of XML::Feed is to provide a unified API for parsing and
using the various syndication formats. The different flavors of RSS
and Atom handle data in different ways: date handling; summaries and
content; escaping and quoting; etc. This module attempts to remove
those differences by providing a wrapper around the formats and the
classes implementing those formats (XML::RSS and XML::Atom::Feed). For
example, dates are handled differently in each of the above formats. To
provide a unified API for date handling, XML::Feed converts all date
formats transparently into DateTime objects, which it then returns
to the caller.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/XML/*.pm
%{perl_vendorlib}/XML/Feed
%{_mandir}/man3/*
