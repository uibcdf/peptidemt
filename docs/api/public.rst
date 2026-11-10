Public objects
==============

Preparing proposals
-------------------

.. autoclass:: peptidemt.SequenceRecord
   :members:

.. autoclass:: peptidemt.InputRecord
   :members:

.. autofunction:: peptidemt.prepare_sequences

.. autofunction:: peptidemt.parse_fasta

.. autofunction:: peptidemt.read_fasta

Receiving and selecting results
-------------------------------

.. autoclass:: peptidemt.Provenance
   :members:

.. autoclass:: peptidemt.ProviderRow
   :members:

.. autoclass:: peptidemt.Outcome
   :members:

.. autoclass:: peptidemt.ResultSet
   :members:

.. autoclass:: peptidemt.HydrAMPReceipt
   :members:

.. autoclass:: peptidemt.Selection
   :members:

.. autofunction:: peptidemt.select

Selecting the optional Macrel route
-----------------------------------

.. autoclass:: peptidemt.MacrelLimits
   :members:

.. autofunction:: peptidemt.assess_macrel

Selecting the provisional HydrAMP route
----------------------------------------

.. autoclass:: peptidemt.HydrAMPBundle
   :members:

.. autoclass:: peptidemt.HydrAMPLimits
   :members:

.. autofunction:: peptidemt.generate_hydramp

Receiving and composing provisional analogue results
----------------------------------------------------

.. autoclass:: peptidemt.HydrAMPAnalogueReceipt
   :members:
   :undoc-members:

.. autoclass:: peptidemt.AnalogueParentOutcome
   :members:
   :undoc-members:

.. autoclass:: peptidemt.AnalogueLink
   :members:
   :undoc-members:

.. autofunction:: peptidemt.analogue_input_issues

.. autoclass:: peptidemt.HydrAMPAnalogueBundle
   :members:

.. autofunction:: peptidemt.redesign_hydramp
