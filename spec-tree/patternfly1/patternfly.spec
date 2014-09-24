%global make_common_opts \\\
	PACKAGE_NAME=%{name} \\\
	RPM_VERSION=%{version} \\\
	RPM_RELEASE=%{release} \\\
	DISPLAY_VERSION=%{version}-%{release} \\\
	PREFIX=%{_prefix} \\\
	DATAROOT_DIR=%{_datadir} \\\
	PKG_DATA_DIR=%{_datadir}/%{name} \\\
	%{nil}

Name:		patternfly1
Summary:	PatternFly open interface project and its dependencies
Version:	1.0.5
Release:	1%{?release_suffix}%{?dist}
License:	ASL 2.0
URL:		https://github.com/patternfly/patternfly
Source:		patternfly-1.0.5.tar.gz

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

%description
PatternFly open interface project, with dependencies bundled

%prep
%setup -q -n patternfly-1.0.5

%build
make %{?_smp_mflags} %{make_common_opts}

%install
rm -rf "%{buildroot}"
make %{?_smp_mflags} %{make_common_opts} install DESTDIR="%{buildroot}"

%files
%{_datadir}/%{name}/

%changelog
* Fri Jun 20 2014 Greg Sheremeta <gshereme@redhat.com> - 1.0.3-1
- Initial version.

