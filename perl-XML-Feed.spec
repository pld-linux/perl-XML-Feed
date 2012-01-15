#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	Feed
Summary:	XML::Feed - Syndication feed parser and auto-discovery
Summary(pl.UTF-8):	XML::Feed - analizator i automatyczne wykrywanie feedów zespolonych
Name:		perl-XML-Feed
Version:	0.46
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/XML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3089c4a19346165d1e3692c2cd912beb
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
BuildRequires:	perl-Module-Pluggable
BuildRequires:	perl-URI-Fetch
BuildRequires:	perl-XML-Atom >= 0.37
BuildRequires:	perl-XML-LibXML >= 1.66
BuildRequires:	perl-XML-RSS >= 1.47
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

%description -l pl.UTF-8
XML::Feed to analizator feedów zespolonych w formatach RSS i Atom.
Implementuje także automatyczne wykrywanie feedów do ich znajdowania
dla danego URI.

Celem XML::Feed jest udostępnienie jednolitego API do analizy i
wykorzystywania różnych formatów zespolonych. Różne rodzaje RSS i Atom
obsługują dane na różne sposoby: obsługa daty, podsumowania i treść,
cytowanie itp. Ten moduł próbuje usunąć te różnice udostępniając
wrapper na te formaty oraz klasy implementujące te formaty (XML::RSS i
XML::Atom::Feed). Na przykład daty są różnie obsługiwane w każdym z
formatów. Aby udostępnić jednolite API do obsługi dat, XML::Feed
w sposób przezroczysty konwertuje wszystkie formaty dat do obiektów
DateTime, które zwraca wywołującemu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/XML/*.pm
%{perl_vendorlib}/XML/Feed
%{_mandir}/man3/*
