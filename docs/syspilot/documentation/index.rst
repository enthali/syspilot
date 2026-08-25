User Documentation
==================

These Needs form the Technical Writer-owned documentation ownership map. The
realized documents remain free of Sphinx-Needs markup.

.. doc:: Project README
   :id: SYSP_DOC_README
   :status: verified
   :realized_by: README.md
   :includes: SYSP_REQ_ACTOR_MODEL, SYSP_REQ_SETUP

   The concise project portal for project leads evaluating or returning to
   Syspilot.

.. doc:: Getting Started Guide
   :id: SYSP_DOC_GETTING_STARTED
   :status: verified
   :realized_by: docs/getting-started.md
   :includes: SYSP_REQ_ACTOR_MODEL, SYSP_REQ_SETUP, SYSP_REQ_CONTRACT_DOCUMENTS, SYSP_REQ_TECHNICAL_WRITER

   The shortest supported path from prerequisites to a working Syspilot
   project and first actor interaction.

.. doc:: Product Model Guide
   :id: SYSP_DOC_PRODUCT_MODEL
   :status: verified
   :realized_by: docs/product-model.md
   :includes: SYSP_REQ_ACTOR_MODEL, SYSP_REQ_PROJECT_MANAGER, SYSP_REQ_ARCHITECT, SYSP_REQ_DEVELOPER, SYSP_REQ_TESTER, SYSP_REQ_QUALITY, SYSP_REQ_SETUP, SYSP_REQ_RELEASE, SYSP_REQ_RESEARCH, SYSP_REQ_TECHNICAL_WRITER, SYSP_REQ_CONTRACT_DOCUMENTS, SYSP_REQ_CONTRACT_HANDLING

   A user-oriented explanation of actors, authority, specifications, Contracts,
   memory, and the product-versus-instance boundary.

.. doc:: Change Workflow Guide
   :id: SYSP_DOC_CHANGE_WORKFLOW
   :status: verified
   :realized_by: docs/change-workflow.md
   :includes: SYSP_REQ_CHANGE_CONTRACT, SYSP_REQ_CONTRACT_HANDLING, SYSP_REQ_CONTRACT_DOCUMENTS, SYSP_REQ_PROJECT_MANAGER, SYSP_REQ_ARCHITECT, SYSP_REQ_DEVELOPER, SYSP_REQ_TESTER, SYSP_REQ_QUALITY, SYSP_REQ_TECHNICAL_WRITER, SYSP_REQ_IMPACT_QUERY

   The project lead's journey through a Change, from intent and responsibility
   transfers to validation and closure.

.. doc:: Customization Guide
   :id: SYSP_DOC_CUSTOMIZATION
   :status: verified
   :realized_by: docs/customization.md
   :includes: SYSP_REQ_ACTOR_MODEL, SYSP_REQ_SETUP, SYSP_REQ_CONTRACT_DOCUMENTS, SYSP_REQ_TECHNICAL_WRITER, SYSP_REQ_ONTOLOGY_SCHEMA, SYSP_REQ_ONTOLOGY_EDITING

   Practical guidance for tailoring project Contracts, ontology, documentation,
   specialist Actors, local memory, and skills without losing clean updates.

.. doc:: Operations Guide
   :id: SYSP_DOC_OPERATIONS
   :status: verified
   :realized_by: docs/operations.md
   :includes: SYSP_REQ_SETUP, SYSP_REQ_RELEASE

   Installation, updates, compatibility, recovery, and routine maintenance for
   a Syspilot project.