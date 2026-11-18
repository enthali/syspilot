Contract Statistics
===================

.. story:: Record What A Contract Cost
   :id: SYSP_US_CONTRACT_STATISTICS
   :status: approved
   :priority: optional
   :tags: skill, statistics, contract
   :tracked_by: ROOT_SYSPILOT

   **As** a User directing Syspilot,
   **I want** the actors' credit use and running time recorded for each
   finished Contract,
   **so that** the cost and effort of Contracts can be compared with evidence
   and discussed, instead of rebuilt by hand from the local session store.

   **Context:**

   The figures describe usage, not quality or value. They are recorded outside
   the Contract and do not replace its evidence.

.. ac:: A finished Contract has a usage record
   :id: SYSP_AC_CONTRACT_STATISTICS_1
   :status: approved
   :validates: SYSP_US_CONTRACT_STATISTICS

   Given a Contract has finished,
   When the Project Manager closes it,
   Then a record shows for each participating actor the credits used and the
   time run within the Contract's window, and a project that runs Syspilot has
   the means to produce it.
