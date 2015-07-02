%global pypi_name toml

Name:           python-%{pypi_name}
Version:        0.9.0
Release:        2%{?dist}
Summary:        Python Library for Tom's Obvious, Minimal Language

License:        MIT
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://pypi.python.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel

%description
TOML aims to be a minimal configuration file format that's easy to read due to
obvious semantics. TOML is designed to map unambiguously to a hash table. TOML
should be easy to parse into data structures in a wide variety of languages.
This package loads toml file into python dictionary and dump dictionary into
toml file.


%package -n     python3-%{pypi_name}
Summary:        Python Library for Tom's Obvious, Minimal Language
BuildRequires:  python3-devel

%description -n python3-%{pypi_name}
TOML aims to be a minimal configuration file format that's easy to read due to
obvious semantics. TOML is designed to map unambiguously to a hash table. TOML
should be easy to parse into data structures in a wide variety of languages.
This package loads toml file into python dictionary and dump dictionary into
toml file.


%prep
%setup -q -n %{pypi_name}-%{version}
rm -rf %{py3dir}
cp -a . %{py3dir}

%build
pushd %{py3dir}
%{__python3} setup.py build
popd

%{__python2} setup.py build


%install
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}
popd

%{__python2} setup.py install -O1 --skip-build --root %{buildroot}


%check
# No test suite at present, so we'll just try importing
pushd %{py3dir}
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} -c "import toml"
popd

PYTHONPATH=%{buildroot}%{python2_sitelib} %{__python2} -c "import toml"


%files
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
* Sun Jun 28 2015 Julien Enselme <jujens@jujens.eu> - 0.9.0-2
- Update description to explain what toml is
- Try to import the package in %%check

* Mon Jun 15 2015 Julien Enselme <jujens@jujens.eu> - 0.9.0-1
- Initial packaging
