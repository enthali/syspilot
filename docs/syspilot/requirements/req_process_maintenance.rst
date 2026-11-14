Process Maintenance Example
===========================

.. req:: Process Maintenance Contract Example
   :id: SYSP_REQ_PROCESS_MAINTENANCE
   :status: approved
   :implements: SYSP_US_PROCESS_MAINTENANCE
   :specializes: SYSP_REQ_CONTRACT_DOCUMENTS
   :realized_by: docs/Example Contracts/process-maintenance.md

   Syspilot shall provide an optional Process Maintenance example that:

   - declares the inherited method's process fields and shared rules, with
     Operation Mode defined by the adopting project;
   - enumerates included templates, registry, role cards, governing instructions
     and skills, assigning changed process documents to Admin;
   - requires Admin's recorded consultation and disposition with every affected
     process owner and, for changed role cards, the described actor, without
     transferring responsibility;
   - records the User-agreed integration target and integration commit in a
     Version control row,
     with the commit required at closure;
   - requires Quality's same-kind peer comparison for duplication, overlap,
     contradiction, missing coverage and responsibility collision, recording
     peer set, evidence, findings and limits;
   - states that the reviewer enumerates peers manually, unlisted peers are
     unexamined, reading-based judgments may differ, and a clean result applies
     only to listed peers;
   - records build, link, schema and mechanical inventories separately as
     supporting checks, not proof of semantic consistency;
   - gains adopter authority only when installed, requires Change and Contract
     Documents, and appears in an adopting registry only after installation; and
   - names the Project Manager as the actor that presents the verified outcome
     after Quality's direct ``proceed`` judgment and evidence.

   The example shall live at ``docs/Example Contracts/process-maintenance.md``
   and be listed in that folder's documentation registry. Syspilot's own process
   changes shall continue through Change; its Needs graph covers specification
   and realization links, while Quality's review verifies Markdown content.

.. vc:: Process Maintenance is an optional adopter Contract
   :id: SYSP_VC_PROCESS_MAINTENANCE_1
   :status: approved
   :verifies: SYSP_REQ_PROCESS_MAINTENANCE

   The example has the inherited process fields and shared rules at the stated
   flat-folder path; links target only Contract Documents and Change. Adopter
   registries list it only when installed, while Syspilot still uses Change.

.. vc:: Process Maintenance consultations preserve factual authority
   :id: SYSP_VC_PROCESS_MAINTENANCE_2
   :status: approved
   :verifies: SYSP_REQ_PROCESS_MAINTENANCE

   Admin's evidence enumerates affected paths and records responses and
   dispositions from each process owner and described actor, without transfer.

.. vc:: Process Maintenance review states its semantic limits
   :id: SYSP_VC_PROCESS_MAINTENANCE_3
   :status: approved
   :verifies: SYSP_REQ_PROCESS_MAINTENANCE

   Quality records same-kind peers and semantic findings with all four manual
   limits; automated supporting checks are separate and claim no Markdown
   consistency guarantee from the Needs graph.

.. vc:: Process Maintenance has evidenced integration
   :id: SYSP_VC_PROCESS_MAINTENANCE_4
   :status: approved
   :verifies: SYSP_REQ_PROCESS_MAINTENANCE

   Closure evidence includes the agreed integration target and actual
   integration commit.

.. vc:: Process Maintenance presents Quality's direct result
   :id: SYSP_VC_PROCESS_MAINTENANCE_5
   :status: approved
   :verifies: SYSP_REQ_PROCESS_MAINTENANCE

   Quality communicates proceed and evidence directly to Project Manager before
   that actor presents the verified outcome to the User.
