# revision 28090
# category Package
# catalog-ctan /macros/latex/contrib/xwatermark
# catalog-date 2012-10-26 10:22:27 +0200
# catalog-license lppl1.3
# catalog-version 1.5.2d
Name:		texlive-xwatermark
Version:	1.5.2d
Release:	1
Summary:	Graphics and text watermarks on selected pages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xwatermark
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xwatermark.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xwatermark.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
