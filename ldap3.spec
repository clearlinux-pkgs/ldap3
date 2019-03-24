#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ldap3
Version  : 2.6
Release  : 4
URL      : https://files.pythonhosted.org/packages/79/66/d297c6f3c30b69c813c06e8933769c2732c83d35ca584107346d81ab2eee/ldap3-2.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/79/66/d297c6f3c30b69c813c06e8933769c2732c83d35ca584107346d81ab2eee/ldap3-2.6.tar.gz
Summary  : A strictly RFC 4510 conforming LDAP V3 pure Python client library
Group    : Development/Tools
License  : GPL-3.0 LGPL-3.0
Requires: ldap3-license = %{version}-%{release}
Requires: ldap3-python = %{version}-%{release}
Requires: ldap3-python3 = %{version}-%{release}
Requires: pyasn1
BuildRequires : buildreq-distutils3

%description
LDAP3
=====
.. image:: https://img.shields.io/pypi/v/ldap3.svg
:target: https://pypi.python.org/pypi/ldap3/
:alt: Latest Version

%package license
Summary: license components for the ldap3 package.
Group: Default

%description license
license components for the ldap3 package.


%package python
Summary: python components for the ldap3 package.
Group: Default
Requires: ldap3-python3 = %{version}-%{release}

%description python
python components for the ldap3 package.


%package python3
Summary: python3 components for the ldap3 package.
Group: Default
Requires: python3-core

%description python3
python3 components for the ldap3 package.


%prep
%setup -q -n ldap3-2.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1553438902
export LDFLAGS="${LDFLAGS} -fno-lto"
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ldap3
cp COPYING.LESSER.txt %{buildroot}/usr/share/package-licenses/ldap3/COPYING.LESSER.txt
cp COPYING.txt %{buildroot}/usr/share/package-licenses/ldap3/COPYING.txt
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ldap3/COPYING.LESSER.txt
/usr/share/package-licenses/ldap3/COPYING.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
