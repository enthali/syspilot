Example Actors And Contracts
============================

.. req:: Example Actors And Example Contracts
   :id: SYSP_REQ_EXAMPLES
   :status: approved
   :implements: SYSP_US_EXAMPLES
   :realized_by: docs/Example Actors/index.md

   Syspilot shall ship generic, plain-Markdown examples:

   - ``docs/Example Actors/`` contains nine persistent role cards and a
     documentation-only ``index.md``;
   - ``docs/Example Contracts/`` is flat and contains ``contract-documents.md``,
     ``change.md``, ``release.md``, ``process-maintenance.md`` and a
     documentation-only ``index.md``; Setup reuses its pre-``Processes`` preamble;
   - Contract examples install directly under their own file names; neither
     index nor Syspilot's ``setup.md`` is installed;
   - each inter-Contract relative link targets Contract Documents or a
     dependency declared in Setup's selection table and resolves after copying;
   - Contract examples leave project-specific branches, tag form, workflows,
     publication targets and repository paths as fill-in values;
   - role cards and Contracts name no installed Syspilot folder; they use
     neighbor-relative links and ``docs/changes/`` for project Change records;
   - example role cards match their active counterparts after line-ending
     normalization, except differences named with reasons in the ``Deviations``
     table of ``docs/Example Actors/index.md``;
   - the Technical Writer owns one ``doc`` Need per folder with ``includes``
     links for its requirements and incoming ``included_in`` impact;
   - examples contain no Needs markup and build with zero warnings; and
   - Technical Writer maintains them through every Change's ``Example sync`` row.

   ``docs/Syspilot Actors/`` and ``docs/Syspilot Contracts/`` remain Syspilot's
   active artifacts, not installation sources.

.. vc:: Example inventory is flat and installable
   :id: SYSP_VC_EXAMPLES_1
   :status: approved
   :verifies: SYSP_REQ_EXAMPLES

   Folder contents match the declared inventory; example Contracts have no
   subfolder, install under their own names and exclude Setup and the indexes.

.. vc:: Example links resolve without source-project assumptions
   :id: SYSP_VC_EXAMPLES_2
   :status: approved
   :verifies: SYSP_REQ_EXAMPLES

   Cross-Contract links target declared dependencies. Cards and Contracts
   contain no installed Syspilot folder or fixed project-specific values.

.. vc:: Example role-card differences have exact declarations
   :id: SYSP_VC_EXAMPLES_3
   :status: approved
   :verifies: SYSP_REQ_EXAMPLES

   Automated comparison rejects both an undeclared normalized difference and
   a deviation declaration whose cards are identical.

.. vc:: Example documentation exposes complete requirement impact
   :id: SYSP_VC_EXAMPLES_4
   :status: approved
   :verifies: SYSP_REQ_EXAMPLES

   Each folder's ``doc`` Need exposes all included requirements and incoming
   impact.

.. vc:: Example documents contain no Needs markup
   :id: SYSP_VC_EXAMPLES_5
   :status: approved
   :verifies: SYSP_REQ_EXAMPLES

   Markdown in both example folders contains no Needs markup.

.. vc:: Example documentation builds strictly
   :id: SYSP_VC_EXAMPLES_6
   :status: approved
   :verifies: SYSP_REQ_EXAMPLES

   The documentation build includes both example folders and reports zero warnings.
