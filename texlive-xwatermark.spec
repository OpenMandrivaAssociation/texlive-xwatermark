Name:		texlive-xwatermark
Version:	61719
Release:	2
Summary:	Graphics and text watermarks on selected pages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xwatermark
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xwatermark.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xwatermark.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package extends the author's draftmark and the watermark
packages.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/xwatermark/xwatermark.sty
%doc %{_texmfdistdir}/doc/latex/xwatermark/README
%doc %{_texmfdistdir}/doc/latex/xwatermark/xwatermark-examples1.tex
%doc %{_texmfdistdir}/doc/latex/xwatermark/xwatermark-examples2.pdf
%doc %{_texmfdistdir}/doc/latex/xwatermark/xwatermark-examples2.tex
%doc %{_texmfdistdir}/doc/latex/xwatermark/xwatermark-guide.pdf
%doc %{_texmfdistdir}/doc/latex/xwatermark/xwatermark-guide.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
