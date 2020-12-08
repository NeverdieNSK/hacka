"""
This is the people module and supports all the ReST actions for the
DISCIPLINE collection
"""

# System modules
from datetime import datetime

# 3rd party modules
from flask import make_response, abort


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with our API
DISCIPLINE = {
    "Safarov": {
        "fname": "Razrabotka_PO",
        "lname": "Safarov",
        "timestamp": get_timestamp(),
    },
    "Kyzmichev": {
        "fname": "Fizra",
        "lname": "Kyzmichev",
        "timestamp": get_timestamp(),
    },
    "Ershova": {
        "fname": "English",
        "lname": "Ershova",
        "timestamp": get_timestamp(),
    },
}


def read_all():
    """
    This function responds to a request for /api/people
    with the complete lists of people
    :return:        json string of list of people
    """
    # Create the list of people from our data
    return [DISCIPLINE[key] for key in sorted(DISCIPLINE.keys())]


def read_one(lname):
    """
    This function responds to a request for /api/people/{lname}
    with one matching person from people
    :param lname:   last name of person to find
    :return:        person matching last name
    """
    # Does the person exist in people?
    if lname in DISCIPLINE:
        person = DISCIPLINE.get(lname)

    # otherwise, nope, not found
    else:
        abort(
            404, "Yrok not found".format(lname=lname)
        )

    return Yrok


def create(Yrok):
    """
    This function creates a new person in the people structure
    based on the passed in person data
    :param Yrok:  person to create in people structure
    :return:        201 on success, 406 on person exists
    """
    lname = Yrok.get("lname", None)
    fname = Yrok.get("fname", None)

    # Does the person exist already?
    if lname not in DISCIPLINE and lname is not None:
        DISCIPLINE[lname] = {
            "lname": lname,
            "fname": fname,
            "timestamp": get_timestamp(),
        }
        return DISCIPLINE[lname], 201

    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            "Yrok already exists".format(lname=lname),
        )


def update(lname, Yrok):
    """
    This function updates an existing person in the people structure
    :param lname:   last name of person to update in the people structure
    :param person:  person to update
    :return:        updated person structure
    """
    # Does the person exist in people?
    if lname in DISCIPLINE:
        DISCIPLINE[lname]["fname"] = Yrok.get("fname")
        DISCIPLINE[lname]["timestamp"] = get_timestamp()

        return DISCIPLINE[lname]

    # otherwise, nope, that's an error
    else:
        abort(
            404, "Discipline not found".format(lname=lname)
        )


def delete(lname):
    """
    This function deletes a person from the people structure
    :param lname:   last name of person to delete
    :return:        200 on successful delete, 404 if not found
    """
    # Does the person to delete exist?
    if lname in DISCIPLINE:
        del DISCIPLINE[lname]
        return make_response(
            "{lname} successfully deleted".format(lname=lname), 200
        )

    # Otherwise, nope, Yrok to delete not found
    else:
        abort(
            404, "Yrok not found".format(lname=lname)
        )
