Pristine Syspilot Setup
=======================

.. req:: Pristine Setup Contract
   :id: SYSP_REQ_SETUP
   :status: approved
   :implements: SYSP_US_SETUP
   :specializes: SYSP_REQ_CONTRACT_DOCUMENTS
   :realized_by: docs/Syspilot Contracts/setup.md

   Pristine Syspilot setup shall use a release-bound Setup Contract that:

   - receives the exact SemVer release tag and materialized release-bound
     Contract from the external bootstrap prompt, uses the supplied release
     without selecting or resolving another version, verifies its full Git
     commit identity, and uses that commit tree as the authoritative
     installation source;
   - owns all behavior after execution starts, including prerequisite checks,
     user interaction, installation, evidence, blockers, and handoff;
   - proceeds to its dedicated Setup branch only after confirming that the
     target is version controlled, the bootstrap-materialized
     ``.syspilot/setup-contract.md`` is its only working-tree change, and the
     User has approved the branch from the selected project state;
   - treats a confirmed existing Syspilot baseline as outside pristine Setup,
     but presents other possible Syspilot artifacts to the User for disposition
     instead of treating every similar artifact as an installation or deleting
     it;
   - copies Syspilot instructions and skills additively into an occupied
     ``.github/instructions/`` or ``.github/skills/`` directory, preserving
     existing unrelated files rather than requiring an empty destination, and
     surfaces an existing ignore rule that would silently exclude a generated
     destination as a blocker instead of a silent installation gap;
   - establishes Jarvis Core 0.32.0 or newer in the VS Code instance that
     hosts the initiating session, as ``SYSP_REQ_SETUP_JARVIS`` specifies,
     before any Jarvis-dependent action, and records an actionable blocker
     without claiming success when a mandatory prerequisite is unavailable;
   - distinguishes immutable release-owned product artifacts, seeded copies,
     generated project-instance artifacts, and protected user-owned
     configuration, where a seeded copy is copied from the example folders of
     the verified commit, is identical to its source when Setup verifies it,
     and belongs to the adopting project from the handoff to the Project
     Manager on, so that the project's later adaptation is never a deviation
     from the release;
   - installs the nine role cards from ``docs/Example Actors/`` as seeded
     copies at ``docs/<Project name> Actors/``, and the Contract processes the
     User selects from ``docs/Example Contracts/`` as seeded copies at
     ``docs/<Project name> Contracts/``, named after the project as
     ``SYSP_REQ_SETUP_NAMING`` specifies, so that an installed project carries
     its own name and no Syspilot folder name; does not install the
     Setup Process of ``docs/Syspilot Contracts/``, because the retained
     ``.syspilot/setup-contract.md`` holds the Setup Contract of the
     installation;
   - asks the User before the installation script is generated which example
     Contracts to install, recommends the Change Process alone as the start
     and says that the others can be added later, always installs Contract
     Documents because every Contract process links to it as its method, adds
     to the selection every Contract that a selected Contract requires and
     tells the User which it added, because the target's zero-warning
     documentation build would report a link that does not resolve, and
     records the final selection in the Setup Contract;
   - generates the process registry of the adopting project, whose preamble
     is the text of ``docs/Example Contracts/index.md`` above its
     ``Processes`` heading and whose list names exactly the installed
     Contracts, so that the registry never lists a Contract the project did
     not install and no installed Contract is missing from it;
   - installs all nine role cards whichever Contracts are selected, because a
     role card names no Contract process, and so an actor whose process is not
     installed has no assignment from that process until the project adopts
     it;
   - preserves an existing configured ontology regardless of whether it is
     defined in ``conf.py``, ``ubproject.toml``, or another TOML source, and
     installs the Syspilot baseline ontology only when no ontology exists;
   - independently preserves an existing Sphinx-Needs environment or, when
     Sphinx-Needs is absent, installs a supported project-local environment,
     records the Sphinx-Needs version of the environment it uses, and, when
     Setup itself has to bind an ontology through ``needs_from_toml``, stops
     with a recorded blocker and User guidance if that version is older than
     4.1.0, the first release with that configuration, instead of binding an
     ontology that the environment cannot read, while an existing configured
     ontology and its environment stay untouched whatever the version; it does
     so without overwriting existing
     project dependency or documentation files, and obtains User guidance for
     additive integration rather than replacing or evaluating project-owned
     configuration;
   - generates and audits one platform-appropriate installation script whose
     dry run and execution use the same declared operation path, retains
     identical destinations, and blocks on differing release-owned or seeded
     destinations that are not an approved integration;
   - records the supplied release tag, corresponding commit, and approved
     project baseline in the versioned ``.syspilot/project.toml`` file;
   - creates exactly the nine persistent Syspilot actors Project Manager,
     Architect, Developer, Tester, Quality, Release, Research, Technical
     Writer, and Admin through Jarvis, without creating a Setup actor, and
     verifies that Jarvis actor discovery includes all nine regardless of
     unrelated actors already present;
   - verifies the declared installation inventory and content integrity,
     installed structure, actor files and Jarvis discovery, successful
     zero-warning target documentation build with its selected ontology, and
     baseline readback before declaring the installation complete;
   - obtains User guidance to commit and merge the verified Setup branch into
     the selected target branch, completes that Git integration, and only then
     sends the Project Manager ``Installation complete, welcome to this
     project`` with the completion summary, the identity of the selected
     ontology, the installed Contracts, and first-project guidance that
     requires the Project Manager to
     explain its artifact types, statuses, and relationships and ask the User
     whether it fits the project;
   - continues normal project intake without an ontology Change when the User
     accepts the selected ontology, but when the User requests an adjustment,
     requires the Project Manager to start a normal Change before any ontology
     modification and uses the existing Ontology skill only as technical
     guidance within that Change;
   - exposes every unmet mandatory condition as explicit Contract evidence and
     does not produce a successful Project Manager handoff while blocked;
   - does not install or retain a persistent Setup actor;
   - permits a later technical update only when a separate project-specific
     Change records the old and proposed baselines, impact analysis,
     revalidation scope, authorization, and assigned technical executor; and
   - carries the shared rules of the Contract Document method in the form its
     executor allows, the executor being one session at a time, either the
     initiating session or the Admin actor to which the record is transferred:
     a Handover log whose entries, each with a note that states what the
     executor did and the facts that change the next owner's situation, record
     every transfer of the record, namely the transfer to the Admin when it
     occurs and the handoff to the Project Manager, in the commit that changes
     the header, the scope-change rule applied to gates that already passed,
     one statement of installed-artifact ownership in the inventory, one
     statement of verification-gate ownership
     naming the executor as sole owner, meaning the executor that the header
     names at that time, the Setup Contract opened in the User's editor in
     the step that asks for the Setup branch, and the Project Manager's
     refresh and header check before it acts on the completion message, after
     which it acknowledges the message and sets the Contract status
     ``handed off``.

.. vc:: Setup Contract establishes a reproducible project baseline
   :id: SYSP_VC_SETUP_1
   :status: approved
   :verifies: SYSP_REQ_SETUP

   Execute the materialized Setup Contract against a version-controlled
   project whose only initial working-tree change is that Contract, using the
   exact release tag supplied by the bootstrap prompt, and inspect the
   completed Contract, target Git history, installed inventory, Jarvis actor
   list, target documentation build, and
   ``.syspilot/project.toml``. Confirm that Setup uses the supplied release and
   corresponding full commit without selecting another version; possible
   pre-existing artifacts and documentation integration receive User-guided
   disposition; any existing ontology remains authoritative and the baseline
   ontology is installed only when none exists; Sphinx-Needs is independently
   preserved or installed as needed; unrelated project work and documentation
   infrastructure remain intact; the nine expected persistent Syspilot actors
   are discovered without a Setup actor; every
   mandatory gate records passing evidence before baseline verification and
   the Contract names the executor named in its header as sole owner of those
   gates; Git
   commit and merge complete before the Project Manager handoff; the handoff
   identifies the selected ontology and directs the Project Manager to explain
   its artifact types, statuses, and relationships and ask the User whether it
   fits; acceptance continues normal intake without an ontology Change, while
   a requested adjustment starts a normal Change before modification and uses
   the existing Ontology skill only for technical guidance; the nine role
   cards and the selected Contract processes are installed as seeded copies
   identical to their example sources, the User is asked which Contracts to
   install before the script is generated with the Change Process recommended
   first, Contract Documents and every required Contract are added to the
   selection, the generated registry lists exactly the installed Contracts,
   the role cards and Contracts are installed in the folders named after the
   project under ``SYSP_REQ_SETUP_NAMING``, and the Setup Process of
   ``docs/Syspilot Contracts/`` is not installed; blockers cannot
   report success; and later updates require an authorized project-specific
   Change. Confirm that an occupied ``.github/instructions/`` or
   ``.github/skills/`` destination keeps its existing unrelated files after
   installation, and that an ignore rule which would silently exclude a
   generated destination is reported as a blocker rather than passed over.

.. req:: Setup Establishes Jarvis Core In The Active Instance
   :id: SYSP_REQ_SETUP_JARVIS
   :status: approved
   :implements: SYSP_US_SETUP
   :specializes: SYSP_REQ_SETUP
   :realized_by: docs/Syspilot Contracts/setup.md

   The Setup Contract shall establish that ``enthali.jarvis-core`` 0.32.0 or
   newer is installed in the VS Code instance and profile that host the
   initiating session, the first release whose messaging tools are bound to
   Actor chats and which no longer offers ``jarvis_listChatSessions``, and
   shall offer to install it there when it is missing. It shall:

   - identify the hosting instance before it reads any extension list, from
     evidence about the running host and not from the first ``code`` command
     on the search path, because that command may address another
     installation: the process that hosts the session's shell, found from the
     shell's ancestry, with the installation it runs from and the
     ``--user-data-dir`` and ``--extensions-dir`` on its command line, or the
     platform defaults when the command line carries none, and the profile in
     use, recorded as evidence in the Setup record; the 2026-11-09 test run
     read a version through such a command and recorded Jarvis Core 0.32.0
     for a target whose own extension directory held no Jarvis package;
   - read the extension list with the command line tool of the identified
     installation and the recorded directories, and accept no version read
     anywhere else;
   - stop with a recorded blocker, without installing and without claiming a
     version, when the hosting instance cannot be identified with such
     evidence, as in a window attached to a remote host or container, and give
     the User the manual path: to install ``enthali.jarvis-core`` from the
     Extensions view of that window and tell the session to continue;
   - when Jarvis Core is absent or older than 0.32.0 in the identified
     instance, explain to the User in one step its purpose for Syspilot,
     namely persistent Actors and their messaging, the extension identifier
     and the Marketplace as its source, and the instance and profile that
     receive it, ask for consent there, install nothing without it, and stop
     with a recorded blocker and the manual path when the User refuses;
   - install only ``enthali.jarvis-core`` after consent, with the command
     line tool and directories that identified the instance, naming the
     profile when the instance uses one other than the default, and edit no
     User or project setting;
   - report an installation failure, with the exit status and the tool's
     output, record a blocker, and give the manual path, and not continue as
     if the installation had succeeded;
   - read the extension list again with the same tool and directories after
     the installation, require version 0.32.0 or newer, and then establish
     the tools that the session actually offers under
     ``SYSP_REQ_SETUP_CONTINUATION``, because an installed extension is not
     an available tool;
   - continue without a reload when the tools are offered after the
     installation, and report as a distinct condition, not as success, an
     extension that Setup installed in this run and whose tools the session
     does not offer, asking for a reload of the window only then, because the
     evidence concerns activation after Setup's own installation, whereas for
     an extension that was already present the ways forward of
     ``SYSP_REQ_SETUP_CONTINUATION`` apply; when it asks for the reload it
     records that it did and gives the User the resume prompt, composed in the
     language rule of ``SYSP_REQ_SETUP_CONTINUATION``, which tells a new chat
     in the reloaded window to continue the Pristine Syspilot Setup recorded
     in ``.syspilot/setup-contract.md`` and to read that record first, because
     a reload ends the chat session and nothing else tells a new session how
     to continue; the resumed session reads the Jarvis version and the tools of
     its session again, resumes from the recorded state, and keeps the before
     scan of the Actors folder; the observation of 2026-11-09, that Actor
     creation became available without a reload, was one reported run and is
     not a guarantee; and
   - perform every step up to the consent with no Jarvis tool, and record in
     the Setup record the instance evidence, the versions before and after,
     the consent or refusal, and the exit status of each command.

.. vc:: Setup finds and installs Jarvis Core in the active instance
   :id: SYSP_VC_SETUP_JARVIS_1
   :status: approved
   :verifies: SYSP_REQ_SETUP_JARVIS

   Inspect the Setup Contract and the records of Setup runs in an isolated
   VS Code instance that lacks Jarvis Core while another installation on the
   same machine has it. Confirm that the record holds the evidence that
   identified the hosting instance, installation, directories and profile,
   that the missing extension was detected in that instance and not read from
   the other installation, that the consent step names purpose, identifier,
   Marketplace, instance and profile, and that nothing is installed before the
   consent. Confirm for a refusal a blocker with the manual path and no
   installation, for a failed installation the exit status, the output and the
   manual path without a continued run, and for an instance that cannot be
   identified a blocker without an installation or a claimed version. Confirm
   after a successful installation the second read with the same tool and
   directories, version 0.32.0 or newer, and the tool check of the session; an
   extension that Setup installed and whose tools the session does not offer
   is reported as a distinct condition with a reload requested only then, the
   resume prompt is given and the resumed session reads version and tools
   again, and a run whose tools
   are offered continues without a reload. Confirm that the run did not read
   an experiment's launcher or run instructions from the target, because a
   recovery that followed such instructions does not show an uninstructed
   flow.

.. req:: Setup Continuation By The Admin
   :id: SYSP_REQ_SETUP_CONTINUATION
   :status: approved
   :implements: SYSP_US_SETUP
   :specializes: SYSP_REQ_SETUP
   :realized_by: docs/Syspilot Contracts/setup.md

   The Setup Contract shall establish which Jarvis tools its executing session
   offers before the first step that uses one, and shall transfer the Setup
   record to the Admin actor when the initiating session lacks a tool that a
   later step needs. It shall:

   - record, before the first step that uses a Jarvis tool and without
     assuming any tool, the ``enthali.jarvis-core`` version established under
     ``SYSP_REQ_SETUP_JARVIS`` and
     whether the initiating session offers ``jarvis_createActor``,
     ``jarvis_listActors``, ``jarvis_sendMessage``, and
     ``jarvis_receiveMessage``, because Jarvis binds the three messaging
     tools to the chats of Actors, so that an ordinary Copilot session does
     not offer them, while ``jarvis_createActor`` is a tool of the ordinary
     chat;
   - when the initiating session does not offer ``jarvis_createActor``, stop
     with a recorded blocker before any write to the target other than the
     Setup record, after the Actors-folder scan has been recorded, because
     Setup creates Actors only through Jarvis, and give the User two
     actionable ways forward: to enable ``jarvis_core_createActor`` in the
     Chat tool picker and tell the session to continue, or, when the tool is
     not offered at all, the manual creation path of
     ``SYSP_REQ_SETUP_ACTORS``;
   - keep the initiating session as executor, without a transfer, when it
     offers all four tools, and otherwise transfer the record to the Admin
     after the other eight Actors exist and the installation script has run,
     before the first verification gate that needs a tool the session lacks;
   - show the User, before the transfer, whether an Admin Actor already exists
     in the recorded scan and leave an existing Admin's files unchanged; for
     an existing Admin ask the User in that step whether Setup may append the
     request to ``.jarvis/messages/queue.json`` directly, naming the limit of
     that write, and stop without a transfer when the User declines to use the
     Admin at all;
   - in the transfer step for a created Admin, in this order, add ``Admin`` to
     ``.jarvis/messages/autodelivery.json`` unless it is listed, commit the
     record with ``Executor`` and ``Current responsibility`` set to ``Admin``
     and its Handover-log entry, and then create the Admin through
     ``jarvis_createActor`` with its ``summary`` and the request text as
     ``initialMessage``, so that a request never exists for a record that does
     not name the Admin, and so that Jarvis itself appends the request to
     ``.jarvis/messages/queue.json`` within its own process, because a
     separate read-modify-write of the shared queue by Setup can overwrite an
     entry that another writer added between Setup's read and write, which a
     read back cannot detect; Setup therefore does not write the queue file
     for a created Admin;
   - write ``.jarvis/messages/autodelivery.json`` as one read of the existing
     content, an addition, one write of the whole content, and a read back
     that shows every earlier name unchanged, stop with a recorded blocker
     when the file exists and is not a JSON array, and record as a stated
     limit that a concurrent write in that short interval could overwrite
     the file, which Jarvis writes only for a User's context-menu command;
   - in the transfer step for an existing Admin, which the User decided on
     2026-11-09 and which Jarvis offers no supported function for, because it
     drops an ``initialMessage`` for an existing Actor, add ``Admin`` to
     ``.jarvis/messages/autodelivery.json`` as above, commit the record naming
     the Admin, and only then, with the User's consent given in that step,
     append one entry with destination ``Admin``, sender ``Setup``, the
     request text, and an ISO 8601 UTC timestamp to
     ``.jarvis/messages/queue.json`` as one read of the existing content, an
     addition, one write of the whole content, and a read back that shows
     every entry read before the write unchanged, stopping with a recorded
     blocker when the existing file is not a JSON array; Setup records the
     limit as stated to the User: Jarvis writes this file without a lock from
     heartbeat jobs, reminders, and Actors, so an entry written between
     Setup's read and write is overwritten and no read back can show it, a
     risk the User judged very small in a freshly installed project; when the
     User withholds the consent, Setup writes neither the queue nor claims a
     queued request, commits the transfer, and gives the User the manual path
     with the manual prompt in the same step;
   - after a created or an existing Admin, leave the record to the Admin
     except to record a delivery blocker;
   - give the request text these elements and no other instruction: that it
     continues a Pristine Syspilot Setup whose initiating session lacks the
     Jarvis messaging tools; the absolute paths of the target project root and
     the Setup record; the instruction to re-read its own ``context.md``, its
     role card, and the Setup record and to verify that the header names the
     Admin as executor before acting; the instruction to continue from the
     first open phase of the record as its executor; and the statement that
     no Actor sent the request, which Jarvis or Setup queued, so that the
     acknowledgement is a
     row in the record's Evidence Summary and not a message;
   - compose the request and the manual prompt in the language the User used
     with the initiating session, and in English when that language is
     ambiguous, with paths, tool names, and file names unchanged, and record
     the language chosen and why;
   - take the Admin's acknowledgement row in the Setup record, committed in
     the Evidence Summary, as the only evidence of continuation, and wait up
     to 120 seconds after creating the Admin for it; read the queue only as a
     diagnostic, because the Admin's receipt removes the queue entry and with
     it its ``notified`` flag: without an acknowledgement, an entry that is
     present and ``notified`` means announced and not yet acted on, an entry
     that is present and not ``notified`` means automatic delivery has not
     run, and an entry that is absent means consumed or deleted, which cannot
     be told apart, so that no case is reported as delivered and a consumed
     request is never reported as a failed delivery once the row exists;
   - when Actor creation, automatic delivery, or continuation is unavailable
     or not evidenced in time, record a delivery blocker without claiming
     receipt, keep the committed header, and give the User the manual path,
     namely to open the chat of the Admin Actor from the ACTORS view and paste
     the manual prompt that the Setup record holds; and
   - require the Admin, as executor, to hold every later gate alone, to run the
     discovery check and the handoff to the Project Manager with its own
     messaging tools, and to append the Handover-log entry for that handoff.

.. vc:: Setup hands the record to the Admin when the session lacks tools
   :id: SYSP_VC_SETUP_CONTINUATION_1
   :status: approved
   :verifies: SYSP_REQ_SETUP_CONTINUATION

   Inspect the Setup Contract and the record of a Setup run that starts in an
   ordinary Copilot session. Confirm that the record lists the Jarvis version
   and, per tool, whether the session offers it, before the first step that
   uses one; that a session without ``jarvis_createActor`` leaves a blocker
   before any target write and offers both ways forward, the tool-picker
   instruction and the manual creation path; that a session with all four tools
   continues without a transfer; that for a session without the messaging
   tools the commit that names the Admin as executor, with its Handover-log
   entry, precedes the creation of the Admin with the request as
   ``initialMessage``, and that Setup writes ``.jarvis/messages/queue.json``
   for a created Admin nowhere; that the automatic-delivery list keeps every
   earlier name and a
   malformed file stops the run, and that the Contract states the limit of
   its short read-modify-write; that for an existing Admin the User's consent
   to the direct queue append is requested in the transfer step with the limit
   named, that the append follows the commit naming the Admin and keeps every
   entry read before the write, that a malformed queue file stops the run, and
   that without the consent nothing is written to the queue and the manual
   prompt is given; that the request text carries exactly the
   listed elements in the User's language, or
   in English when the language is ambiguous, with paths, tool names, and file
   names unchanged; that continuation is evidenced only by the Admin's row
   within 120 seconds, that the three queue observations are diagnostics
   which are never reported as delivery, that a request consumed by the
   Admin before Setup reads the queue is not reported as a failed delivery
   once the row exists, and that a failure leaves a
   delivery blocker and the manual path with the manual prompt; that an
   existing Admin is shown to the User, left unchanged, and then notified by
   the consented direct append or, without consent, by the manual prompt; and
   that the Admin
   alone passes the later gates and hands off to the Project Manager.

.. req:: Setup Creates The Actors Through Jarvis
   :id: SYSP_REQ_SETUP_ACTORS
   :status: approved
   :implements: SYSP_US_SETUP
   :specializes: SYSP_REQ_SETUP
   :realized_by: docs/Syspilot Contracts/setup.md

   The Setup Contract shall create the nine persistent Syspilot actors through
   Jarvis, by its creation tool or, when the session does not offer the tool,
   by its ACTORS view command, and shall:

   - call ``jarvis_createActor`` once per actor that the manual creation path
     does not create, from a session that offers it, with the exact actor name
     and a ``summary`` and without ``initialMessage``, except for the Admin in
     a transfer, which ``SYSP_REQ_SETUP_CONTINUATION`` creates with the request
     as ``initialMessage``, and write no ``actor.yaml`` or ``context.md``
     itself;
   - compose each ``summary`` as one paragraph that names the actor's domain,
     the project-root-relative path of its installed role card, and the
     instruction to read the project-root-relative path of the installed
     Contract registry, ``docs/<Project name> Contracts/index.md`` with the
     confirmed project name, at the start of every session and
     follow every applicable Contract process, because Jarvis writes the
     ``summary`` as the body of the new ``context.md`` and offers no other
     input for its content, so the two durable instructions arrive through the
     supported function;
   - write those paths as code spans that state they are relative to the
     project root, and not as relative links, because the depth of an Actor
     folder below the project root depends on ``jarvis.actors.folder`` and a
     link written for another depth resolves to a wrong place, as the
     ``../../docs`` link of the 2026-11-06 test run did;
   - resolve the Actors folder from the configured ``jarvis.actors.folder``
     (default ``.jarvis/actors``) and use the path that the tool returns for
     each Actor it created, and the path that the folder scan finds for each
     Actor the User created by the manual path, for the persistence decision
     and the ignore check, not a path it assumed;
   - show every target Actor that already exists to the User before creation;
     for an Actor that the tool reports as ``created: false`` it leaves the
     Actor's files unchanged and records it as pre-existing, with its returned
     path, instead of claiming it as configured by Setup;
   - record per Actor whether it was created or pre-existing and its returned
     path, and verify for each created Actor that both paths of its
     ``context.md`` resolve against the project root to installed files;
   - take the before state from a recorded scan of the Actors folder that
     lists the folder and name of every ``actor.yaml`` below it, and the after
     state from ``jarvis_listActors`` with up to 60 seconds allowed for the
     Jarvis rescan, and accept unrelated Actors in both; the scan is a
     different observation from the listing that the ordinary session cannot
     produce, because it has no listing tool and ``jarvis_listChatSessions``
     no longer exists, so the Contract records it as a scan and claims no
     equivalence to a listing;
   - offer, when ``jarvis_createActor`` is not offered, a manual creation path
     through the ``+`` command of the Jarvis ACTORS view, which creates an
     Actor by the same routine and asks for an optional Summary, in this
     order: Setup has confirmed the project name and recorded the before scan,
     both before it checks the tools so that they exist whichever way that
     check ends, then
     stops with the blocker and shows the User the nine exact names with their
     ``summary`` paragraphs, composed with the confirmed name, the User creates the Actors and enters each
     paragraph at the Summary prompt, and the resumed Setup keeps the recorded
     before scan, scans the folder again for the after observation, and
     writes nothing to the Actors, because Jarvis leaves the ``context.md`` of
     an Actor to the Actor itself; Setup counts an Actor as created for this
     Setup only when it was absent from the before scan, has one of the nine
     names, its ``context.md`` names both paths, and the User confirms
     explicitly, name by name, that the User created it for this Setup, because
     absence and content cannot show who created an Actor in a shared
     workspace; any other Actor, and any ambiguous or colliding state, is
     recorded as a blocker and not claimed; a ``context.md`` without both
     paths fails the Actor gate and the correction stays with the User;
   - itself write no message to any queue and call no messaging tool, except
     the one request to an existing Admin that the User consents to in the
     transfer step, the only other request to an Actor being the Admin's
     ``initialMessage``, which Jarvis queues; open no Actor session itself, and
     tell the User before creation
     that Jarvis opens the chat of a new Actor while
     ``jarvis.actors.openSessionOnCreate`` is enabled and that this setting
     turns it off, without editing the User's or the project's settings; and
   - create no Setup actor.

.. vc:: Setup creates usable Actors without touching existing ones
   :id: SYSP_VC_SETUP_ACTORS_1
   :status: approved
   :verifies: SYSP_REQ_SETUP_ACTORS

   Inspect the Setup Contract and the target project after a Setup run, once
   with no Actor present and once with one of the nine pre-existing. Confirm
   that each missing Actor was created by ``jarvis_createActor``, or, in the
   manual path, by the User, with a ``summary`` as specified and without
   ``initialMessage`` except for the Admin created in a transfer, that the
   Contract has no
   instruction to write ``actor.yaml`` or ``context.md`` directly, that each
   created ``context.md`` names the installed role card and the Contract
   registry as project-root-relative paths that resolve to existing files, that
   the pre-existing Actor is unchanged and recorded as pre-existing with its
   returned path, that the persistence decision and the ignore check used the
   returned paths, that the before state is recorded as a scan before the tool
   check and not called a listing, that Setup itself wrote no message to any
   queue except the consented request to an existing Admin, that discovery
   lists all nine Actors, and that no Setup
   actor exists. For a run in which ``jarvis_createActor`` is not offered,
   confirm that the before scan precedes the stop, that the manual path names
   the nine Actors with their ``summary``
   paragraphs, that the resumed Setup keeps the recorded scan, that Setup
   writes no file of those Actors, and that an Actor
   counts as created for this Setup only with the User's explicit name-by-name
   confirmation, absence from the before scan, and both paths in its
   ``context.md``, while any ambiguous or colliding state is a recorded
   blocker.

.. req:: Setup Verifies Before It Claims
   :id: SYSP_REQ_SETUP_GATES
   :status: approved
   :implements: SYSP_US_SETUP
   :specializes: SYSP_REQ_SETUP
   :realized_by: docs/Syspilot Contracts/setup.md

   The Setup Contract shall record its verification so that a claim of success
   cannot outrun its evidence, and shall:

   - record each mandatory gate with exactly one of the statuses ``pending``,
     ``passed``, and ``failed`` and with its evidence, and use no other status
     such as ``conditional``, because the 2026-11-06 test run recorded a
     conditional result for open gates and then claimed a verified baseline;
     the mandatory gates are exactly the rows of the Phase 5 verification
     table, and the Evidence Summary row ``PM handoff`` is a delivery row
     outside that rule, so that the status ``verified`` with the Project
     Manager named and ``PM handoff`` ``pending`` does not contradict it;
   - set the Contract status ``verified`` and ``baseline_status = "verified"``
     in ``.syspilot/project.toml`` only when every mandatory gate is
     ``passed``, and make the handoff in one commit after the Git integration
     that keeps the status ``verified``, names the Project Manager as
     ``Current responsibility``, appends the Handover-log entry, and records
     the Evidence Summary row ``PM handoff`` as ``pending``, because Contract
     handling requires the committed header before the message is sent and the
     status ``handed off`` claims a receipt that does not yet exist;
   - set the Contract status ``handed off`` and the row ``PM handoff`` to
     ``passed`` only in the Project Manager's own first commit on the record,
     after the Project Manager's refresh and header check and its
     acknowledgement of the message, so that the status shows a handoff that
     reached its receiver, and report completion to the User only after that
     acknowledgement, saying before it that the message was sent and the
     acknowledgement is awaited;
   - leave the record unchanged when sending the message fails, because the
     executor makes no change to a record it no longer holds: the state
     ``verified`` with the Project Manager named and ``PM handoff`` ``pending``
     is the visible state of an unacknowledged handoff, and the executor
     reports the failure to the User with the manual path, namely to tell the
     Project Manager's chat the path of the Setup record and to ask it to
     perform the refresh and header check;
   - keep the Contract status ``blocked``, ``baseline_status = "preparing"``,
     and a ``Current blocker`` that names the gate and the required action
     while any gate is ``pending`` or ``failed``, including the Jarvis actor
     discovery gate while the Actors are not listed after the allowed wait and
     the documentation gate while the build reports any warning, and make no
     handoff to the Project Manager in that state;
   - record the observed number of documentation warnings as the evidence of
     the documentation gate and require zero for ``passed``;
   - re-read the Setup record and ``.syspilot/project.toml`` before it seals
     the project state and before it hands off, and stop when the two disagree
     about the baseline status or when a gate is not ``passed``; and
   - keep a blocker that survives a transfer of the record visible in the
     header, so that the next executor starts from it.

.. vc:: Open or failed gates prevent verification and handoff
   :id: SYSP_VC_SETUP_GATES_1
   :status: approved
   :verifies: SYSP_REQ_SETUP_GATES

   Inspect the Setup Contract and fixture records. Confirm that every gate row
   has one of the three statuses and evidence, that the mandatory gates are
   exactly the rows of the Phase 5 table and the row ``PM handoff`` is outside
   them, that no other result word is
   allowed, and that the Contract states the conditions under which the
   statuses ``verified`` and ``handed off`` and the baseline status
   ``verified`` may be set. Using a record in which the discovery gate is
   ``pending``, and another in which the documentation gate is ``failed``
   with a warning count above zero, confirm that the Contract requires status
   ``blocked``, baseline status ``preparing``, a blocker naming the gate, and
   no handoff, and that the final re-read compares the record with
   ``.syspilot/project.toml``. Confirm for the handoff that the commit before
   the message keeps the status ``verified`` with the Project Manager named
   and ``PM handoff`` ``pending``, that only the Project Manager's first commit
   after its acknowledgement sets ``handed off`` and ``passed``, that the
   executor reports completion only after that acknowledgement, and that a
   failed send leaves the record unchanged and gives the User the manual path.

.. req:: Setup Generates A Neutral Documentation Scaffold
   :id: SYSP_REQ_SETUP_DOCS
   :status: approved
   :implements: SYSP_US_SETUP
   :specializes: SYSP_REQ_SETUP
   :realized_by: docs/Syspilot Contracts/setup.md

   When the target has no documentation configuration or root page, the Setup
   Contract shall generate them from definitions it carries, and shall:

   - take the project name as ``SYSP_REQ_SETUP_NAMING`` confirms it, show it
     again in the step that asks the User to approve the additive
     documentation edits, and carry no Syspilot project name,
     author, release, copyright, logo, or other Syspilot metadata into
     ``docs/conf.py``;
   - refer in ``docs/conf.py`` only to files and settings that the target has
     after installation, so that it names no template folder, static folder,
     logo, stylesheet, source-project path, or intersphinx inventory fetched
     from the network, loads only the extensions that the installed
     ``docs/requirements.txt`` provides and the installed pages need, binds
     the Needs configuration to the selected ontology path as the literal
     string assignment ``needs_from_toml = "<path relative to conf.py>"``,
     because the shipped Impact, MECE, and Trace skills read that literal
     without executing ``conf.py`` and fail on a computed binding, and
     excludes ``changes/*``, because Change Contracts are process records and
     not pages;
   - list in the generated ``docs/index.rst`` only pages that exist in the
     target, namely the two registries in the folders named after the
     project, ``<Project name> Actors/index`` and
     ``<Project name> Contracts/index``, and carry a hidden table of contents in each
     generated registry for the role cards or Contracts it installs, so that
     the zero-warning build has no orphaned page;
   - generate no hook that writes ``docs/ontology-reference.md`` and install
     no such page, because that page is Syspilot's own internal reference and
     the closed Change ``sphinx-needs-graph-alignment`` decided not to deliver
     it to installed projects; and
   - preserve every existing documentation file, so that for a target that has
     a documentation build it offers the registries and the changed navigation
     entries only as additive edits that the User approves.

.. vc:: The generated documentation builds without source-project pages
   :id: SYSP_VC_SETUP_DOCS_1
   :status: approved
   :verifies: SYSP_REQ_SETUP_DOCS

   Inspect the generated ``docs/conf.py`` and ``docs/index.rst`` of a pristine
   target after Setup and run its documentation build. Confirm that neither
   file names a Syspilot project name, release, logo, template or static
   folder, source-project page, or generation hook, that the root page lists
   only the two registries, that each registry has a hidden table of contents
   for exactly what was installed, that ``docs/ontology-reference.md`` is
   neither installed nor generated, that the selected ontology is bound as a
   literal ``needs_from_toml`` string, and
   that the build reports zero warnings. Confirm for a target with an existing
   documentation build that no existing file was overwritten, and for a
   target whose Sphinx-Needs is older than 4.1.0 and that has no ontology that
   the Setup record holds the observed version and a blocker with User
   guidance, and that no ``needs_from_toml`` binding is generated against that
   environment.

.. req:: Setup Names The Installed Folders After The Project
   :id: SYSP_REQ_SETUP_NAMING
   :status: approved
   :implements: SYSP_US_SETUP
   :specializes: SYSP_REQ_SETUP
   :realized_by: docs/Syspilot Contracts/setup.md

   The Setup Contract shall install the role cards and the Contract processes
   in two folders named after the adopting project, so that an installed
   project carries its own name and not Syspilot's, and shall:

   - propose the project name from the name of the target project folder, ask
     the User to confirm or change it in Phase 1, before the scan of the
     Actors folder and the check of the session's tools, because the stop of
     that check offers the manual Actor path whose summaries carry the name,
     and so before any destination is verified or written, record the
     confirmed name in the header of the Setup record, and use that one name
     for the two folders, the documentation scaffold, and every reference
     that follows from it, so that a name has no second source;
   - accept as the name only letters, digits, spaces, hyphens, underscores,
     and dots that are neither leading nor trailing, no name that consists of
     dots only, and no reserved Windows device name, because the name becomes
     a folder name, a Sphinx table-of-contents entry, and a Markdown path on
     every platform, and ask again instead of altering a name the User gave;
   - install the nine role cards at ``docs/<Project name> Actors/`` and the
     selected Contract processes at ``docs/<Project name> Contracts/``, where
     the name is followed by one space and the word ``Actors`` or
     ``Contracts``, with a registry generated into each folder under the title
     ``<Project name> Actors`` or ``<Project name> Contracts``;
   - generate from the confirmed name every reference to these folders: the
     registries, the entries of the generated root page, the project-root
     relative paths in each Actor's ``summary``, the paths in the handoff to
     the Project Manager, the evidence of the Setup record, and the additive
     navigation edits offered to a target that already has a documentation
     build;
   - leave the seeded copies identical to their example sources, so that no
     text of a role card or Contract is substituted and the Integrity gate
     still compares bytes, which holds because the example role cards and
     Contracts name no installed folder, a property that
     ``SYSP_REQ_EXAMPLES`` requires;
   - treat an existing folder at a project-named destination as the existing
     collision rule does: an identical file is retained and a differing file
     blocks unless the User approved the integration;
   - keep the confirmed name fixed once the first write to an installed
     destination has happened, that is from Phase 4 on, and not from the
     branch, the Setup record, or the dry run, and treat a later change as a
     widened scope after which the affected gates are opened again, as the
     Setup Contract states for every widened decision; and
   - leave the folders of the Syspilot source project, ``docs/Syspilot
     Actors/`` and ``docs/Syspilot Contracts/``, and the example folders under
     their own names, and migrate no existing project and rename no existing
     installation.

.. vc:: Installed folders carry the project name
   :id: SYSP_VC_SETUP_NAMING_1
   :status: approved
   :verifies: SYSP_REQ_SETUP_NAMING

   Inspect the Setup Contract and the target of a Setup run for a project
   whose name differs from Syspilot and contains a space. Confirm that the name
   was proposed from the target folder, confirmed by the User before the scan
   of the Actors folder, the tool check and any destination verification, and
   recorded in the header of the Setup record, so that the manual Actor path
   shows summaries that carry the confirmed name;
   that the two folders ``docs/<Project name> Actors/`` and
   ``docs/<Project name> Contracts/`` exist with the registries titled by the
   name and no folder named after Syspilot; that the root page, the Actor
   summaries, the handoff paths, and the record's evidence name those folders
   and that every path resolves; that a name with a forbidden character is
   asked for again and not altered; that the seeded copies are byte identical
   to their sources and the example sources contain no installed folder name;
   that an existing folder at a destination follows the collision rule; that
   a name changed after the first write to an installed destination opens the affected gates again; and
   that the documentation builds with zero warnings, which includes the name
   with its space in every table of contents.