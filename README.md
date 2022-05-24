# cray-kubectl-kubelogin-plugin

This repo creates an rpm for installation on NCNs so `kubectl` commands will prompt for username and password.

The .version file in this repo should be updated to stay in sync with the version of the kubelogin
binary being bundled in the rpm.  The initial binary was pulled from:

https://github.com/int128/kubelogin/releases/download/v1.25.1/kubelogin_linux_amd64.zip

See https://github.com/int128/kubelogin for the latest `kubelogin` plugin info.
