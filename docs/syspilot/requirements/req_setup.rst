Pristine Syspilot Setup
=======================

.. req:: Pristine Setup Contract
   :id: SYSP_REQ_SETUP
   :status: approved
   :implements: SYSP_US_SETUP
   :specializes: SYSP_REQ_CONTRACT_DOCUMENTS
   :realized_by: docs/Syspilot Contracts/setup.md

   Pristine Setup shall use the release-bound materialized Setup Contract as
   authority for prerequisites, interaction, installation, evidence, blockers
   and handoff after bootstrap.
   One initiating session or transferred Admin shall execute it at a time.

   The record shall carry the shared rules in executor-appropriate form:
   transfers to Admin and Project Manager in the header-changing commit's
   Handover log, notes stating completed work and the next owner's situation,
   scope reassessment of passed gates, installed ownership once in the inventory,
   and verification-gate ownership naming the executor as sole owner.
   The Setup-branch request shall open the Contract in the User's editor;
   the receiving Project Manager shall refresh and verify authority before ACK.

.. vc:: Setup has one authoritative record and executor
   :id: SYSP_VC_SETUP_1
   :status: approved
   :verifies: SYSP_REQ_SETUP

   The materialized record governs execution with one executor and the shared
   rules, including committed transfers, sole gate ownership and same-step
   presentation of the Contract for branch approval.

.. req:: Setup Source And Target Identity
   :id: SYSP_REQ_SETUP_SOURCE
   :status: approved
   :implements: SYSP_US_SETUP
   :specializes: SYSP_REQ_SETUP
   :realized_by: docs/Syspilot Contracts/setup.md

   Setup shall use the exact supplied SemVer tag's verified full Git commit
   tree without selecting another version.
   Before its dedicated branch, the target shall be version controlled, the
   materialized ``.syspilot/setup-contract.md`` its only working-tree change,
   and the User shall approve the branch from the selected project state.
   A confirmed existing Syspilot baseline shall stop pristine Setup; other
   possible Syspilot artifacts shall receive User disposition, not deletion
   or automatic classification as an installation.
   Unavailable mandatory prerequisites shall be explicit blockers, not success.

.. vc:: Setup uses the supplied release identity
   :id: SYSP_VC_SETUP_SOURCE_1
   :status: approved
   :verifies: SYSP_REQ_SETUP_SOURCE

   The record and inventory identify the supplied tag and verified full source
   commit; no independently resolved version replaces them.

.. vc:: Setup starts from the materialized-record-only Git state
   :id: SYSP_VC_SETUP_SOURCE_2
   :status: approved
   :verifies: SYSP_REQ_SETUP_SOURCE

   Initial Git evidence shows a version-controlled target with only the
   materialized Setup record changed.

.. vc:: Setup branch creation has explicit User approval
   :id: SYSP_VC_SETUP_SOURCE_3
   :status: approved
   :verifies: SYSP_REQ_SETUP_SOURCE

   User approval identifies the dedicated branch and selected project state
   before branch creation.

.. vc:: Setup distinguishes baselines from possible artifacts
   :id: SYSP_VC_SETUP_SOURCE_4
   :status: approved
   :verifies: SYSP_REQ_SETUP_SOURCE

   A confirmed baseline stops pristine Setup; other possible Syspilot artifacts
   receive User disposition without unrelated deletion.

.. req:: Setup Installation Inventory
   :id: SYSP_REQ_SETUP_INSTALLATION
   :status: approved
   :implements: SYSP_US_SETUP
   :specializes: SYSP_REQ_SETUP
   :realized_by: docs/Syspilot Contracts/setup.md

   Setup shall distinguish immutable release-owned artifacts, seeded copies,
   generated project instances and protected User-owned configuration.
   Seeded copies shall match example sources at verification and belong to the
   project after handoff; subsequent project adaptation shall not be a release deviation.

   All nine role cards shall be installed from ``docs/Example Actors/`` and
   selected Contracts from ``docs/Example Contracts/`` in project-named folders.
   Neither source index nor Syspilot's Setup Process shall be copied as an
   installed Contract; the materialized Setup record shall remain available.
   Before script generation, the User shall choose Contracts, with Change
   recommended first and later addition explained. Contract Documents and all
   selected dependencies shall be added, disclosed and recorded.
   The generated process registry shall reuse the example index's pre-``Processes``
   preamble and list exactly the installed Contracts.

   Instructions and skills shall be copied additively into occupied destinations,
   preserving unrelated content. Ignored generated destinations shall block.
   The version-controlled ``.syspilot/project.toml`` shall record supplied tag,
   full source commit and approved project baseline.

.. vc:: Setup installs the declared source inventory
   :id: SYSP_VC_SETUP_INSTALLATION_1
   :status: approved
   :verifies: SYSP_REQ_SETUP_INSTALLATION

   Inventory and integrity evidence cover release-owned files, identical seeded
   copies, generated instances and retained User configuration with their
   declared ownership classes.

.. vc:: Setup Contract selection has complete dependencies
   :id: SYSP_VC_SETUP_INSTALLATION_2
   :status: approved
   :verifies: SYSP_REQ_SETUP_INSTALLATION

   The final User selection precedes script generation; required additions are
   disclosed and the generated registry lists exactly installed Contracts.
   All nine role cards are installed regardless of Contract selection.

.. vc:: Setup preserves unrelated occupied destinations
   :id: SYSP_VC_SETUP_INSTALLATION_3
   :status: approved
   :verifies: SYSP_REQ_SETUP_INSTALLATION

   Existing unrelated instruction/skill files survive additive installation;
   no occupied directory is required to be empty.

.. vc:: Ignored Setup outputs block installation
   :id: SYSP_VC_SETUP_INSTALLATION_4
   :status: approved
   :verifies: SYSP_REQ_SETUP_INSTALLATION

   An ignore rule excluding a generated destination produces a recorded blocker.

.. vc:: Setup baseline records the approved installation identity
   :id: SYSP_VC_SETUP_INSTALLATION_5
   :status: approved
   :verifies: SYSP_REQ_SETUP_INSTALLATION

   Version-controlled baseline readback matches the supplied tag, full source
   commit and approved project state.

.. req:: Setup Script Integrity
   :id: SYSP_REQ_SETUP_SCRIPT
   :status: approved
   :implements: SYSP_US_SETUP
   :specializes: SYSP_REQ_SETUP
   :realized_by: docs/Syspilot Contracts/setup.md

   Setup shall generate and audit one platform-appropriate installation script.
   Dry run and execution shall share the declared operation path.
   Identical destinations shall be retained; differing release-owned or seeded
   destinations shall block unless the User approved integration.
   Verification shall cover inventory, content integrity and installed structure.

.. vc:: Setup execution follows the audited plan
   :id: SYSP_VC_SETUP_SCRIPT_1
   :status: approved
   :verifies: SYSP_REQ_SETUP_SCRIPT

   Dry-run and execution evidence identify the same operations, retained
   identical files and only approved differing integrations; inventory and
   integrity checks agree with installed outputs.

.. req:: Setup Preserves Project Ontology And Environment
   :id: SYSP_REQ_SETUP_ONTOLOGY
   :status: approved
   :implements: SYSP_US_SETUP
   :specializes: SYSP_REQ_SETUP
   :realized_by: docs/Syspilot Contracts/setup.md

   Setup shall preserve existing ontology configuration in ``conf.py``,
   ``ubproject.toml`` or another TOML source; when none exists it shall copy
   the Example Ontology folder to ``docs/<Project name> Ontology/`` and bind
   its ``ontology.toml``, and it shall copy no Syspilot-owned ontology.
   Independently, it shall preserve an existing Sphinx-Needs environment or
   install a supported project-local one when absent, recording the version used.
   A Setup-created ``needs_from_toml`` binding shall require Sphinx-Needs 4.1.0
   or newer; an older version shall block with User guidance before binding.
   Existing configured ontology/environment shall remain untouched regardless
   of version. Dependency/documentation integration shall be additive and
   User-guided, not replacement or evaluation of project-owned configuration.

.. vc:: Setup preserves ontology and environment independently
   :id: SYSP_VC_SETUP_ONTOLOGY_1
   :status: approved
   :verifies: SYSP_REQ_SETUP_ONTOLOGY

   Existing ontology/environment cases remain unchanged; absent components
   alone are installed, without overwriting project dependency or documentation files.
   Without an existing ontology the installed folder equals the Example Ontology
   under the project-named folder and the generated binding names it.

.. vc:: Setup does not create an unsupported ontology binding
   :id: SYSP_VC_SETUP_ONTOLOGY_2
   :status: approved
   :verifies: SYSP_REQ_SETUP_ONTOLOGY

   Recorded versions below 4.1.0 block a new TOML binding with guidance, while
   already configured projects remain untouched.

.. req:: Setup Establishes Jarvis In The Hosting Instance
   :id: SYSP_REQ_SETUP_JARVIS
   :status: approved
   :implements: SYSP_US_SETUP
   :specializes: SYSP_REQ_SETUP
   :realized_by: docs/Syspilot Contracts/setup.md

   Setup shall establish ``enthali.jarvis-core`` 0.32.0 or newer in the hosting
   VS Code instance/profile before Jarvis-dependent work, using no Jarvis tool
   to establish identity or obtain installation consent.
   Instance evidence shall identify the shell-host process ancestry,
   installation, profile and command-line ``--user-data-dir``/``--extensions-dir``
   or their platform defaults. Extension versions shall be read only through
   that installation's tool and recorded directories, never an arbitrary PATH command.

   A missing/older extension shall require consent naming its purpose
   (persistent Actors and messaging), extension ID, Marketplace source and
   receiving instance/profile. Only that extension shall
   be installed; no User/project settings shall be edited.
   Refusal, unidentified host or failed installation shall stop with recorded
   blockers and the window's Extensions-view manual path. An unidentified host
   shall yield no claimed version; failed commands shall retain exit/output evidence.

   After installation, Setup shall re-read the version with the same tool and
   establish offered session tools. It shall request reload only for an
   extension installed in this run whose needed tools remain unavailable,
   otherwise continuing without reload or using the continuation alternatives.
   Reload evidence shall include a language-appropriate prompt to read and
   resume ``.syspilot/setup-contract.md``; resumed execution shall recheck version
   and tools and retain the recorded before scan.
   Instance, before/after versions, consent/refusal and command exit statuses
   shall be recorded.

.. vc:: Jarvis detection addresses the actual host
   :id: SYSP_VC_SETUP_JARVIS_1
   :status: approved
   :verifies: SYSP_REQ_SETUP_JARVIS

   In an isolated host missing Jarvis while another installation has it,
   evidence identifies the host directories/profile and detects the local
   absence, without claiming the other installation's version. An unidentified
   host blocks with the manual path, no installation and no version claim.

.. vc:: Jarvis installation has informed User consent
   :id: SYSP_VC_SETUP_JARVIS_2
   :status: approved
   :verifies: SYSP_REQ_SETUP_JARVIS

   Consent precedes installation and names purpose, extension ID, source,
   instance and profile. Refusal blocks with the manual path and no installation.

.. vc:: Jarvis activation resumes only from observed state
   :id: SYSP_VC_SETUP_JARVIS_3
   :status: approved
   :verifies: SYSP_REQ_SETUP_JARVIS

   Post-installation evidence rechecks the same instance and session tools;
   reload occurs only under the stated condition with a resume prompt.
   Resumed version/tool checks retain the before scan.

.. vc:: Jarvis runtime evidence is an uninstructed flow
   :id: SYSP_VC_SETUP_JARVIS_4
   :status: approved
   :verifies: SYSP_REQ_SETUP_JARVIS

   A recorded Setup run did not use an experiment launcher or target-resident
   run instructions to supply a recovery that the Contract itself lacks.

.. vc:: Jarvis installation failure remains explicit
   :id: SYSP_VC_SETUP_JARVIS_5
   :status: approved
   :verifies: SYSP_REQ_SETUP_JARVIS

   Failed installation records exit status/output, a blocker and the manual
   path; no successful continuation is claimed.

.. req:: Setup Continuation By The Admin
   :id: SYSP_REQ_SETUP_CONTINUATION
   :status: approved
   :implements: SYSP_US_SETUP
   :specializes: SYSP_REQ_SETUP
   :realized_by: docs/Syspilot Contracts/setup.md

   Before tool-dependent work, Setup shall record Jarvis version and availability
   of ``jarvis_createActor``, ``jarvis_listActors``, ``jarvis_sendMessage`` and
   ``jarvis_receiveMessage``.
   Missing creation shall block target writes except the record, after the
   before scan, with tool-picker ``jarvis_core_createActor`` and manual-creation
   alternatives. All four available tools shall keep the initiating executor;
   otherwise ``SYSP_REQ_SETUP_ADMIN_TRANSFER`` shall apply after the script and
   other eight Actors, before an unavailable-tool gate.

.. vc:: Setup routes by actually offered tools
   :id: SYSP_VC_SETUP_CONTINUATION_1
   :status: approved
   :verifies: SYSP_REQ_SETUP_CONTINUATION

   Tool/version evidence precedes use; missing creation blocks writes with both
   alternatives, all four tools retain the executor, and missing messaging
   transfers only after the script and other Actors.

.. req:: Setup Admin Transfer Authority
   :id: SYSP_REQ_SETUP_ADMIN_TRANSFER
   :status: approved
   :implements: SYSP_US_SETUP
   :specializes: SYSP_REQ_SETUP_CONTINUATION
   :realized_by: docs/Syspilot Contracts/setup.md

   Setup shall show whether Admin exists, preserve existing Admin files and
   stop without transfer if the User declines Admin use.
   After ``SYSP_REQ_SETUP_AUTODELIVERY``, it shall commit executor/responsibility
   and the Handover log to Admin before any request under
   ``SYSP_REQ_SETUP_ADMIN_DELIVERY`` exists.
   Thereafter the initiator shall change only delivery-blocker evidence;
   Admin alone shall own later gates, discovery and the logged Project Manager
   handoff with its own messaging tools.

.. vc:: Setup commits Admin authority before requesting continuation
   :id: SYSP_VC_SETUP_CONTINUATION_2
   :status: approved
   :verifies: SYSP_REQ_SETUP_ADMIN_TRANSFER

   The Admin executor/responsibility and log commit follows autodelivery
   preparation and precedes request creation or append.

.. vc:: Setup respects the existing Admin disposition
   :id: SYSP_VC_SETUP_CONTINUATION_6
   :status: approved
   :verifies: SYSP_REQ_SETUP_ADMIN_TRANSFER

   Setup shows the existing/absent Admin state and preserves existing files;
   User refusal to use Admin leaves responsibility untransferred.

.. vc:: Transferred Setup work has one executor
   :id: SYSP_VC_SETUP_CONTINUATION_7
   :status: approved
   :verifies: SYSP_REQ_SETUP_ADMIN_TRANSFER

   After transfer, initiator edits are limited to delivery blockers; Admin
   performs later gates, discovery and the logged Project Manager handoff.

.. req:: Setup Admin Autodelivery Registration
   :id: SYSP_REQ_SETUP_AUTODELIVERY
   :status: approved
   :implements: SYSP_US_SETUP
   :specializes: SYSP_REQ_SETUP_CONTINUATION
   :realized_by: docs/Syspilot Contracts/setup.md

   Setup shall add Admin to ``.jarvis/messages/autodelivery.json`` unless listed,
   using one read/add/whole-file write/readback that preserves earlier names.
   A non-array file shall block. Setup shall state and record that concurrent
   writes can overwrite this unlocked update despite readback.

.. vc:: Setup autodelivery writes preserve their stated limits
   :id: SYSP_VC_SETUP_CONTINUATION_3
   :status: approved
   :verifies: SYSP_REQ_SETUP_AUTODELIVERY

   A single update/readback retains earlier names and adds Admin if needed;
   non-array input blocks, and the recorded limit admits undetectable overwrite.

.. req:: Setup Admin Delivery Route
   :id: SYSP_REQ_SETUP_ADMIN_DELIVERY
   :status: approved
   :implements: SYSP_US_SETUP
   :specializes: SYSP_REQ_SETUP_CONTINUATION
   :realized_by: docs/Syspilot Contracts/setup.md

   After the committed authority transfer, Setup shall create a new Admin last
   with summary and request as ``initialMessage``, writing no queue request itself.
   For an existing Admin, it shall request queue-append consent in the transfer
   step, stating the race limit of ``SYSP_REQ_SETUP_ADMIN_QUEUE``.
   Consent shall permit that append; without consent, Setup shall write no queue
   and claim no queued request, giving the manual prompt in the same step.

.. vc:: New Admin delivery uses only Jarvis creation
   :id: SYSP_VC_SETUP_CONTINUATION_8
   :status: approved
   :verifies: SYSP_REQ_SETUP_ADMIN_DELIVERY

   New Admin is created last with summary and request initialMessage; Setup
   does not write that request to the queue.

.. vc:: Existing Admin delivery respects queue consent
   :id: SYSP_VC_SETUP_CONTINUATION_9
   :status: approved
   :verifies: SYSP_REQ_SETUP_ADMIN_DELIVERY

   Transfer-step consent names the queue race. A refusal yields the same-step
   manual prompt without a queue write or queued-request claim.

.. req:: Setup Existing-Admin Queue Append
   :id: SYSP_REQ_SETUP_ADMIN_QUEUE
   :status: approved
   :implements: SYSP_US_SETUP
   :specializes: SYSP_REQ_SETUP_CONTINUATION
   :realized_by: docs/Syspilot Contracts/setup.md

   The append authorized by ``SYSP_REQ_SETUP_ADMIN_DELIVERY`` shall update
   ``.jarvis/messages/queue.json`` once by read/add/whole-file write/readback,
   preserving earlier-read entries and adding destination Admin, sender Setup,
   request text and UTC ISO timestamp. A non-array file shall block.
   Setup shall state and record that unlocked concurrent writes may be lost
   undetectably despite readback.

.. vc:: Existing Admin queue updates retain their declared integrity
   :id: SYSP_VC_SETUP_CONTINUATION_10
   :status: approved
   :verifies: SYSP_REQ_SETUP_ADMIN_QUEUE

   One append/readback retains earlier-read entries and the required new fields;
   non-array input blocks and concurrent preservation is not guaranteed.

.. req:: Setup Continuation Request Content
   :id: SYSP_REQ_SETUP_CONTINUATION_REQUEST
   :status: approved
   :implements: SYSP_US_SETUP
   :specializes: SYSP_REQ_SETUP_CONTINUATION
   :realized_by: docs/Syspilot Contracts/setup.md

   Request and manual prompt shall contain only: continuation of pristine Setup
   because the initiator lacks messaging tools; absolute project/record paths;
   own context/role/record refresh and Admin executor-header check; continuation
   from the first open phase; and non-Actor origin requiring acknowledgement
   in the record's Evidence Summary, not a message.

.. vc:: Setup continuation prompts contain only the required context
   :id: SYSP_VC_SETUP_CONTINUATION_4
   :status: approved
   :verifies: SYSP_REQ_SETUP_CONTINUATION_REQUEST

   Request/manual text has the declared purpose, paths, refresh, authority,
   next-phase and acknowledgement instructions, with no extra instruction.

.. req:: Setup Continuation Language
   :id: SYSP_REQ_SETUP_CONTINUATION_LANGUAGE
   :status: approved
   :implements: SYSP_US_SETUP
   :specializes: SYSP_REQ_SETUP_CONTINUATION
   :realized_by: docs/Syspilot Contracts/setup.md

   Request/manual text shall use the User's language, or English if ambiguous,
   preserving paths/tool/file names and recording the language and reason.

.. vc:: Setup continuation preserves the recorded language choice
   :id: SYSP_VC_SETUP_CONTINUATION_11
   :status: approved
   :verifies: SYSP_REQ_SETUP_CONTINUATION_LANGUAGE

   Text matches the recorded language/reason; paths and tool/file names remain
   unchanged, including under the English ambiguity fallback.

.. req:: Setup Continuation Receipt Evidence
   :id: SYSP_REQ_SETUP_CONTINUATION_RECEIPT
   :status: approved
   :implements: SYSP_US_SETUP
   :specializes: SYSP_REQ_SETUP_CONTINUATION
   :realized_by: docs/Syspilot Contracts/setup.md

   Only Admin's committed Evidence Summary acknowledgement shall prove
   continuation, with up to 120 seconds allowed.
   Queue state shall be diagnostic only: present/notified means announced but
   not yet acted on; present/unnotified means not auto-delivered; absent means
   consumed or deleted, indistinguishably. No state shall prove delivery.
   A committed acknowledgement shall prevent false failure even if the entry is absent.

.. vc:: Admin receipt is evidenced independently of queue consumption
   :id: SYSP_VC_SETUP_CONTINUATION_5
   :status: approved
   :verifies: SYSP_REQ_SETUP_CONTINUATION_RECEIPT

   Only the committed acknowledgement within the wait proves continuation;
   an absent consumed entry cannot negate that evidence.

.. vc:: Queue diagnostics do not claim delivery
   :id: SYSP_VC_SETUP_CONTINUATION_12
   :status: approved
   :verifies: SYSP_REQ_SETUP_CONTINUATION_RECEIPT

   Each of the three queue states has only its declared diagnostic meaning;
   none substitutes for the Admin acknowledgement.

.. req:: Setup Continuation Failure Recovery
   :id: SYSP_REQ_SETUP_CONTINUATION_FAILURE
   :status: approved
   :implements: SYSP_US_SETUP
   :specializes: SYSP_REQ_SETUP_CONTINUATION
   :realized_by: docs/Syspilot Contracts/setup.md

   Missing creation, delivery or timely continuation evidence under
   ``SYSP_REQ_SETUP_CONTINUATION_RECEIPT`` shall produce a delivery blocker,
   no receipt claim and no committed-header change.
   Setup shall give the User the manual path: open Admin's chat from the
   ACTORS view and paste the manual prompt held in the record.

.. vc:: Continuation failure leaves an actionable manual recovery
   :id: SYSP_VC_SETUP_CONTINUATION_13
   :status: approved
   :verifies: SYSP_REQ_SETUP_CONTINUATION_FAILURE

   Unavailable creation/delivery or acknowledgement timeout leaves the committed
   header, records a delivery blocker and offers the ACTORS-chat paste path,
   without claiming receipt.

.. req:: Setup Creates The Actors Through Jarvis
   :id: SYSP_REQ_SETUP_ACTORS
   :status: approved
   :implements: SYSP_US_SETUP
   :specializes: SYSP_REQ_SETUP
   :realized_by: docs/Syspilot Contracts/setup.md

   Setup shall establish exactly nine persistent Actors: Project Manager,
   Architect, Developer, Tester, Quality, Release, Research, Technical Writer
   and Admin, with no Setup actor and unrelated Actors preserved.
   Creation shall use ``jarvis_createActor`` once per non-manually-created Actor,
   with exact name and summary, no initialMessage except transferred Admin.
   Setup shall write neither ``actor.yaml`` nor ``context.md`` and open no Actor session.

   Each one-paragraph summary shall give domain, installed role-card path and
   instruction to read ``docs/<Project name> Contracts/index.md`` each session
   and follow applicable processes. Both paths shall be explicitly
   project-root-relative code spans resolving to installed files.
   Existing Actors shall be shown before creation; ``created: false`` shall
   be recorded as pre-existing and left unchanged, not claimed as configured.
   Created/pre-existing disposition and returned or scanned path shall be
   recorded per Actor and used for persistence decisions and ignore checks.

   The before observation shall scan configured ``jarvis.actors.folder``
   (default ``.jarvis/actors``), listing every actor.yaml folder/name before
   the tool check. It shall not claim equivalence to Jarvis listing.
   Discovery shall use ``jarvis_listActors`` with up to 60 seconds allowed.
   Resumed Setup shall retain its before scan.

   Missing creation tools shall offer ACTORS ``+`` with nine names/summaries.
   Manual creation shall count only expected names absent before, both context
   paths and explicit name-by-name User confirmation. Ambiguous/colliding state
   shall block; missing context paths shall fail the Actor gate with correction
   left to the User. Resumption shall scan for actual Actor paths, not write them.
   Actor creation shall send no messages except the two Admin-request variants
   in ``SYSP_REQ_SETUP_CONTINUATION``. Setup shall disclose
   ``jarvis.actors.openSessionOnCreate`` behavior without editing settings.

.. vc:: Jarvis creation preserves existing Actors
   :id: SYSP_VC_SETUP_ACTORS_1
   :status: approved
   :verifies: SYSP_REQ_SETUP_ACTORS

   Empty and pre-existing-Actor cases show only the expected new Actors created
   through Jarvis, with correct summaries and returned paths; existing files
   and unrelated Actors remain unchanged, and no Setup actor is created.

.. vc:: Actor contexts resolve installed authority sources
   :id: SYSP_VC_SETUP_ACTORS_2
   :status: approved
   :verifies: SYSP_REQ_SETUP_ACTORS

   Every new context contains the domain and both resolvable root-relative paths;
   the paths name installed authority sources.

.. vc:: Actor observations distinguish scanning from discovery
   :id: SYSP_VC_SETUP_ACTORS_3
   :status: approved
   :verifies: SYSP_REQ_SETUP_ACTORS

   The configured-folder before scan precedes tool checks and survives resume;
   it is not claimed as an equivalent Jarvis listing.

.. vc:: Manual Actor creation has explicit provenance
   :id: SYSP_VC_SETUP_ACTORS_4
   :status: approved
   :verifies: SYSP_REQ_SETUP_ACTORS

   User confirmation, before-scan absence and both paths establish each manual
   creation. Ambiguity or missing paths blocks without Setup writing Actor files.

.. vc:: Actor creation sends only the declared continuation request
   :id: SYSP_VC_SETUP_ACTORS_5
   :status: approved
   :verifies: SYSP_REQ_SETUP_ACTORS

   Only the declared Admin continuation request is sent; no other creation-stage
   message or queue write occurs.

.. vc:: Actor persistence uses observed locations
   :id: SYSP_VC_SETUP_ACTORS_6
   :status: approved
   :verifies: SYSP_REQ_SETUP_ACTORS

   Persistence decisions and ignore checks use returned/scanned Actor paths,
   not an assumed folder depth.

.. vc:: Jarvis discovery observes all expected Actors
   :id: SYSP_VC_SETUP_ACTORS_7
   :status: approved
   :verifies: SYSP_REQ_SETUP_ACTORS

   Jarvis discovery lists all nine Actors within the allowed 60-second wait,
   accepting unrelated Actors.

.. vc:: Setup leaves Actor session settings under User control
   :id: SYSP_VC_SETUP_ACTORS_8
   :status: approved
   :verifies: SYSP_REQ_SETUP_ACTORS

   Setup opens no Actor session and explains the auto-open setting without
   editing User or project settings.

.. req:: Setup Verifies Before It Claims
   :id: SYSP_REQ_SETUP_GATES
   :status: approved
   :implements: SYSP_US_SETUP
   :specializes: SYSP_REQ_SETUP
   :realized_by: docs/Syspilot Contracts/setup.md

   Mandatory gates shall be exactly the Phase 5 verification-table rows.
   Every gate shall have evidence and exactly one status: ``pending``,
   ``passed`` or ``failed``. ``PM handoff`` shall be a separate delivery row.
   While any mandatory gate is pending/failed, Contract status shall be
   ``blocked``, baseline status ``preparing``, and a named gate/action blocker
   shall prevent handoff. Discovery after its wait and documentation with any
   warning shall not pass; observed warning count shall be recorded.

   Only all-passed gates shall permit Contract/baseline status ``verified``.
   Before sealing and handoff, record and ``.syspilot/project.toml`` shall be
   re-read; disagreement or an unpassed gate shall stop.
   The post-integration handoff commit shall retain ``verified``, name Project
   Manager, append the log and leave ``PM handoff`` ``pending``.
   Only Project Manager's first commit after refresh, header check and ACK
   shall set ``handed off`` and delivery ``passed``.
   Completion to the User shall await ACK; until then only sent/awaiting may be claimed.
   Failed sending shall leave the record unchanged and provide the User the
   manual Project Manager chat/record-path/refresh route.
   Blockers surviving transfer shall remain visible in the header.

.. vc:: Open or failed gates prevent verification and handoff
   :id: SYSP_VC_SETUP_GATES_1
   :status: approved
   :verifies: SYSP_REQ_SETUP_GATES

   Fixtures where the discovery gate is ``pending`` or documentation gate is
   ``failed`` require status ``blocked``, baseline status ``preparing``, a
   named blocker and no handoff. Final readback compares the record with
   ``.syspilot/project.toml``; disagreement also stops.

.. vc:: Setup gate evidence admits no conditional success
   :id: SYSP_VC_SETUP_GATES_2
   :status: approved
   :verifies: SYSP_REQ_SETUP_GATES

   Exactly the Phase 5 verification rows use the three allowed gate statuses
   with evidence; PM handoff is a delivery row outside that set.

.. vc:: Setup completion is claimed only after receipt
   :id: SYSP_VC_SETUP_GATES_3
   :status: approved
   :verifies: SYSP_REQ_SETUP_GATES

   The sending commit is verified/Project Manager/pending; only that receiver's
   acknowledged first commit sets handed off/passed. Failed sending preserves
   the state and supplies the manual route, not a completion claim.

.. vc:: Setup documentation gate requires recorded zero warnings
   :id: SYSP_VC_SETUP_GATES_4
   :status: approved
   :verifies: SYSP_REQ_SETUP_GATES

   The gate records the observed warning count and passes only when it is zero.

.. req:: Setup Generates A Neutral Documentation Scaffold
   :id: SYSP_REQ_SETUP_DOCS
   :status: approved
   :implements: SYSP_US_SETUP
   :specializes: SYSP_REQ_SETUP
   :realized_by: docs/Syspilot Contracts/setup.md

   Missing documentation configuration/root shall be generated from the
   Contract's definitions using the confirmed project name, shown again during
   additive-edit approval.
   ``docs/conf.py`` shall contain no Syspilot metadata, source-project paths,
   unavailable assets, network inventory or ontology-reference hook.
   It shall load only extensions supplied by installed requirements and needed
   by installed pages; ``sphinxcontrib.mermaid`` is one of them, because the
   installed ontology page contains a link diagram.
   It shall bind the selected ontology
   with literal ``needs_from_toml = "<path relative to conf.py>"``.
   It shall exclude ``changes/*``.
   The root shall list only existing project-named Actor/Contract registries
   and, when Setup installed it, the project-named ontology page;
   each registry shall carry a hidden toctree of exactly installed pages.
   Syspilot's generated ontology reference page shall neither be installed nor generated.
   Existing documentation shall be preserved; navigation integration shall be
   User-approved and additive. Target documentation shall build with zero warnings.

.. vc:: Generated documentation has only target-project inputs
   :id: SYSP_VC_SETUP_DOCS_1
   :status: approved
   :verifies: SYSP_REQ_SETUP_DOCS

   Generated config/root use the confirmed project and installed assets only,
   with no source metadata, network inventory or ontology-reference generation.

.. vc:: Generated navigation is complete and builds strictly
   :id: SYSP_VC_SETUP_DOCS_2
   :status: approved
   :verifies: SYSP_REQ_SETUP_DOCS

   Exact registry toctrees produce zero warnings, including projects with spaces
   in their names.

.. vc:: Existing documentation receives only approved additive edits
   :id: SYSP_VC_SETUP_DOCS_3
   :status: approved
   :verifies: SYSP_REQ_SETUP_DOCS

   Existing files are preserved; offered registry/navigation changes have
   explicit User approval, not replacement.

.. vc:: Setup ontology configuration has a literal binding
   :id: SYSP_VC_SETUP_DOCS_4
   :status: approved
   :verifies: SYSP_REQ_SETUP_DOCS

   Generated configuration binds the selected ontology through a literal
   ``needs_from_toml`` string relative to ``conf.py``, not computed configuration.

.. vc:: Installed ontology diagram renders under the strict build
   :id: SYSP_VC_SETUP_DOCS_5
   :status: approved
   :verifies: SYSP_REQ_SETUP_DOCS

   A target without ontology gets ``sphinxcontrib.mermaid`` loaded in the
   generated configuration and supplied by the installed requirements; an
   existing build receives it only as an approved additive edit, and the
   strict build of the installed ontology page reports zero warnings.

.. req:: Setup Names The Installed Folders After The Project
   :id: SYSP_REQ_SETUP_NAMING
   :status: approved
   :implements: SYSP_US_SETUP
   :specializes: SYSP_REQ_SETUP
   :realized_by: docs/Syspilot Contracts/setup.md

   Setup shall propose the target-folder name and obtain User confirmation
   before Actor scanning, tool checks and destination verification/writes,
   recording one authoritative name in the header.
   Allowed names shall contain only letters, digits, spaces, hyphens,
   underscores and non-leading/non-trailing dots; dots-only and Windows device
   names shall be rejected by asking again, never silently altered.

   Role cards and selected Contracts shall use ``docs/<Project name> Actors/``
   and ``docs/<Project name> Contracts/`` with matching registry titles; a
   copied ontology uses ``docs/<Project name> Ontology/``.
   Registries, root navigation, Actor summaries, handoff and evidence paths,
   and additive navigation proposals shall derive from the same name.
   Seeded files shall remain byte-identical to their examples with no substitution.
   Existing destinations shall follow the retain-identical/approved-integration
   collision rule.
   The name shall become fixed at the first installed-destination write, not
   branch/record/dry-run creation; later changes shall use the scope-change
   rule and reopen affected gates.
   Source/example folders shall keep their names; Setup shall migrate or rename
   no existing installation.

.. vc:: Project naming precedes every dependent path decision
   :id: SYSP_VC_SETUP_NAMING_1
   :status: approved
   :verifies: SYSP_REQ_SETUP_NAMING

   The record confirms the target-derived name before scan/tools/destinations;
   manual summaries already contain it.

.. vc:: Project-named references resolve consistently
   :id: SYSP_VC_SETUP_NAMING_2
   :status: approved
   :verifies: SYSP_REQ_SETUP_NAMING

   A non-Syspilot name containing a space appears consistently in folders,
   registries, summaries, navigation and handoff; paths resolve.

.. vc:: Project renaming respects the write boundary
   :id: SYSP_VC_SETUP_NAMING_3
   :status: approved
   :verifies: SYSP_REQ_SETUP_NAMING

   The first installed-destination write fixes the name; later changes reopen
   affected gates through the scope-change rule.

.. vc:: Project naming does not substitute seeded content
   :id: SYSP_VC_SETUP_NAMING_4
   :status: approved
   :verifies: SYSP_REQ_SETUP_NAMING

   Seeded role cards and Contracts remain byte-identical to their examples,
   without project-name substitution.

.. vc:: Project-named destinations retain the collision disposition
   :id: SYSP_VC_SETUP_NAMING_5
   :status: approved
   :verifies: SYSP_REQ_SETUP_NAMING

   Identical existing files are retained; differing files block unless the
   User approved integration.

.. vc:: Setup leaves source folders and existing installations named
   :id: SYSP_VC_SETUP_NAMING_6
   :status: approved
   :verifies: SYSP_REQ_SETUP_NAMING

   Source/example folders keep their names; Setup neither migrates nor renames
   an existing installation.

.. vc:: Setup rejects invalid project names without transformation
   :id: SYSP_VC_SETUP_NAMING_7
   :status: approved
   :verifies: SYSP_REQ_SETUP_NAMING

   Forbidden characters, leading/trailing dots, dots-only names and reserved
   Windows device names trigger another User choice, not silent sanitization.

.. req:: Setup Integration And Project Manager Handoff
   :id: SYSP_REQ_SETUP_HANDOFF
   :status: approved
   :implements: SYSP_US_SETUP
   :specializes: SYSP_REQ_SETUP
   :realized_by: docs/Syspilot Contracts/setup.md

   Verified Setup shall obtain User guidance for commit/merge and complete
   integration into the selected target branch before sending Project Manager
   ``Installation complete, welcome to this project``.
   The handoff shall include summary, selected ontology/path, installed
   Contracts and first-project guidance to explain ontology artifact types,
   statuses and relationships and ask whether they fit.
   Acceptance shall continue normal intake without an ontology Change;
   requested adjustment shall require a normal Change before modification,
   using the existing Ontology skill only as technical guidance.
   Unmet mandatory conditions shall remain explicit and prohibit success handoff.

.. vc:: Setup handoff follows verified Git integration
   :id: SYSP_VC_SETUP_HANDOFF_1
   :status: approved
   :verifies: SYSP_REQ_SETUP_HANDOFF

   User-guided commit/merge completes before the completion message.

.. vc:: Setup ontology feedback respects Change authority
   :id: SYSP_VC_SETUP_HANDOFF_2
   :status: approved
   :verifies: SYSP_REQ_SETUP_HANDOFF

   Project Manager explains the ontology and asks for fit; acceptance continues
   intake, while adjustment starts a normal Change before editing.

.. vc:: Setup handoff identifies the installed project state
   :id: SYSP_VC_SETUP_HANDOFF_3
   :status: approved
   :verifies: SYSP_REQ_SETUP_HANDOFF

   The completion message carries the installation summary, selected ontology
   and path, installed Contracts and first-project guidance.

.. req:: Later Setup Baseline Updates
   :id: SYSP_REQ_SETUP_UPDATES
   :status: approved
   :implements: SYSP_US_SETUP
   :specializes: SYSP_REQ_SETUP
   :realized_by: docs/Syspilot Contracts/setup.md

   A later technical update shall require a separate project-specific Change
   recording old/proposed baselines, impact, revalidation scope, authorization
   and assigned technical executor.

.. vc:: Baseline updates have separate project authorization
   :id: SYSP_VC_SETUP_UPDATES_1
   :status: approved
   :verifies: SYSP_REQ_SETUP_UPDATES

   Update guidance assigns the six required decisions/evidence items to a
   separate Change, not continued pristine Setup.
