Summary:	Build Vagrant base boxes or KVM, VirtualBox and Fusion images
Name:		veewee
Version:	0.3.7
Release:	0.6
License:	MIT
Group:		Applications/Emulators
Source0:	https://github.com/jedi4ever/veewee/archive/v%{version}.tar.gz
# Source0-md5:	2b5a2f293eabe65b9c104258574e5967
URL:		http://github.com/jedi4ever/veewee/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	sed >= 4.0
Requires:	ruby-ansi < 1.4
Requires:	ruby-ansi >= 1.3.0
Requires:	ruby-childprocess
Requires:	ruby-highline
Requires:	ruby-i18n
Requires:	ruby-net-ssh >= 2.2.0
Requires:	ruby-popen4 < 0.2
Requires:	ruby-popen4 >= 0.1.2
Requires:	ruby-progressbar
Requires:	ruby-vnc < 1.1
Requires:	ruby-vnc >= 1.0.0
Requires:	vagrant >= 0.9
Suggests:	ruby-fission = 0.4.0
Suggests:	ruby-fog >= 1.8
Suggests:	ruby-grit
Conflicts:	ruby-fog >= 2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%{__sed} -i -e '1 s,#!.*ruby,#!%{__ruby},' bin/*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a bin/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md License
%attr(755,root,root) %{_bindir}/veewee
%{ruby_vendorlibdir}/%{name}.rb
%{ruby_vendorlibdir}/%{name}

%{ruby_vendorlibdir}/fission.rb
%dir %{ruby_vendorlibdir}/fission
%{ruby_vendorlibdir}/fission/config.rb

%dir %{ruby_vendorlibdir}/java
%{ruby_vendorlibdir}/java/README.txt
%{ruby_vendorlibdir}/java/dir2floppy.jar
%{ruby_vendorlibdir}/java/dir2floppy.java

%{ruby_vendorlibdir}/net/vnc/vnc.rb

%dir %{ruby_vendorlibdir}/python
%{ruby_vendorlibdir}/python/parallels_sdk_check.py
%{ruby_vendorlibdir}/python/parallels_send_key.py
%{ruby_vendorlibdir}/python/parallels_send_string.py

%{ruby_vendorlibdir}/vagrant_init.rb
