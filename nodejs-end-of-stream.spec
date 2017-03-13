%{?scl:%scl_package nodejs-%{module_name}}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global enable_tests 0
%global module_name end-of-stream

Name:           %{?scl_prefix}nodejs-%{module_name}
Version:        1.1.0
Release:        5%{?dist}
Summary:        Call a callback when a readable/writable/duplex stream has completed or failed

License:        MIT
URL:            https://github.com/mafintosh/end-of-stream
Source0:        http://registry.npmjs.org/%{module_name}/-/%{module_name}-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:  %{?scl_prefix}npm(tap)
BuildRequires:  %{?scl_prefix}npm(once)
%endif

%description
%{summary}.

%prep
%setup -q -n package
rm -rf node_modules

%nodejs_fixdep once

%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -pr package.json *.js %{buildroot}%{nodejs_sitelib}/%{module_name}
%nodejs_symlink_deps

%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
tap test.js
%endif

%files
%doc README.md LICENSE
%{nodejs_sitelib}/%{module_name}

%changelog
* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.1.0-5
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.1.0-4
- Rebuilt with updated metapackage

* Thu Jan 14 2016 Tomas Hrcka <thrcka@redhat.com> - 1.1.0-3
- Enable scl macros

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Dec 22 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.1.0-1
- Initial packaging
