# revision 25564
# category Package
# catalog-ctan /macros/latex/contrib/xwatermark
# catalog-date 2012-02-01 12:32:07 +0100
# catalog-license lppl1.3
# catalog-version 1.5.2a
Name:		texlive-xwatermark
Version:	1.5.2a
Release:	3
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
%doc %{_texmfdistdir}/doc/latex/xwatermark/xwatermark-test-20120201.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Fri Mar 09 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.5.2a-3
+ Revision: 783481
- rebuild without scriptlet dependencies

* Wed Mar 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.5.2a-2
+ Revision: 783098
- Update to latest release.

* Wed Feb 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.5.2a-1
+ Revision: 772178
- Update to latest release.

* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.5.2-2
+ Revision: 757703
- Rebuild to reduce used resources

* Fri Dec 09 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.5.2-1
+ Revision: 739945
- texlive-xwatermark

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.5.1-1
+ Revision: 719954
- texlive-xwatermark
- texlive-xwatermark
- texlive-xwatermark

