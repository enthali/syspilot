Example Actors And Contracts
============================

.. story:: Example Actors And Contracts
   :id: SYSP_US_EXAMPLES
   :status: approved
   :priority: mandatory
   :tags: example, setup, adoption, documentation
   :tracked_by: ROOT_SYSPILOT

   **As** a project that adopts syspilot and adapts its actors and processes,
   **I want** to receive generic example role cards and Contract processes at
   Setup, kept current by the Technical Writer in every Change,
   **so that** my starting point holds for a general project and I own it
   afterwards, I install only the Contracts I use, and a release needs no
   manual merge of accumulated process changes.

.. ac:: Adopter receives generic copies that the project owns
   :id: SYSP_AC_EXAMPLES_1
   :status: approved
   :validates: SYSP_US_EXAMPLES

   Given the exact release tag supplied to Setup,
   When Setup installs the role cards and Contract processes,
   Then they are copied from the example folders of that release and the
   project adapts them without Setup treating the adaptation as a deviation
   from the release.

.. ac:: Adopter chooses which Contracts to install
   :id: SYSP_AC_EXAMPLES_3
   :status: approved
   :validates: SYSP_US_EXAMPLES

   Given the example Contracts of the supplied release,
   When Setup asks which of them to install, recommending the Change Process
   first,
   Then the project receives the chosen Contracts, the ones they require, and
   a registry that lists exactly those, without any link that does not
   resolve.

.. ac:: Every Change states who maintains the examples
   :id: SYSP_AC_EXAMPLES_2
   :status: approved
   :validates: SYSP_US_EXAMPLES

   Given a Change Contract,
   When it reaches closure,
   Then its ``Example sync`` row records that the Technical Writer carried
   the generally valid changes into the example folders, or records why none
   applied, and the release verifies that row instead of merging the changes.
