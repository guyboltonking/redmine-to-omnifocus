Installation
============

You should be able to download all the dependencies and install the
script by running:

    $ sudo python setup.py install

...to install for all users.

Branches
========

Note that you should use the redmine-1.2 branch if you're using
redmine-1.2, as the CSV column names appear to have changed (thanks to
FatherShawn for the patch).

Usage
=====

Here's the output from `redmine-to-omnifocus --help`:

<pre>
Usage: redmine-to-omnifocus [options] REDMINE-URL MY-NAME ISSUE-FOLDER-PATH ASSIGNED-CONTEXT-PATH WAITING-CONTEXT-PATH AVAILABLE-CONTEXT-PATH

Logs into the REDMINE-URL, retrieves the open issues, and inserts
them into ISSUE-FOLDER-PATH in OmniFocus.

  - REDMINE-URL: the URL of the redmine installation, e.g. "http://redmine.org"
  - ISSUE-FOLDER-PATH: colon-separated path to the OmniFocus folder
    under which Redmine tasks will be inserted e.g.
    "Earn a Living:Do work for clients"
  - MY-NAME: your full name in Redmine (not your login name); this is
    a regular expression, so you can match against a number of names,
    or compensate for changes in name representation.
  - ASSIGNED-CONTEXT-PATH: colon-separated path to the OmniFocus
    context that is set on tasks that are assigned to MY-NAME.
  - WAITING-CONTEXT-PATH: colon-separated path to the OmniFocus context that
    is set on tasks that are assigned to someone else.
  - AVAILABLE-CONTEXT-PATH: colon-separated path to the OmniFocus
    context that is set on tasks that are not assigned to anyone.

The idea is to get all your external tasks into one place.  You can
organise the imported tasks any way you like (including nesting them
inside each other), and the importer won't move them around _unless_
the project changes.  The context won't be changed unles the assignee
changes.  The task subject, descript, due date and completion status
will be overwritten on subsequent imports.

To use it, you should set the "Issues export limit" in Redmine's
"Issue Tracking" Settings tab to a high enough value such that all
issues are exported. The script also expects the date format to be set
in Redmine on the Display tab in Settings to the DD MMM YYYY format,
such as 19 Sep 2011.

The requirements are:
 
  1. Nothing is lost: If a task is assigned to you, then you must be
     able to see it in OmniFocus.

  2. Don't waste my time: Don't import things that you don't need to
     pay attention to:

     2.1. If you're not interested in a particular project and there are no
          tasks assigned to you in that project, you shouldn't have to track
          it in OmniFocus.

Tasks are inserted according to the following rules:

  1. A new task in Redmine will be added to a project with the same
     name in the ISSUE-FOLDER-PATH or one of its child folders.  If no
     matching project can be found, then a new project will be created
     under ISSUE-FOLDER-PATH if the task is assigned to MY-NAME.  If
     the issue has a target version, then the task will be inserted as
     a child of a task with that target version's name; the version
     task will be created if it doesn't exist.

  2. An OmniFocus task is considered to be a Redmine task if its name
     starts with '#'.

  3. The following attributes of an OmniFocus task will be set:

     - name: '#REDMINE-TASK-ID: REDMINE-SUBJECT'
     - note: The Redmine task description, a URL pointing to the task,
       misc. other useful stuff.
     - due date: The Redmine due date.
     - start date: The Redmine start date.
     - context:
       - If the Redmine task is assigned to MY-NAME, and the current
         context is WAITING, then make it AVAILABLE.
       - If the Redmine task is not assigned to ME, set the context to
         WAITING

  4. Tasks that have moved to a different project/version will be
     moved to that project/version; if the project isn't being tracked
     by OmniFocus, then the task is deleted.

  5. Tasks that are in OmniFocus and no longer in Redmine's open
     issues are set to be completed.

Options:
  -h, --help           show this help message and exit
  --username=USERNAME  Login as USERNAME
  --password=PASSWORD  Login with PASSWORD
  --use-growl          Use growl for notifications
</pre>
