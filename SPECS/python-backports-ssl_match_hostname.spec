%global module_name backports.ssl_match_hostname

Name:           python-backports-ssl_match_hostname
Version:        3.5.0.1
Release:        12%{?dist}
Summary:        The ssl.match_hostname() function from Python 3

License:        Python
URL:            https://bitbucket.org/brandon/backports.ssl_match_hostname
Source0:        https://pypi.python.org/packages/source/b/%{module_name}/%{module_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel

%global _description\
The Secure Sockets layer is only actually secure if you check the hostname in\
the certificate returned by the server to which you are connecting, and verify\
that it matches to hostname that you are trying to reach.\
\
But the matching logic, defined in RFC2818, can be a bit tricky to implement on\
your own. So the ssl package in the Standard Library of Python 3.2 now includes\
a match_hostname() function for performing this check instead of requiring\
every application to implement the check separately.\
\
This backport brings match_hostname() to users of earlier versions of Python.\
The actual code is only slightly modified from Python 3.5.\


%description %_description

%package -n python2-backports-ssl_match_hostname
Summary: %summary
Requires: python2-backports
Requires: python2-ipaddress
%{?python_provide:%python_provide python2-backports-ssl_match_hostname}

%description -n python2-backports-ssl_match_hostname %_description

%prep
%setup -qn %{module_name}-%{version}

cp backports/ssl_match_hostname/README.txt ./
cp backports/ssl_match_hostname/LICENSE.txt ./

%build
python2 setup.py build

%install
python2 setup.py install --skip-build --root %{buildroot}
rm -f %{buildroot}%{python2_sitelib}/backports/__init__.py*

%files -n python2-backports-ssl_match_hostname
%{!?_licensedir:%global license %%doc}
%license LICENSE.txt
%doc README.txt
%{python2_sitelib}/backports/ssl_match_hostname/
%{python2_sitelib}/backports.ssl_match_hostname-%{version}-*egg*

%changelog
* Wed Dec 16 2020 Tomas Orsava <torsava@redhat.com> - 3.5.0.1-12
- Remove unversioned Provides
- Resolves: rhbz#1908300

* Thu Apr 25 2019 Tomas Orsava <torsava@redhat.com> - 3.5.0.1-11
- Bumping due to problems with modular RPM upgrade path
- Resolves: rhbz#1695587

* Mon Jul 16 2018 Lumír Balhar <lbalhar@redhat.com> - 3.5.0.1-10
- First version for python27 module
