%define		pkgname		simplepie
%define		php_min_version 5.0.0
Summary:	atomlib.php - Atom Syndication Format PHP Library
Name:		php-atomlib
Version:	0.4
Release:	3
License:	Apache v2.0
Group:		Development/Languages/PHP
# svn --ignore-externals co http://phpatomlib.googlecode.com/svn/trunk/ phpatomlib
# tar --exclude-vcs -cjf phpatomlib-$(svnversion phpatomlib).tar.bz2 phpatomlib --exclude=feedvalidator-results
# ../dropin phpatomlib-$(svnversion phpatomlib).tar.bz2 &
Source0:	phpatomlib-7.tar.bz2
# Source0-md5:	5bd976c57a0a8b7a2a3a6c6f6e03ca7b
Patch0:		istext.patch
URL:		http://code.google.com/p/phpatomlib/
BuildRequires:	rpm-build >= 4.4.9-96
BuildRequires:	rpm-php-pearprov
BuildRequires:	rpmbuild(macros) >= 1.461
Requires:	php(core) >= %{php_min_version}
Requires:	php(xml)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional php dependencies
%define		_noautophp	%{nil}

# put it together for rpmbuild
%define		_noautoreq	%{?_noautophp} %{?_noautopear}

%description
This project was created in order to provide a more complete PHP
library to efficiently parse Atom Feeds.

%prep
%setup -q -n phpatomlib
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -a lib/atomlib.php $RPM_BUILD_ROOT%{php_data_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_data_dir}/atomlib.php
