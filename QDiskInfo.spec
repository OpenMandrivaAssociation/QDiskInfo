%global debug_package %{nil}

%global commit eae61beac7e5ef15a9570ad8509f308532b28050
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		QDiskInfo
Version:	0.3.git%{shortcommit}
Release:	3
URL:		https://github.com/edisionnano/QDiskInfo
Source0:	%{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Summary:	QDiskInfo is a frontend for smartctl
License:	GPL-3.0
Group:		Applications/System

BuildSystem: cmake
BuildOption: -DCMAKE_BUILD_TYPE:STRING=MinSizeRel
BuildOption: -DQT_VERSION_MAJOR=6
BuildOption: -DENABLE_TRANSLATIONS=ON

BuildRequires:	cmake
BuildRequires:	qt6-cmake
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	qt6-qttools-linguist-tools
BuildRequires:	vulkan-headers
BuildRequires:	lib64vulkan1

%description
QDiskInfo is a frontend for smartctl (part of the smartmontools package). It provides a user experience similar to CrystalDiskInfo. It shows the SMART (Self-Monitoring, Analysis, and Reporting Technology) data of modern hard disk drives.
%prep
%autosetup -n %{name}-%{commit} -p1

%files
%{_bindir}/QDiskInfo
%{_datadir}/applications/QDiskInfo.desktop
%{_datadir}/icons/hicolor/scalable/apps/QDiskInfo.svg
