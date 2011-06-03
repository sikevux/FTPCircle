###ConnectionInfo 
Class that stores information about the FTP connection

###FTP 
An FTP client class.

    To create a connection, call the class using these arguments:
            host, user, passwd, acct, timeout

    The first four arguments are all strings, and have default value ''.
    timeout must be numeric and defaults to None if not passed,
    meaning that no timeout will be set on any ftp socket(s)
    If a timeout is passed, then this is now the default timeout for all ftp
    socket operations for this instance.

    Then use self.connect() with optional host and port argument.

    To download a file, use ftp.retrlines('RETR ' + filename),
    or ftp.retrbinary() with slightly different arguments.
    To upload a file, use ftp.storlines() or ftp.storbinary(),
    which have an open file as argument (see their definitions
    below for details).
    The download/upload functions first issue appropriate TYPE
    and PORT or PASV commands.
    

###FTPConnector 
 Class that connects to the FTP servers and takes care of interfaceing with the FTP

###FTPThread 
 Class to do the threaded fetching 

###FTP_TLS 
A FTP subclass which adds TLS support to FTP as described
        in RFC-4217.

        Connect as usual to port 21 implicitly securing the FTP control
        connection before authenticating.

        Securing the data connection requires user to explicitly ask
        for it by calling prot_p() method.

        Usage example:
        >>> from ftplib import FTP_TLS
        >>> ftps = FTP_TLS('ftp.python.org')
        >>> ftps.login()  # login anonimously previously securing control channel
        '230 Guest login ok, access restrictions apply.'
        >>> ftps.prot_p()  # switch to secure data connection
        '200 Protection level set to P'
        >>> ftps.retrlines('LIST')  # list directory content securely
        total 9
        drwxr-xr-x   8 root     wheel        1024 Jan  3  1994 .
        drwxr-xr-x   8 root     wheel        1024 Jan  3  1994 ..
        drwxr-xr-x   2 root     wheel        1024 Jan  3  1994 bin
        drwxr-xr-x   2 root     wheel        1024 Jan  3  1994 etc
        d-wxrwxr-x   2 ftp      wheel        1024 Sep  5 13:43 incoming
        drwxr-xr-x   2 root     wheel        1024 Nov 17  1993 lib
        drwxr-xr-x   6 1094     wheel        1024 Sep 13 19:07 pub
        drwxr-xr-x   3 root     wheel        1024 Jan  3  1994 usr
        -rw-r--r--   1 root     root          312 Aug  1  1994 welcome.msg
        '226 Transfer complete.'
        >>> ftps.quit()
        '221 Goodbye.'
        >>>
        

###Main 
Main class, connecting FTPConnector and Database, 
	takes care of UI input.
	To clearify: UI CALLS THIS CLASS WHICH WRAPPS THE WHOLE PROGRAM AND HELPS OTHER CLASSES TO INTERFACE WITH EACH OTHER (yay, caps.)

###ServerList 
Interface to serverlist.csv 

###__builtins__ 
dict() -> new empty dictionary
dict(mapping) -> new dictionary initialized from a mapping object's
    (key, value) pairs
dict(iterable) -> new dictionary initialized as if via:
    d = {}
    for k, v in iterable:
        d[k] = v
dict(**kwargs) -> new dictionary initialized with the name=value pairs
    in the keyword argument list.  For example:  dict(one=1, two=2)

###__cached__ 
str(string[, encoding[, errors]]) -> str

Create a new string object from the given encoded string.
encoding defaults to the current default string encoding.
errors can be 'strict', 'replace' or 'ignore' and defaults to 'strict'.

###__file__ 
str(string[, encoding[, errors]]) -> str

Create a new string object from the given encoded string.
encoding defaults to the current default string encoding.
errors can be 'strict', 'replace' or 'ignore' and defaults to 'strict'.

###__name__ 
str(string[, encoding[, errors]]) -> str

Create a new string object from the given encoded string.
encoding defaults to the current default string encoding.
errors can be 'strict', 'replace' or 'ignore' and defaults to 'strict'.

###search 
Scan through string looking for a match to the pattern, returning
    a match object, or None if no match was found.

###socket 
This module provides socket operations and some related functions.
On Unix, it supports IP (Internet Protocol) and Unix domain sockets.
On other systems, it only supports IP. Functions specific for a
socket are available as methods of the socket object.

Functions:

socket() -- create a new socket object
socketpair() -- create a pair of new socket objects [*]
fromfd() -- create a socket object from an open file descriptor [*]
gethostname() -- return the current hostname
gethostbyname() -- map a hostname to its IP number
gethostbyaddr() -- map an IP number or hostname to DNS info
getservbyname() -- map a service name and a protocol name to a port number
getprotobyname() -- map a protocol name (e.g. 'tcp') to a number
ntohs(), ntohl() -- convert 16, 32 bit int from network to host byte order
htons(), htonl() -- convert 16, 32 bit int from host to network byte order
inet_aton() -- convert IP addr string (123.45.67.89) to 32-bit packed format
inet_ntoa() -- convert 32-bit packed format IP to string (123.45.67.89)
socket.getdefaulttimeout() -- get the default timeout value
socket.setdefaulttimeout() -- set the default timeout value
create_connection() -- connects to an address, with an optional timeout and
                       optional source address.

 [*] not available on all platforms!

Special objects:

SocketType -- type object for socket objects
error -- exception raised for I/O errors
has_ipv6 -- boolean value indicating if IPv6 is supported

Integer constants:

AF_INET, AF_UNIX -- socket domains (first argument to socket() call)
SOCK_STREAM, SOCK_DGRAM, SOCK_RAW -- socket types (second argument)

Many other constants may be defined; these may be used in calls to
the setsockopt() and getsockopt() methods.


###sys 
This module provides access to some objects used or maintained by the
interpreter and to functions that interact strongly with the interpreter.

Dynamic objects:

argv -- command line arguments; argv[0] is the script pathname if known
path -- module search path; path[0] is the script directory, else ''
modules -- dictionary of loaded modules

displayhook -- called to show results in an interactive session
excepthook -- called to handle any uncaught exception other than SystemExit
  To customize printing in an interactive session or to install a custom
  top-level exception handler, assign other functions to replace these.

stdin -- standard input file object; used by input()
stdout -- standard output file object; used by print()
stderr -- standard error object; used for error messages
  By assigning other file objects (or objects that behave like files)
  to these, it is possible to redirect all of the interpreter's I/O.

last_type -- type of last uncaught exception
last_value -- value of last uncaught exception
last_traceback -- traceback of last uncaught exception
  These three are only available in an interactive session after a
  traceback has been printed.

Static objects:

float_info -- a dict with information about the float implementation.
int_info -- a struct sequence with information about the int implementation.
maxsize -- the largest supported length of containers.
maxunicode -- the largest supported character
builtin_module_names -- tuple of module names built into this interpreter
subversion -- subversion information of the build as tuple
version -- the version of this interpreter as a string
version_info -- version information as a named tuple
hexversion -- version information encoded as a single integer
copyright -- copyright notice pertaining to this interpreter
platform -- platform identifier
executable -- pathname of this Python interpreter
prefix -- prefix used to find the Python library
exec_prefix -- prefix used to find the machine-specific Python library
float_repr_style -- string indicating the style of repr() output for floats
__stdin__ -- the original stdin; don't touch!
__stdout__ -- the original stdout; don't touch!
__stderr__ -- the original stderr; don't touch!
__displayhook__ -- the original displayhook; don't touch!
__excepthook__ -- the original excepthook; don't touch!

Functions:

displayhook() -- print an object to the screen, and save it in builtins._
excepthook() -- print an exception and its traceback to sys.stderr
exc_info() -- return thread-safe information about the current exception
exit() -- exit the interpreter by raising SystemExit
getdlopenflags() -- returns flags to be used for dlopen() calls
getprofile() -- get the global profiling function
getrefcount() -- return the reference count for an object (plus one :-)
getrecursionlimit() -- return the max recursion depth for the interpreter
getsizeof() -- return the size of an object in bytes
gettrace() -- get the global debug tracing function
setcheckinterval() -- control how often the interpreter checks for events
setdlopenflags() -- set the flags to be used for dlopen() calls
setprofile() -- set the global profiling function
setrecursionlimit() -- set the max recursion depth for the interpreter
settrace() -- set the global debug tracing function


###Database 
Interface to the SQLite database. This is the class that will cache the servers filenames and also conduct searches.
		SQLite escapes are handled by the python SQL interface.

###__builtins__ 
dict() -> new empty dictionary
dict(mapping) -> new dictionary initialized from a mapping object's
    (key, value) pairs
dict(iterable) -> new dictionary initialized as if via:
    d = {}
    for k, v in iterable:
        d[k] = v
dict(**kwargs) -> new dictionary initialized with the name=value pairs
    in the keyword argument list.  For example:  dict(one=1, two=2)

###__cached__ 
str(string[, encoding[, errors]]) -> str

Create a new string object from the given encoded string.
encoding defaults to the current default string encoding.
errors can be 'strict', 'replace' or 'ignore' and defaults to 'strict'.

###__file__ 
str(string[, encoding[, errors]]) -> str

Create a new string object from the given encoded string.
encoding defaults to the current default string encoding.
errors can be 'strict', 'replace' or 'ignore' and defaults to 'strict'.

###__name__ 
str(string[, encoding[, errors]]) -> str

Create a new string object from the given encoded string.
encoding defaults to the current default string encoding.
errors can be 'strict', 'replace' or 'ignore' and defaults to 'strict'.

###ConnectionInfo 
Class that stores information about the FTP connection

###FTP 
An FTP client class.

    To create a connection, call the class using these arguments:
            host, user, passwd, acct, timeout

    The first four arguments are all strings, and have default value ''.
    timeout must be numeric and defaults to None if not passed,
    meaning that no timeout will be set on any ftp socket(s)
    If a timeout is passed, then this is now the default timeout for all ftp
    socket operations for this instance.

    Then use self.connect() with optional host and port argument.

    To download a file, use ftp.retrlines('RETR ' + filename),
    or ftp.retrbinary() with slightly different arguments.
    To upload a file, use ftp.storlines() or ftp.storbinary(),
    which have an open file as argument (see their definitions
    below for details).
    The download/upload functions first issue appropriate TYPE
    and PORT or PASV commands.
    

###FTPConnector 
 Class that connects to the FTP servers and takes care of interfaceing with the FTP

###FTPThread 
 Class to do the threaded fetching 

###FTP_TLS 
A FTP subclass which adds TLS support to FTP as described
        in RFC-4217.

        Connect as usual to port 21 implicitly securing the FTP control
        connection before authenticating.

        Securing the data connection requires user to explicitly ask
        for it by calling prot_p() method.

        Usage example:
        >>> from ftplib import FTP_TLS
        >>> ftps = FTP_TLS('ftp.python.org')
        >>> ftps.login()  # login anonimously previously securing control channel
        '230 Guest login ok, access restrictions apply.'
        >>> ftps.prot_p()  # switch to secure data connection
        '200 Protection level set to P'
        >>> ftps.retrlines('LIST')  # list directory content securely
        total 9
        drwxr-xr-x   8 root     wheel        1024 Jan  3  1994 .
        drwxr-xr-x   8 root     wheel        1024 Jan  3  1994 ..
        drwxr-xr-x   2 root     wheel        1024 Jan  3  1994 bin
        drwxr-xr-x   2 root     wheel        1024 Jan  3  1994 etc
        d-wxrwxr-x   2 ftp      wheel        1024 Sep  5 13:43 incoming
        drwxr-xr-x   2 root     wheel        1024 Nov 17  1993 lib
        drwxr-xr-x   6 1094     wheel        1024 Sep 13 19:07 pub
        drwxr-xr-x   3 root     wheel        1024 Jan  3  1994 usr
        -rw-r--r--   1 root     root          312 Aug  1  1994 welcome.msg
        '226 Transfer complete.'
        >>> ftps.quit()
        '221 Goodbye.'
        >>>
        

###Main 
Main class, connecting FTPConnector and Database, 
	takes care of UI input.
	To clearify: UI CALLS THIS CLASS WHICH WRAPPS THE WHOLE PROGRAM AND HELPS OTHER CLASSES TO INTERFACE WITH EACH OTHER (yay, caps.)

###ServerList 
Interface to serverlist.csv 

###__builtins__ 
dict() -> new empty dictionary
dict(mapping) -> new dictionary initialized from a mapping object's
    (key, value) pairs
dict(iterable) -> new dictionary initialized as if via:
    d = {}
    for k, v in iterable:
        d[k] = v
dict(**kwargs) -> new dictionary initialized with the name=value pairs
    in the keyword argument list.  For example:  dict(one=1, two=2)

###__cached__ 
str(string[, encoding[, errors]]) -> str

Create a new string object from the given encoded string.
encoding defaults to the current default string encoding.
errors can be 'strict', 'replace' or 'ignore' and defaults to 'strict'.

###__file__ 
str(string[, encoding[, errors]]) -> str

Create a new string object from the given encoded string.
encoding defaults to the current default string encoding.
errors can be 'strict', 'replace' or 'ignore' and defaults to 'strict'.

###__name__ 
str(string[, encoding[, errors]]) -> str

Create a new string object from the given encoded string.
encoding defaults to the current default string encoding.
errors can be 'strict', 'replace' or 'ignore' and defaults to 'strict'.

###search 
Scan through string looking for a match to the pattern, returning
    a match object, or None if no match was found.

###socket 
This module provides socket operations and some related functions.
On Unix, it supports IP (Internet Protocol) and Unix domain sockets.
On other systems, it only supports IP. Functions specific for a
socket are available as methods of the socket object.

Functions:

socket() -- create a new socket object
socketpair() -- create a pair of new socket objects [*]
fromfd() -- create a socket object from an open file descriptor [*]
gethostname() -- return the current hostname
gethostbyname() -- map a hostname to its IP number
gethostbyaddr() -- map an IP number or hostname to DNS info
getservbyname() -- map a service name and a protocol name to a port number
getprotobyname() -- map a protocol name (e.g. 'tcp') to a number
ntohs(), ntohl() -- convert 16, 32 bit int from network to host byte order
htons(), htonl() -- convert 16, 32 bit int from host to network byte order
inet_aton() -- convert IP addr string (123.45.67.89) to 32-bit packed format
inet_ntoa() -- convert 32-bit packed format IP to string (123.45.67.89)
socket.getdefaulttimeout() -- get the default timeout value
socket.setdefaulttimeout() -- set the default timeout value
create_connection() -- connects to an address, with an optional timeout and
                       optional source address.

 [*] not available on all platforms!

Special objects:

SocketType -- type object for socket objects
error -- exception raised for I/O errors
has_ipv6 -- boolean value indicating if IPv6 is supported

Integer constants:

AF_INET, AF_UNIX -- socket domains (first argument to socket() call)
SOCK_STREAM, SOCK_DGRAM, SOCK_RAW -- socket types (second argument)

Many other constants may be defined; these may be used in calls to
the setsockopt() and getsockopt() methods.


###Database 
Interface to the SQLite database. This is the class that will cache the servers filenames and also conduct searches.
		SQLite escapes are handled by the python SQL interface.

###__builtins__ 
dict() -> new empty dictionary
dict(mapping) -> new dictionary initialized from a mapping object's
    (key, value) pairs
dict(iterable) -> new dictionary initialized as if via:
    d = {}
    for k, v in iterable:
        d[k] = v
dict(**kwargs) -> new dictionary initialized with the name=value pairs
    in the keyword argument list.  For example:  dict(one=1, two=2)

###__cached__ 
str(string[, encoding[, errors]]) -> str

Create a new string object from the given encoded string.
encoding defaults to the current default string encoding.
errors can be 'strict', 'replace' or 'ignore' and defaults to 'strict'.

###__file__ 
str(string[, encoding[, errors]]) -> str

Create a new string object from the given encoded string.
encoding defaults to the current default string encoding.
errors can be 'strict', 'replace' or 'ignore' and defaults to 'strict'.

###__name__ 
str(string[, encoding[, errors]]) -> str

Create a new string object from the given encoded string.
encoding defaults to the current default string encoding.
errors can be 'strict', 'replace' or 'ignore' and defaults to 'strict'.

