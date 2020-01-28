=====================
Before the Analysis
=====================

Sample Preparation
^^^^^^^^^^^^^^^^^^^^

* Filter samples before injection with a ``Syringe`` and ``Filter``.

	* Syringe filters can be found in the cupboard in the weighing room.
	* Clean syringes can be found in sealed packets in the cupboard under the ``HPLC``.


Pre-Run
^^^^^^^^^

#. Check the indicator lights on the ``Autosampler``, ``Pump``, ``Column``, ``VWD`` and ``MS`` are not ``Red``.

	``Orange``, ``Flashing Orange`` or ``Off`` are OK.

#. Check the valve near the ``ESI`` on the ``MS`` is open (handle in line with pipe) and is connected to ``L`` on the nearby block (shown below)

	.. figure:: images/flow-block.png
		:alt: Check that the pipe is connected to the port marked "L" to the left of this image, not to the port marked "H"

		Check that the pipe is connected to the port marked "L" to the left of this image, not to the port marked "H"

#. Check the levels of the bottles on the front of the ``MS``. Tap the bottles to disturb the liquid if the level is not obvious.

#. Check the levels of the waste bottles in the following locations:

	* Beneath the bench below the ``Pump``/``Autosampler``/``Eluent`` stack
	* Beneath the bench below the ``MS`` and behind the ``Vacuum Pumps``
	* Behind the ``MS``

#. Check there is pressure in the ``Nitrogen Bottle`` behind the ``MS``

#. Check the 3 ``Exhaust Pipes`` are entering the ``Extractor`` for the ``Graphite Furnace``

#. Return to the front of the instrument

#. Fetch some blue towel.

#. Open the ``Ionisation Chamber`` of the ``MS`` and spray ``50% IPA`` around (but not into) the metal surfaces of the inlet orifice.

#. Spray the inside of the ``Ionisation Chamber`` door and wipe with the blue towel.

#. Close the ``Ionisation Chamber``.

#. Open `Mass Hunter Workstation Data Acquisition`.

#. Check the pressures on the top right of the screen are within the following values:

	+-----------+-------------------+
	| Rough Vac | < 4.4×10 :sup:`0` |
	+-----------+-------------------+
	| Quad Vac  | 1×10 :sup:`−5`    |
	|           | - 4×10\ :sup:`−5` |
	+-----------+-------------------+
	| TOC Vac   | 2×10 :sup:`−7`    |
	|           | - 4×10 :sup:`−7`  |
	+-----------+-------------------+

#. Check sufficient eluent is present in the eluent bottles being used for the run.

#. Check that the ``Quat. Pump`` is aware of the level of eluent in the bottles. To do this:

	#. Right click on the ``Quat. Pump`` panel of the `Instrument Status` window in `MassHunter`. <could use image here>
	#. Select :guilabel:`Bottle Fillings` from the menu.
	#. Under `Actual Volume`, ensure the value reflects the volume of eluent actually present in the bottle.

		.. figure:: images/bottle_fillings.PNG
			:alt: The "Bottle Fillings" window

			The "Bottle Fillings" window
	
	#. Click :guilabel:`OK`.
	
	Repeat the above steps when :ref:`Changing Eluent` (see below)


Changing Eluent
^^^^^^^^^^^^^^^^^

When changing eluents, try to swap similar eluents. For example, replace `Ammonium Formate` with `Ammonium Acetate`.

		* The Lids on the bottles do not need to be tight.

To change an eluent, perform the following steps:

#. Right click on the ``QTOF`` panel of the :guilabel:`Instrument Status` window in `MassHunter` and select :guilabel:`LC` → :guilabel:`Waste` from the menu.

	.. figure:: images/instrument_status_qtof.png
		:alt: The Instrument Status window

		The Instrument Status window

#. In the :guilabel:`Method Editor`, under ``Quat. Pump``, set the :guilabel:`Flow Rate` to 0.000 mL/min and press :kbd:`Enter⏎`

#. Open the valve behind the door on the front of the ``Pump``.

#. Set the level of any solvents that weren't changed to 0% and enable the eluents that were changed.

#. Set the :guilabel:`Flow Rate` to 1.000 mL/min and press :kbd:`Enter⏎`

#. Check the pressure in the ``Column`` does not rise above 0 Bar. If it does, check the valve at the front of the ``Pump`` is open.

#. Set the :guilabel:`Flow Rate` to 5.000 mL/min and press :kbd:`Enter⏎`

#. After 5 minutes, set the :guilabel:`Flow Rate` to 0.000 mL/min and press :kbd:`Enter⏎`

#. Close the valve on the front of the ``Pump`` and close the door.

A method can be setup for flushing and equilibrating the column as part of the :guilabel:`Worklist` if desired
