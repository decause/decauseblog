<!-- 
.. title: Fedora 22 Beta Release!
.. slug: fedora-22-beta-release
.. date: 2015-04-21 15:23:27 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. LICENSE: CC-BY-SA-4.0
-->

Fedora 22 Beta Release Announcement
===================================

The Fedora 22 Beta release has arrived, with a preview of the latest
free and open source technology under development. Take a peek inside!

-   [Get Fedora 22 Beta
    Workstation](https://getfedora.org/en/workstation/prerelease/)
-   [Get Fedora 22 Beta
    Server](https://getfedora.org/en/server/prerelease/)
-   [Get Fedora 22 Beta
    Cloud](https://getfedora.org/en/cloud/prerelease/)
-   [Get Fedora 22 Beta
    Spins](https://spins.fedoraproject.org/prerelease)

What is the Beta release?
-------------------------

The Beta release contains all the exciting features of Fedora 22's
editions in a form that anyone can help test. This testing, guided by
the [Fedora QA team](QA "wikilink"), helps us target and identify bugs.
When these bugs are fixed, we make a Beta release available. A Beta
release is meant to be feature complete and bears a very strong
resemblance to the third and final release. The final release of Fedora
22 is expected in May.

We need your help to make Fedora 22 the best release yet, so please take
some time to download and try out the Beta and make sure the things that
are important to you are working. If you find a bug, please report
it – every bug you uncover (and/or help fix!) is a chance to improve
the experience for millions of Fedora users worldwide.

Together, we can make Fedora rock-solid. We have a culture of
coordinating new features and pushing fixes upstream as much as
feasible, and your feedback will help improve not only Fedora but Linux
and free software on the whole.

### Base platform

-   Faster and better dependency management: Yum has been replaced with
    dnf as the default package manager. Dnf has very similar command
    line options and configuration files compared to yum but also has
    several major internal changes including using libsolv in
    coordination with friends from the openSUSE project for faster and
    better dependency management. dnf-yum provides automatic redirection
    from yum to dnf in the command line for compatibility. The classic
    yum command line tool renamed to yum-deprecated as a transitional
    step for tools still using it.

### Fedora 22 Cloud

The Fedora 22 Cloud Edition builds on the work completed during the
Fedora 21 cycle, and brings in a number of improvements that make Fedora
22 a superb choice for running Linux in the cloud.

Ready for the Fedora 22 release, we have:

-   The latest versions of rpm-ostree and rpm-ostree-toolbox. You can
    even use rpm-ostree-toolbox to generate your own Atomic hosts from a
    custom set of packages.

-   Introduction of the Atomic command line tool to help manage Linux
    containers on Atomic Hosts and update Atomic Hosts.

### Fedora 22 Server

Fedora 22 Server Edition brings several changes that will improve Fedora
for use as a server in your environment.

-   Database Server Role: Fedora 21 introduced Rolekit, a daemon for
    Linux systems that provides a stable D-Bus interface to manage
    deployment of server roles. The Fedora 22 release adds onto that
    work with a database server role based on PostgreSQL.

-   Cockpit Updates: The Cockpit Web-based management application has
    been updated to the latest upstream release which adds many new
    features as well as a modular design for adding new functionality.

-   XFS as default filesystem. XFS scales better for servers and can
    handle higher storage capacity and we have made it the default
    filesystem for Fedora 22 server users. Other filesystems including
    Ext4 will continue to be supported and the ability to choose them
    have been retained.

### Fedora 22 Workstation

As always, Fedora carries a number of improvements to make life better
for its desktop users and developers! Here's some of the goodness you'll
get in Fedora 22 Workstation edition.

Enhancements:

-   The GNOME Shell notification system has been redesigned and subsumed
    into the calendar widget.
-   The Terminal now notifies you when a long running job completes.
-   The login screen now uses Wayland by default with automatic fallback
    to Xorg when necessary. This is a transitional step towards
    replacing Xorg with Wayland by default in the next release and
    should have no user visible difference.
-   Installation of GStreamer codecs, fonts, and certain document types
    is now handled by Software, instead of gnome-packagekit.
-   The Automatic Bug Reporting Tool (ABRT) now features better
    notifications, and uses the privacy control panel in GNOME to
    control information sent.

Appearance:

-   The Nautilus file manager has been improved to use GActions, from
    the deprecated GtkAction APIs, for a better, more consistent
    experience.
-   The GNOME Shell has a refreshed theme for better usability.
-   The Qt/Adwaita theme is now code complete, and Qt notifications have
    been improved for smoother experience using Qt-based apps in
    Workstation.

Under the covers:

-   Consistent input handling for graphical applications is provided
    using libinput library which is now used for both X11 and Wayland.

### Spins

Fedora spins are alternative versions of Fedora, tailored for various
types of users via hand-picked application sets or customizations. You
can browse all of the available spins via
http://spins.fedoraproject.org. Some of the popular ones include:

#### Fedora 22 KDE Plasma spin

Plasma 5, the successor to KDE Plasma 4, is now the default workspace in
the Fedora KDE spin. It has a new theme called Breeze, which has cleaner
visuals and better readability, improves certain work-flows and provides
overall more consistent and polished interface. Changes under the hood
include switch to Qt 5 and KDE Frameworks 5 and migration to fully
hardware-accelerated graphics stack based on OpenGL(ES).

#### Fedora 22 Xfce spin

The Xfce spin has been updated to Xfce 4.12. This release has an
enormous number of improvements, including HiDPI support, improvements
to window tiling, support for Gtk3 plugins, and many improvements for
multi-monitor support.

Issues and Details
------------------

This is an Beta release. As such, we expect that you may encounter bugs
or missing features. To report issues encountered during testing,
contact the Fedora QA team via the mailing list or in \#fedora-qa on
freenode.

As testing progresses, common issues are tracked on the Common F22
Bugs page:

https://fedoraproject.org/wiki/Common_F22_bugs

Roadmap
-------

While Fedora 22 is still under active development, we have a number of
new features developed in parallel for Fedora 23 as well. While all of
these features are work in progress and the plans have not been
finalized, we want to highlight a few major changes expected and invite
your early testing and feedback.

-   Wayland by default for Fedora 23 Workstation. XWayland will continue
    to be provided for compatibility with applications using X.

-   Python 3 by default for Fedora 23 Workstation: While most of the
    default applications are already using Python 3 in Fedora 22, Fedora
    23 Workstation will only include Python 3 by default. Python 2 will
    continue to be included in the repositories.

-   A Vagrant image for Fedora 23 Atomic Host and Cloud Images. We're
    supplying Vagrant boxes that work with KVM or VirtualBox, so users
    on Fedora will be able to easily consume the Vagrant images with
    KVM, and users on Mac OS X or Windows can use the VirtualBox image.

For tips on reporting a bug effectively, read "how to file a bug
report":

https://fedoraproject.org/wiki/How_to_file_a_bug_report

Release Schedule
----------------

The full release schedule is available on the Fedora wiki. The current
schedule calls for a final release in the end of May.

https://fedoraproject.org/wiki/Releases/22/Schedule

These dates are subject to change, pending any major bugs or issues
found during the testing process.
