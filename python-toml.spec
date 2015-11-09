%global pypi_name toml
%global with_test 0

Name:           python-%{pypi_name}
Version:        0.9.1
Release:        4%{?dist}
Summary:        Python Library for Tom's Obvious, Minimal Language

License:        MIT
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://pypi.python.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Tests files are not provided in pypi release as they require toml-test to run
Source1:        https://raw.githubusercontent.com/uiri/toml/da6d593944d08569e08ff32f2bb2e73da91d3578/toml_test.py
Source2:        https://raw.githubusercontent.com/uiri/toml/da6d593944d08569e08ff32f2bb2e73da91d3578/toml_test3.py

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  golang-github-BurntSushi-toml-test

%description
TOML aims to be a minimal configuration file format that's easy to read due to
obvious semantics. TOML is designed to map unambiguously to a hash table. TOML
should be easy to parse into data structures in a wide variety of languages.
This package loads toml file into python dictionary and dump dictionary into
toml file.


%package -n     python2-%{pypi_name}
Summary:        Python Library for Tom's Obvious, Minimal Language
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
TOML aims to be a minimal configuration file format that's easy to read due to
obvious semantics. TOML is designed to map unambiguously to a hash table. TOML
should be easy to parse into data structures in a wide variety of languages.
This package loads toml file into python dictionary and dump dictionary into
toml file.


%package -n     python3-%{pypi_name}
Summary:        Python Library for Tom's Obvious, Minimal Language
BuildRequires:  python3-devel
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
TOML aims to be a minimal configuration file format that's easy to read due to
obvious semantics. TOML is designed to map unambiguously to a hash table. TOML
should be easy to parse into data structures in a wide variety of languages.
This package loads toml file into python dictionary and dump dictionary into
toml file.


%prep
%setup -q -n %{pypi_name}-%{version}
# Copy test files and make them executable so toml-test can work
cp -a %{SOURCE1} %{SOURCE2} .
chmod +x toml_test.py toml_test3.py


%build
%py2_build
%py3_build


%install
%py2_install
%py3_install


%check
# Using the language independent toml-test suite to launch tests
# link the the tests files
%if 0%{with_test}
ln -s /usr/share/toml-test/tests tests
toml-test $(pwd)/toml_test3.py
toml-test $(pwd)/toml_test.py
%endif


%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst
%{python2_sitelib}/%{pypi_name}-%{version}-py%{python2_version}.egg-info
%{python2_sitelib}/%{pypi_name}.py*

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/__pycache__/%{pypi_name}.cpython-*.py*

%changelog
* Mon Nov 9 2015 Julien Enselme <jujens@jujens.eu> - 0.9.1-4
- Correct %%python_provides for python3

* Thu Nov 5 2015 Julien Enselme <jujens@jujens.eu> - 0.9.1-3
- Rebuilt for python 3.5

* Sat Aug 8 2015 Julien Enselme <jujens@jujens.eu> - 0.9.1-2
- Enable tests suite
- Build python3 and python2 in the same directory
- Use %%py2_build, %%py3_build, %%py2_install and %%py2_install
- Move python2 package in its own subpackage

* Sat Jul 11 2015 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 0.9.1-1
- Update to 0.9.1 (#1242131)

* Sun Jun 28 2015 Julien Enselme <jujens@jujens.eu> - 0.9.0-2
- Update description to explain what toml is
- Try to import the package in %%check

* Mon Jun 15 2015 Julien Enselme <jujens@jujens.eu> - 0.9.0-1
- Initial packaging
