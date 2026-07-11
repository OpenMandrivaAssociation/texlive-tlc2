%global tl_name tlc2
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Examples from The LaTeX Companion, second edition
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/examples/tlc2
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tlc2.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tlc2.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The source of the examples printed in the book, together with necessary
supporting files. The book was published by Addison-Wesley, 2004, ISBN
0-201-36299-6.

