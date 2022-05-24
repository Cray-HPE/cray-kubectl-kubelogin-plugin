# This spec file generates an RPM that installs the kubectl kubelogin binary
# scripts into the /usr/bin directory.
# Copyright 2022 Hewlett Packard Enterprise Development LP

%define bin_dir /usr/bin

Name: cray-kubectl-kubelogin-plugin
Vendor: Hewlett Packard Enterprise Company
License: HPE Proprietary 
Summary: Install kubectl kubelogin plugin
Version: %(cat .version) 
Release: %(echo ${BUILD_METADATA})
Source: %{name}-%{version}.tar.bz2

# Compiling not currently required:
# BuildArchitectures: noarch

%description
This RPM when installed will install and configure the /usr/bin/kubectl-oidc_login binary.

%files
%defattr(755, root, root)
%dir %{bin_dir}
%{bin_dir}/kubectl-oidc_login

%prep
%setup -q

%build

%install
install -m 755 -d %{buildroot}%{bin_dir}/
install -m 755 kubectl-oidc_login  %{buildroot}%{bin_dir}

exit 0
