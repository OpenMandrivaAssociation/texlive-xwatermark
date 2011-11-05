# revision 23545
# category Package
# catalog-ctan /macros/latex/contrib/xwatermark
# catalog-date 2011-08-12 13:59:10 +0200
# catalog-license lppl1.3
# catalog-version 1.5.1
Name:		texlive-xwatermark
Version:	1.5.1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package extends the author's draftmark and the watermark
packages.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/xwatermark/xwatermark.sty
%doc %{_texmfdistdir}/doc/latex/xwatermark/README
%doc %{_texmfdistdir}/doc/latex/xwatermark/tab-globaloptions.tex
%doc %{_texmfdistdir}/doc/latex/xwatermark/tab-localoptions.tex
%doc %{_texmfdistdir}/doc/latex/xwatermark/xwatermark-examples.cfg
%doc %{_texmfdistdir}/doc/latex/xwatermark/xwatermark-examples1.pdf
%doc %{_texmfdistdir}/doc/latex/xwatermark/xwatermark-examples1.tex
%doc %{_texmfdistdir}/doc/latex/xwatermark/xwatermark-examples2.pdf
%doc %{_texmfdistdir}/doc/latex/xwatermark/xwatermark-examples2.tex
%doc %{_texmfdistdir}/doc/latex/xwatermark/xwatermark-guide.cfg
%doc %{_texmfdistdir}/doc/latex/xwatermark/xwatermark-guide.pdf
%doc %{_texmfdistdir}/doc/latex/xwatermark/xwatermark-guide.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
