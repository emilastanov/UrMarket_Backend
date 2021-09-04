from api import app, db
from api import models

from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify
from api.queries import *
from api.mutations import *
from api.config import CLOUDINARY
import cloudinary
import cloudinary.uploader
from flask import request

query = ObjectType("Query")
mutation = ObjectType("Mutation")

query.set_field("listOffers", listOffers_resolver)
query.set_field("getOffer", getOffer_resolver)
query.set_field("listUsers", listUsers_resolver)
query.set_field("getUser", getUser_resolver)
query.set_field("listFAQ", listFAQ_resolver)
query.set_field("listReviews", listReviews_resolver)
query.set_field("getContent", getContent_resolver)

mutation.set_field("addOffer", add_offer_resolver)
mutation.set_field('updateOffer', update_offer_resolver)
mutation.set_field("removeOffer", remove_offer_resolver)
mutation.set_field("addUser", add_user_resolver)
mutation.set_field("removeUser", remove_user_resolver)
mutation.set_field("updateUser", update_user_resolver)
mutation.set_field("addFAQ", add_faq_resolver)
mutation.set_field("removeFAQ", remove_faq_resolver)
mutation.set_field("updateFAQ", update_faq_resolver)
mutation.set_field("addReview", add_review_resolver)
mutation.set_field("removeReview", remove_review_resolver)
mutation.set_field("addContent", add_content_resolver)
mutation.set_field("updateContent", update_content_resolver)
mutation.set_field("removeContent", remove_content_resolver)


type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
)

@app.route("/", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200

@app.route("/", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code

@app.route("/image", methods=["POST"])
def upload_img():
    cloudinary.config(**CLOUDINARY)
    link = cloudinary.uploader.upload(request.files['image'])['url'].split('/')
    return jsonify({"out": '/'.join(link[:-2]+['w_400,h_200,c_fill']+link[-2:])})