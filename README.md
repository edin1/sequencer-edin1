# sequencer-edin1
An implementation of the [sequencer API](http://docs.sequencer.apiary.io) in Python with flask-restful and pymongo.
# Installation
Clone the git repository to your local machine:

    git clone https://github.com/edin1/sequencer-edin1.git
    cd sequencer_edin1
Install the package (preferably in a [virtualenv](https://virtualenv.pypa.io/en/latest/)) with the usual:

    python setup.py develop
or

    pip install -e .
To check everything is OK, you can run the tests with:

    pip setup.py test
To run the api server with flask's default debug server, use:

    python sequencer_edin1/api.py
