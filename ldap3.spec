#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ldap3
Version  : 2.7
Release  : 10
URL      : https://files.pythonhosted.org/packages/c2/49/3bf179229a92ae87ff2dca1609c2ad599c497938f90fd5d66d02aa8e977e/ldap3-2.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/c2/49/3bf179229a92ae87ff2dca1609c2ad599c497938f90fd5d66d02aa8e977e/ldap3-2.7.tar.gz
Summary  : A strictly RFC 4510 conforming LDAP V3 pure Python client library
Group    : Development/Tools
License  : GPL-3.0 LGPL-3.0
Requires: ldap3-license = %{version}-%{release}
Requires: ldap3-python = %{version}-%{release}
Requires: ldap3-python3 = %{version}-%{release}
Requires: pyasn1
BuildRequires : buildreq-distutils3
BuildRequires : pyasn1

%description
LDAP3
=====

.. image:: https://img.shields.io/pypi/v/ldap3.svg
    :target: https://pypi.python.org/pypi/ldap3/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/l/ldap3.svg
    :target: https://pypi.python.org/pypi/ldap3/
    :alt: License

.. image:: https://img.shields.io/travis/cannatag/ldap3/master.svg
    :target: https://travis-ci.org/cannatag/ldap3
    :alt: TRAVIS-CI build status for master branch


ldap3 is a strictly RFC 4510 conforming **LDAP V3 pure Python client** library. The same codebase runs in Python 2, Python 3, PyPy and PyPy3.


Version 2 warning
-----------------

In version 2 of ldap3 some default values have been changed and the ldap3 namespace has been decluttered, removing redundant
constants (look at the changelog for details). Also, the result code constants were moved to ldap3.core.results and the ldap3 custom exceptions
were stored in ldap3.core.exceptions. If you experience errors in your existing code you should rearrange the import statements or explicitly
set the defaults to their former values.


A more pythonic LDAP
--------------------

LDAP operations look clumsy and hard-to-use because they reflect the old-age idea that time-consuming operations should be performed client-side
to not hog the server with heavy elaborations. To alleviate this ldap3 includes a fully functional **Abstraction Layer** that lets you
interact with the LDAP server in a modern and *pythonic* way. With the Abstraction Layer you don't need to directly issue any LDAP operation at all.


Home Page
---------

Project home page is https://github.com/cannatag/ldap3


Documentation
-------------

Documentation is available at http://ldap3.readthedocs.io


License
-------

The ldap3 project is open source software released under the **LGPL v3 license**.
Copyright 2013 - 2018 Giovanni Cannata


PEP8 Compliance
---------------

ldap3 is PEP8 compliant, except for line length.


Download
--------

Package download is available at https://pypi.python.org/pypi/ldap3.


Install
-------

Install with **pip install ldap3**


Git repository
--------------

You can download the latest source at https://github.com/cannatag/ldap3


Continuous integration
----------------------

Continuous integration for testing is at https://travis-ci.org/cannatag/ldap3


Support
-------

You can submit support tickets on https://github.com/cannatag/ldap3/issues/new
You can submit pull request on the **dev** branch at https://github.com/cannatag/ldap3/tree/dev


Thanks to
---------

* **Ilya Etingof**, the author of the *pyasn1* package for his excellent work and support.

* **Mark Lutz** for his *Learning Python* and *Programming Python* excellent books series and **John Goerzen** and **Brandon Rhodes** for their book *Foundations of Python Network Programming*. These books are wonderful tools for learning Python and this project owes a lot to them.

* **JetBrains** for donating to this project the Open Source license of *PyCharm Professional*.

* **GitHub** for providing the *free source repository space and the tools* I use to develop this project.

* The **FreeIPA** team for letting me use their demo LDAP server in the ldap3 tutorial.


Contact me
----------

For information and suggestions you can contact me at cannatag@gmail.com. You can also open a support ticket on https://github.com/cannatag/ldap3/issues/new


Donate
------

If you want to keep this project up and running you can send me an Amazon gift card. I will use it to improve my skills in the Information and Communication technology.


Changelog
---------

Updated changelog at https://ldap3.readthedocs.io/changelog.html

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
Provides: pypi(ldap3)

%description python3
python3 components for the ldap3 package.


%prep
%setup -q -n ldap3-2.7
cd %{_builddir}/ldap3-2.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583161388
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ldap3
cp %{_builddir}/ldap3-2.7/COPYING.LESSER.txt %{buildroot}/usr/share/package-licenses/ldap3/93a34ec120cdc2f9216d2217ffb32908fd9e3d4b
cp %{_builddir}/ldap3-2.7/COPYING.txt %{buildroot}/usr/share/package-licenses/ldap3/52be821be7d06dde87d7805331066d1af6f3f9f8
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ldap3/52be821be7d06dde87d7805331066d1af6f3f9f8
/usr/share/package-licenses/ldap3/93a34ec120cdc2f9216d2217ffb32908fd9e3d4b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
