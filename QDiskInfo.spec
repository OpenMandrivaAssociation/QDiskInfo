%global debug_package %{nil}

Name:		QDiskInfo
Version:	0.3
Release:	2
URL:		https://github.com/edisionnano/QDiskInfo
Source0:	%{url}/archive/refs/tags/%{version}.tar.gz
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
BuildRequires:	libvulkan-devel

%description
QDiskInfo is a frontend for smartctl (part of the smartmontools package). It provides a user experience similar to CrystalDiskInfo. It shows the SMART (Self-Monitoring, Analysis, and Reporting Technology) data of modern hard disk drives.
%prep
%autosetup -p1

%files
%{_bindir}/QDiskInfo
%{_datadir}/applications/QDiskInfo.desktop
%{_datadir}/icons/hicolor/scalable/apps/QDiskInfo.svg
