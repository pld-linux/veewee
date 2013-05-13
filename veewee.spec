# TODO
# - could be optional:
#   - grit
Summary:	Build Vagrant base boxes or KVM, VirtualBox and Fusion images
Name:		veewee
Version:	0.3.7
Release:	1
License:	MIT
Group:		Applications/Emulators
Source0:	https://github.com/jedi4ever/veewee/archive/v%{version}.tar.gz
# Source0-md5:	2b5a2f293eabe65b9c104258574e5967
Patch0:		install-root.patch
URL:		http://github.com/jedi4ever/veewee/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	sed >= 4.0
Requires:	ruby-ansi < 1.4
Requires:	ruby-ansi >= 1.3.0
Requires:	ruby-childprocess
Requires:	ruby-grit
Requires:	ruby-highline
Requires:	ruby-i18n
Requires:	ruby-net-ssh >= 2.2.0
Requires:	ruby-popen4 < 0.2
Requires:	ruby-popen4 >= 0.1.2
Requires:	ruby-progressbar
Requires:	ruby-thor < 1
Requires:	ruby-thor >= 0.15
Requires:	vagrant >= 0.9
# vnc: for vmware fusion and kvm
# fog: for libvirt (kvm)
Suggests:	ruby-cucumber >= 1.0.0
Suggests:	ruby-fission = 0.4.0
Suggests:	ruby-fog >= 1.8
Suggests:	ruby-vnc >= 1.0.1-1
Conflicts:	ruby-fog >= 2
Conflicts:	ruby-vnc > 1.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/%{name}

%description
Vagrant is a great tool to test new things or changes in a virtual
machine (Virtualbox) using either Chef or Puppet.

The first step is to download an existing 'base box'. I believe this
scares a lot of people as they don't know who or how this box was
built. Therefore lots of people end up first building their own base
box to use with vagrant.

Besides building Vagrant boxes, veewee can also be used for:
- create VMWare (fusion), KVM virtual machines
- interact with with those vms (up, destroy, halt, ssh)
- export them: OVA for fusion, IMG for KVM and ovf for VirtualBox

%prep
%setup -q
%patch0 -p1
%{__sed} -i -e '1 s,#!.*ruby,#!%{__ruby},' bin/*

# unvendor
# https://github.com/jedi4ever/veewee/commit/9f1163b53aa3ee82b0776c52bef92b74f6bd2cdb
rm lib/net/vnc/vnc.rb
%{__sed} -i -e 's,net/vnc/vnc.rb,net/vnc.rb,' lib/veewee/provider/core/box/vnc.rb

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{_bindir},%{_appdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a bin/* $RPM_BUILD_ROOT%{_bindir}
cp -a templates validation $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md License
%attr(755,root,root) %{_bindir}/veewee
%{ruby_vendorlibdir}/%{name}.rb
%{ruby_vendorlibdir}/%{name}
%{_appdir}

%{ruby_vendorlibdir}/fission.rb
%dir %{ruby_vendorlibdir}/fission
%{ruby_vendorlibdir}/fission/config.rb

%dir %{ruby_vendorlibdir}/java
%{ruby_vendorlibdir}/java/README.txt
%{ruby_vendorlibdir}/java/dir2floppy.jar
%{ruby_vendorlibdir}/java/dir2floppy.java

%dir %{ruby_vendorlibdir}/python
%{ruby_vendorlibdir}/python/parallels_sdk_check.py
%{ruby_vendorlibdir}/python/parallels_send_key.py
%{ruby_vendorlibdir}/python/parallels_send_string.py

%{ruby_vendorlibdir}/vagrant_init.rb
