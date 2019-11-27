==================
Changing Eluent
==================

#. If changing eluent bottles, try to swap similar eluents.

		e.g. Replace `Ammonium Formate` with `Ammonium Acetate`.

		* Lids on bottles do not need to be tight

#. Open the valve behind the door on the front of the ``Pump``.
#. Right click on the ``QTOF`` panel of the :guilabel:`Instrument Status` window in `MassHunter` and select :guilabel:`LC` → :guilabel:`Waste` from the menu.

	.. figure:: instrument_status_qtof.png
		:alt: The Instrument Status window

		The Instrument Status window

#. In the :guilabel:`Method Editor`, under <?>, set the :guilabel:`Flow Rate` to 0.000 mL/min and press :kbd:`Enter⏎`
#. Set the level of any solvents that weren't changed to 0% and enable the eluents that were changed.
#. Set the :guilabel:`Flow Rate` to 1.000 mL/min and press :kbd:`Enter⏎`
#. Check the pressure in the ``Column`` does not rise above 0 Bar. If it does, check the valve at the front of the ``Pump`` is open.
#. Set the :guilabel:`Flow Rate` to 5.000 mL/min and press :kbd:`Enter⏎`
#. After 5 minutes, set the :guilabel:`Flow Rate` to 0.000 mL/min and press :kbd:`Enter⏎`
#. Close the valve on the front of the ``Pump``

A method can be setup for flushing and equilibrating the column as part of the :guilabel:`Worklist` if desired