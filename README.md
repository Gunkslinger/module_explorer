<h1>Module Explorer</h1>
This is a terminal python script that I wrote while trying to teach myself python.
It will display information about the specified python module installed in the system
libraries, including the author's documentation contianed in the source file's docstrings.

It uses the <i>inspect</i> module and the <i>importlib</i> module to load and inspect the
module dynamically. This program does not handle packages yet, only modules. You'll probably
want to pipe the output to less. Running the program with no arguments will give you a usage
message.
