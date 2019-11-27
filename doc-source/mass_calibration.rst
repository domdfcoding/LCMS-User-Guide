============================
Mass Calibration / Check
============================

#. Select :guilabel:`Context` → :guilabel:`Tune` at the top left of the `MassHunter` window.
#. Turn on the ``QTOF`` by clicking the :guilabel:`On` button in its section of the `MassHunter` window.
#. Close the valve near the ``ESI`` on the ``MS``.
#. Set :guilabel:`Calibrant Bottle` to :guilabel:`B` at the bottom left of the :guilabel:`Tune` window.
#. Set :guilabel:`LC Flow to` to :guilabel:`Waste` at the bottom left of the :guilabel:`Tune` window.
#. In the :guilabel:`Tune & Calibration` tab (pictured below) set the instrument parameters required for the run, e.g.:

	* :guilabel:`Positive` – if using +ESI
	* :guilabel:`TOF` - <when you you use both?>
	* :guilabel:`Mass Calibration / Check`
	* :guilabel:`50-1500 m/z`
	.. TODO

	.. highlight:: none

	|

	.. figure:: mass_calibration_window.png
		:alt: View of the Tune & Calibration

		The Tune & Calibration tab

	|

	From Agilent's manual::

		Before you calibrate the instrument, you have to set the instrument state
		to the proper instrument mode, mass range and fast polarity switching mode.
		You set these values on the Instrument State tab.

		When you change the mass range or enable/disable fast polarity switching
		on the Instrument State tab, the pulser frequency is changed which results
		in the DEI pulser warming up or cooling down. If the calibration is
		performed too soon, the DEI may still be heating up or cooling down which
		can result in drift. See the online Help for more information on the
		Instrument State tab.

	.. highlight:: default

#. Click <button text> to start the calibration

#. Once complete, the calibration report will open automatically.

#. Under TOF Mass Calibration Data, for the largest mass check that the resolution is at least 20,000 and that the corrected residuals is below 5 ppm.

#. On Page 2 of the report, under :guilabel:`Detector` → :guilabel:`MCP`, check that the value is below 900.

#. Back in `MassHunter`, return to `Acquistision` mode by selecting :guilabel:`Context` → :guilabel:`Acquisition` at the top left of the window.

#. Open the valve near the ``ESI`` on the ``MS``.
