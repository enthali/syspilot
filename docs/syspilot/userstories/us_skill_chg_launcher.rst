Change Launcher Skill
=====================

.. story:: Change Launcher Automation
   :id: SYSP_US_CHG_LAUNCHER
   :status: draft
   :priority: mandatory
   :tags: skill, pm, automation
   :links: SYSP_US_PM

   **As a** Project Manager,
   **I want** the mechanical steps of starting a change (branch creation,
   template copy, header pre-fill, initial commit) automated by a script,
   **so that** I can focus immediately on writing the Summary without
   risking errors in the deterministic scaffolding steps.

   **Context:**

   Steps 7–8 of the PM workflow (Create Branch + Create Change Document) are
   fully deterministic given three inputs: change name, author, and operation
   mode. They are a recurring source of errors (wrong fields touched,
   Operation Mode forgotten, CM territory inadvertently modified). A script
   eliminates these errors and saves time.

   **Acceptance Criteria:**

   1. Given a change name, author, and operation mode, When I invoke the launcher, Then a feature branch exists and a pre-filled Change Document is committed.
   2. Given the launcher has run, When I open the Change Document, Then only the header fields are filled and the Summary is empty for me to write.
   3. Given the feature branch already exists, When I invoke the launcher, Then it warns me and continues without failing.
