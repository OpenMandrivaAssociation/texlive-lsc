# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/lsc
# catalog-date 2007-03-09 12:50:50 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-lsc
Version:	20070309
Release:	7
Summary:	Typesetting Live Sequence Charts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lsc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lsc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lsc.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is similar to the msc package in that it provides
macros for typesetting a variant of sequence diagrams, in this
case the Live Sequence Charts of Damm and Harel. The package
supports the full LSC language of the original LSC paper, the
Klose-extensions for formal verification and some of the Harel-
extensions for the Play-In/Play-Out approach (cf. the manual).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bib/lsc/lsc.bib
%{_texmfdistdir}/tex/latex/lsc/lsc.sty
%doc %{_texmfdistdir}/doc/latex/lsc/README
%doc %{_texmfdistdir}/doc/latex/lsc/lsc.pdf
%doc %{_texmfdistdir}/doc/latex/lsc/lsc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070309-2
+ Revision: 753461
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070309-1
+ Revision: 718883
- texlive-lsc
- texlive-lsc
- texlive-lsc
- texlive-lsc

