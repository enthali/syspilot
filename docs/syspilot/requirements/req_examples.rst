Example Actors And Contracts
============================

.. req:: Example Actors And Example Contracts
   :id: SYSP_REQ_EXAMPLES
   :status: approved
   :implements: SYSP_US_EXAMPLES
   :realized_by: docs/Example Actors/index.md

   Syspilot shall ship generic examples of its actors and Contract processes
   that:

   - live in ``docs/Example Actors/`` and ``docs/Example Contracts/``, named
     after the existing ``docs/Syspilot Actors/`` and
     ``docs/Syspilot Contracts/`` folders, while those two folders stay
     Syspilot's own active artifacts;
   - hold in ``docs/Example Actors/`` the nine persistent role cards and an
     ``index.md`` that serves the documentation build and is not installed,
     because Setup generates the registry of an adopting project;
   - hold in ``docs/Example Contracts/`` a flat set of files, with no
     subfolder: every file other than ``index.md`` is one example Contract,
     namely ``contract-documents.md``, ``change.md``, ``release.md``, and
     ``process-maintenance.md``, and each is installed under its own file name
     directly in the adopting project's Contracts folder named after the
     project, so that
     the relative links between Contracts resolve in the source and in the
     copy; ``index.md`` serves the documentation build, is not installed, and
     carries above its ``Processes`` heading the preamble that Setup reuses
     for the registry of the adopting project; ``setup.md`` stays with
     ``docs/Syspilot Contracts/`` because the retained Setup record already
     holds the Setup Contract of an installation;
   - declare which Contract each example Contract requires, namely that every
     relative link between example Contracts is a link to
     ``contract-documents.md`` or to a Contract the Setup selection table
     lists as required, so that an installed Contract has no link that does
     not resolve;
   - carry in the Contracts only what holds for any adopting project, with
     project-specific values such as branch names, tag form, publication
     target, and workflow names left as values to fill in, and expect them to
     differ from ``docs/Syspilot Contracts/``;
   - name, in the role cards and Contracts, no installed folder such as
     ``docs/Syspilot Actors/`` or ``docs/Syspilot Contracts/``, because the
     installed folders carry the project's name and Setup substitutes no text
     in a seeded copy; the examples refer to their neighbours by relative
     links and to the project's Change Contracts by ``docs/changes/``;
   - keep each role card identical to its counterpart in
     ``docs/Syspilot Actors/`` after line-ending normalization, unless the
     ``Deviations`` table in ``docs/Example Actors/index.md`` names the card
     with the reason for the difference, so that a test can fail on an
     undeclared difference and on a declared deviation whose cards do not
     differ;
   - appear as two ``doc`` Needs owned by the Technical Writer, one per
     folder, whose ``:includes:`` links name the requirements whose content
     the folder carries, so that a changed requirement reaches the folder
     through its incoming ``included_in`` link;
   - stay plain Markdown without Needs markup and build with the
     documentation with zero warnings; and
   - are maintained in every Change by the Technical Writer through the
     Change Process's ``Example sync`` row.

.. vc:: Examples are generic, current, and declared
   :id: SYSP_VC_EXAMPLES_1
   :status: approved
   :verifies: SYSP_REQ_EXAMPLES

   Inspect both example folders, their ``doc`` Needs, and the documentation
   build. Confirm that the folders contain exactly the listed files, that
   ``docs/Example Contracts/`` has no subfolder and every file in it other
   than ``index.md`` is installable under its own name into the Contracts
   folder named after the project, that no role card or Contract example names an
   installed folder by its Syspilot name, that every relative link between example
   Contracts resolves to ``contract-documents.md`` or to a Contract the Setup
   selection table lists as required, that no Contract example names a
   Syspilot-specific repository path, workflow, branch, tag form, or
   publication target, and that ``setup.md`` is not among them. Run a test
   that fails when an example role card differs from its counterpart without
   a row in the ``Deviations`` table and when a row names a card that does not
   differ. Confirm that each ``doc`` Need links the requirements its folder
   carries, that those requirements list the folder through
   ``included_in``, and that the build reports zero warnings.
