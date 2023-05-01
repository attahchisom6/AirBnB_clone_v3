#!/usr/bin/python3
"""
This module will be to manipupate city objects using RESTful Api
"""
from flask import abort, make_response
from models.state import State
from models.city import City
from models import Storage
from api.v1.views import app_views


@app_views.route('/states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def list_cities_in_state(state_id):
    """
    list all cities available in a state
    """
    c_list = []
    state = get(State, state_id)
    if state is None:
        abort(404)
    for city in state.cities:
        c_list.append(city)
        c_list = c_list.to_dict()
    return jasonify(c_list)
