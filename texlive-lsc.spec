# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/lsc
# catalog-date 2007-03-09 12:50:50 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-lsc
Version:	20070309
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This package is similar to the msc package in that it provides
macros for typesetting a variant of sequence diagrams, in this
case the Live Sequence Charts of Damm and Harel. The package
supports the full LSC language of the original LSC paper, the
Klose-extensions for formal verification and some of the Harel-
extensions for the Play-In/Play-Out approach (cf. the manual).

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
%{_texmfdistdir}/bibtex/bib/lsc/lsc.bib
%{_texmfdistdir}/tex/latex/lsc/lsc.sty
%doc %{_texmfdistdir}/doc/latex/lsc/README
%doc %{_texmfdistdir}/doc/latex/lsc/lsc.pdf
%doc %{_texmfdistdir}/doc/latex/lsc/lsc.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
