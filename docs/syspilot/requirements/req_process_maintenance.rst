Process Maintenance Example
===========================

.. req:: Process Maintenance Contract Example
  :id: SYSP_REQ_PROCESS_MAINTENANCE
  :status: approved
  :implements: SYSP_US_PROCESS_MAINTENANCE
  :specializes: SYSP_REQ_CONTRACT_DOCUMENTS
  :realized_by: docs/Syspilot Contracts/examples/process-maintenance.md

   Syspilot shall provide a Process Maintenance Contract example that:

   - follows the Contract Document method, including its shared rules for
     every Contract kind, declaring its applicability, its canonical template
     and concrete instance locations, its initial responsibility, its first
     handoff, its closure responsibility, one owner and completion evidence
     for every artifact, and checkable closure conditions, and refers to the
     adopting project's own mode definitions for its Operation Mode;
   - applies to a project's own process documents, meaning its Contract
     templates, process registry, role cards, and the instructions and skills
     that govern those processes, enumerates the included paths in each
     instance, and names the Admin as owner of the process documents a change
     modifies;
   - requires the Admin to consult each affected process owner and, for a
     changed role card, the actor whose domain the card describes, and to
     record their responses and dispositions, while consultation transfers no
     responsibility;
   - records the User-agreed integration target and the integration commit in
     a Version control row and requires the integration commit at closure;
   - includes a Quality review in which Quality compares each affected
     process document with its peers of the same kind for overlapping or
     duplicated obligation, contradiction, missing coverage, and
     responsibility-boundary collision, and records the selected peer set, the
     evidence, the findings, and the limits in its review-methods table;
   - states the limits of that manual comparison in the example itself: the
     peer set is enumerated by the reviewer and is not discovered by a script,
     because the Needs-based analysis reads specification Needs and not
     Markdown Contracts; a peer the reviewer did not list is not examined; the
     judgment rests on a recorded reading and a second reader may reach a
     different result; and a clean comparison shows that nothing was found
     among the listed peers and nothing beyond them, with build, link, and
     schema checks and any mechanical inventory of the listed peers recorded
     separately as supporting checks that do not establish semantic
     consistency;
   - states its boundary: it is an adopter example whose authority extends to
     the adopting project, it is listed in the process registry apart from
     Syspilot's own processes, and Syspilot's own process documents change
     through the Change process, where the Needs graph covers the
     specification Needs and their realization links and Quality's recorded
     review verifies the Markdown content;
   - names the Project Manager as the actor that presents the verified outcome
     to the User after Quality communicates its ``proceed`` judgment directly
     to the Project Manager, as the Change process does; and
   - lives at ``docs/Syspilot Contracts/examples/process-maintenance.md``,
     listed in the registry index under its own ``Examples`` heading.

.. vc:: Process Maintenance example is a bounded adopter example
   :id: SYSP_VC_PROCESS_MAINTENANCE_1
   :status: approved
   :verifies: SYSP_REQ_PROCESS_MAINTENANCE

   Inspect the example and the registry index and confirm that the example
   declares the Contract Document method's process fields and carries every
   shared rule, names the Admin as owner of the changed process documents,
   covers instructions and skills as well as templates, registry, and role
   cards, requires the consultation of each affected process owner and of the
   described actor for a changed role card, records the integration target
   and commit, carries a Quality review whose review-methods table records
   peer set, evidence, findings, and limits, states the four limits of manual
   comparison, and states its adopter boundary without claiming that the
   Needs graph verifies Markdown content, and names the Project Manager as the
   presenter of the verified outcome to the User. Confirm that the registry lists it under ``Examples`` and not
   under ``Processes``, that Syspilot's own process changes still use the
   Change process, and that the realization link of this Requirement names the
   example.
