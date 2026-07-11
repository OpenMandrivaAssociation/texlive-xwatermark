%global tl_name xwatermark
%global tl_revision 61719

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5.2d
Release:	%{tl_revision}.1
Summary:	Graphics and text watermarks on selected pages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/xwatermark
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xwatermark.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xwatermark.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package extends the author's draftmark and the watermark packages.
It is currently unmaintained and does not work with modern LaTeX
releases.

