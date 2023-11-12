Verum Verify: Authenticity Verifier for VerumJourno
========================================
.. image:: https://github.com/Ethosym/verumverify/actions/workflows/ci.yml/badge.svg
    :target: https://travis-ci.org/cgdeboer/verumverify

.. image:: https://img.shields.io/pypi/v/verumverify.svg
    :target: https://pypi.org/project/verumverify/

.. image:: https://img.shields.io/conda/vn/conda-forge/verumverify.svg
    :target: https://anaconda.org/conda-forge/verumverify

Verum Verify is a public, open-source library that provides tools for verifying the authenticity
of content posted to verumjourno.com

.. image:: https://github.com/Ethosym/verumverify/blob/main/docs/verumverify.png?raw=true


Example Code:

.. code-block::

    $ verify --hash_id 7708e5e103f71fd65af14a33747755836690545b8873f228dd43bbf17ee42a21

    Verify Authenticity of Hash: 7708e5e103f71fd65af14a33747755836690545b8873f228dd43bbf17ee42a21

    Locating and retrieving files...OK
    Loading public key files...OK
    Loading data and signature files...OK
    Verifying Timestamps Authenticity
    | 2023-11-12 11:25:35 |...OK
    Verifying Sensor Authenticity
    | ccee4e51-daff-4a2f-9dd2-c495252813a0 |...OK
    | b5bb2ee2-5ed8-42b5-ae90-31660b8c77d4 |...OK
    | 5bf8ba9d-7c50-4be7-8f6a-f0fe8d2ee5df |...OK
    Verifying Recording Authenticity
    | c080b0d4-bf06-44f4-9618-c8f1a9b4ca6b |...OK
    Verifying Device Authenticity
    | 8872846e-530b-48e3-8f3b-2bf02806e327 |...OK


How It Works
---------------
Verum Verify provides a single command line callable, :code:`verify` that takes one of
of the following inputs:

hash_id:
    The hash value of a recording from verumjourno.com

id:
    The ID of a recording from verumjourno.com

url:
	The full URL of a recording from verumjourno.com

zipfile:
    A zipfile of all recorded sensor data (downloadable from verumjourno.com)

The :code:`verify` command will verify the authenticity of the recording, the device that
made the recording, all sensor data associated with the recording, and an external timestamp
of when the recording occurred.

Verum Verify officially supports Python 3.6+.

Installation
------------

To install Verum Verify, use:
-  `pipenv <http://pipenv.org/>`_ (or pip, of course)
- `conda <https://docs.conda.io/en/latest/>`_ (or anaconda, or course)
- or wherever you get your python packages.

.. code-block:: bash

    $ pip install verumverify
    $ verify --hash_id <hash>



Documentation
-------------

See https://verumjourno/posts/faq for more information.

Verum Verify relies on these open-source libraries for cryptography and timestamping:
-  `cryptography <https://github.com/pyca/cryptography>`_
-  `rfc3161ng <https://github.com/trbs/rfc3161ng>`_


How to Contribute
-----------------

#. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug.
#. Fork `the repository`_ on GitHub to start making your changes to the **main** branch (or branch off of it).
#. Send a pull request. Make sure to add yourself to AUTHORS_.

.. _`the repository`: https://github.com/cgdeboer/verumverify
.. _AUTHORS: https://github.com/cgdeboer/verumverify/blob/master/AUTHORS.rst
