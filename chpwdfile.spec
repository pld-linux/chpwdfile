# TODO:
# - make cgi version
Summary:	Program to manage /etc/passwd-like files
Summary(pl):	Program do zarz±dzania plikami podobnymi do /etc/passwd
Name:		chpwdfile
Version:	0.26
Release:	1
Epoch:		0
License:	GPL v2
Group:		Base/Authentication and Authorization
Source0:	ftp://eclipse.che.uct.ac.za/chpwdfile/%{name}-%{version}.tar.gz
# Source0-md5:	7f63f7c1ce95cedace94d18745038768
URL:		http://eclipse.che.uct.ac.za/chpwdfile/
Requires:	pam-pam_pwdfile
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

%description -l pl
Ten program pozwala na administrowanie plikami tekstowymi,
zawieraj±cymi pary login:zaszyfrowane_has³o, u¿yteczne przy u¿ywaniu
modu³u do PAM pam_pwdfile.

Mo¿liwe jest administrowanie wieloma plikami z has³ami, a opcje
minimalnej d³ugo¶ci hase³ itp. mog± byæ ustawione dla ka¿dego pliku
osobno. Zaufani u¿ytkownicy mog± ustawiaæ te opcje z linii poleceñ i
manipulowaæ wpisami innych u¿ytkowników. Obs³ugiwane s± has³a DES oraz
MD5.

<TODO>
Wersja CGI pozwala na operowanie pojedynczym plikiem z has³ami poprzez
prosty interfejs HTML.
</TODO>

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	COPTS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_sbindir} \
	MANDIR=%{_mandir}/man1

install examples/chpwdfile.conf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README examples
%attr(640,root,root) %config(noreplace) %{_sysconfdir}/chpwdfile.conf
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man1/*.1*
