# TODO:
# - make cgi version
Summary:	Program to manage /etc/passwd-like files
Summary(pl):	Program do zarządzania plikami podobnymi do /etc/passwd
Name:		chpwdfile
Version:	0.23
Release:	0.1
License:	GPL v2
Group:		Base/Authentication and Authorization
Source0:	ftp://eclipse.che.uct.ac.za/chpwdfile/%{name}-%{version}.tar.gz
# Source0-md5:	79abea076576d9a3015a5a8fdfa2d4b0
Patch0:		%{name}-DESTDIR.patch
URL:		http://eclipse.che.uct.ac.za/chpwdfile/
Requires:	pam_pwdfile
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a simple program to allow the administration of a text file
containing username:crypted_password pairs, useful if one uses
pam_pwdfile by Charl Botha.

Multiple password files can be administered and minimum password
lengths, etc, can be set in a configuration file on a per-file basis.
Trusted users can set these parameters on the command line and
manipulate other users' entries. Both DES and MD5 passwords are
supported.

<TODO>
A CGI version allows manipulation of a single password file via a
simple HTML form.
</TODO>

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	COPTS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README examples
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
