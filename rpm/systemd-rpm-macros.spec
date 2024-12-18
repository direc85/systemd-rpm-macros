#
# spec file for package systemd-rpm-macros
#
# Copyright (c) 2023 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.


Name:           systemd-rpm-macros
Version:        24
Release:        1
Summary:        RPM macros for systemd
License:        LGPL-2.1-or-later
Group:          Development/Tools/Building
URL:            http://en.opensuse.org/openSUSE:Systemd_packaging_guidelines
Source0:        macros.systemd
Requires:       coreutils
BuildArch:      noarch

# From macros.systemd
%global unitdir /usr/lib/systemd/system

%description

Provide RPM macros used to package systemd services files.

%prep

%build

%install
install -Dm644 %{SOURCE0} %{buildroot}%{_rpmconfigdir}/macros.d/macros.systemd
mkdir -p %{buildroot}%{unitdir}

%files
%defattr(-,root,root)
%{_rpmconfigdir}/macros.d/macros.systemd
%dir %{unitdir}

%changelog

